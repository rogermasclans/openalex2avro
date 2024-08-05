import os
import gzip
import json
from tqdm import tqdm
from avro import schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter
from concurrent.futures import ProcessPoolExecutor, as_completed

from utils import retrieve_folders_in_dir, create_dir

from sources.sources import process_source
from sources.sources import SCHEMA_PATH as sources_schema_path

from authors.authors import process_author
from authors.authors import SCHEMA_PATH as authors_schema_path

from works.works import process_work
from works.works import SCHEMA_PATH as works_schema_path

from institutions.institutions import process_institution
from institutions.institutions import SCHEMA_PATH as institutions_schema_path

from concepts.concepts import process_concept
from concepts.concepts import SCHEMA_PATH as concepts_schema_path

from publishers.publishers import process_publisher
from publishers.publishers import SCHEMA_PATH as publishers_schema_path

from funders.funders import process_funder
from funders.funders import SCHEMA_PATH as funders_schema_path


RAW_DATA_LOCATION = '[raw_data_location]'
CONVERTED_DATA_LOCATION = '[converted_data_location]'


def json_to_avro(input_file: str, destination_file: str,
                 schema_location: str, process_json: callable) -> dict:
    """
    This function will convert a jsonl file to an avro file using the schema provided
    and the process_json function to process the json data

    :param input_file: input jsonl file
    :param destination_file: destination avro file
    :param schema_location: location of the schema file
    :param process_json: function to process the json data

    :return: number of works processed
    """
    avro_schema = schema.parse(open(schema_location).read())
    writer = DataFileWriter(open(destination_file, "wb"),
                            DatumWriter(), avro_schema, codec="deflate")
    counter = 0
    with gzip.open(input_file, 'r') as jsonl:
        pbar = tqdm(jsonl, desc="Files counter: ")
        for json_file in pbar:
            if not json_file.strip():
                continue
            json_file = json.loads(json_file)
            pbar.set_description(f"Processing {json_file.get('id')}")
            writer.append(process_json(json_file))
            counter += 1
    writer.close()

    return


def execute_processes_parallel(input_data_root: str, destination_data_root: str, table: str,
                               process_function: callable, schema_path: str):
    """
    This function will execute the process_function for each file in the input_data_root
    and save the result in the destination_data_root

    :param input_data_root: root folder of the input data
    :param destination_data_root: root folder of the destination data
    :param table: table to process (e.g. authors, works, etc.)
    :param process_function: function to process the data
    :param schema_path: path to the schema file
    """
    input_table_folder = os.path.join(input_data_root, table)
    destination_table_folder = os.path.join(destination_data_root, table)

    # Retrieve all the folders in the raw works directory
    subdirs = retrieve_folders_in_dir(input_table_folder)
    [
        create_dir(os.path.join(destination_table_folder, dir)) for dir in subdirs
    ]

    with ProcessPoolExecutor() as executor:
        # Using submit to parallelize transform_work function
        futures = [
            executor.submit(
                json_to_avro,
                os.path.join(
                    input_table_folder,
                    subdir,
                    jsonl_file_name
                ),
                os.path.join(
                    destination_table_folder,
                    subdir,
                    jsonl_file_name
                ).strip('gz') + 'avro',
                schema_path,
                process_function
            )
            for subdir in subdirs
            for jsonl_file_name in os.listdir(os.path.join(input_table_folder, subdir))
        ]

        # Wait for all tasks to complete
        list(tqdm(as_completed(futures), total=len(
            futures), desc="Files processing"))
    return

def execute_processes(
    input_data_root: str, destination_data_root: str, table: str,
    process_function: callable, schema_path: str
):
    """
    This function will execute the process_function for each file in the input_data_root
    and save the result in the destination_data_root

    :param input_data_root: root folder of the input data
    :param destination_data_root: root folder of the destination data
    :param table: table to process (e.g. authors, works, etc.)
    :param process_function: function to process the data
    :param schema_path: path to the schema file
    """
    input_table_folder = os.path.join(input_data_root, table)
    destination_table_folder = os.path.join(destination_data_root, table)

    # Retrieve all the folders in the raw works directory
    subdirs = retrieve_folders_in_dir(input_table_folder)
    [
        create_dir(os.path.join(destination_table_folder, dir)) for dir in subdirs
    ]

    for subdir in subdirs:
        for jsonl_file_name in os.listdir(os.path.join(input_table_folder, subdir)):
            json_to_avro(
                input_file=os.path.join(input_table_folder, subdir, jsonl_file_name),
                destination_file=os.path.join(destination_table_folder, subdir, jsonl_file_name).strip('gz') + 'avro',
                schema_location=schema_path,
                process_json=process_function
            )
    return

def main():
    # execute_processes_parallel(RAW_DATA_LOCATION, CONVERTED_DATA_LOCATION,
    #                   'sources', process_source, sources_schema_path)
    # execute_processes(RAW_DATA_LOCATION, CONVERTED_DATA_LOCATION,
    #                   'authors', process_author, authors_schema_path)
    execute_processes_parallel(RAW_DATA_LOCATION, CONVERTED_DATA_LOCATION,
                      'works', process_work, works_schema_path)
    # execute_processes_parallel(RAW_DATA_LOCATION, CONVERTED_DATA_LOCATION,
    #                   'institutions', process_institution, institutions_schema_path)
    # execute_processes(RAW_DATA_LOCATION, CONVERTED_DATA_LOCATION,
    #                   'concepts', process_concept, concepts_schema_path)
    # execute_processes(RAW_DATA_LOCATION, CONVERTED_DATA_LOCATION,
    #                   'publishers', process_publisher, publishers_schema_path)
    # execute_processes(RAW_DATA_LOCATION, CONVERTED_DATA_LOCATION,
    #                     'funders', process_funder, funders_schema_path)
    print("FINISHED")

if __name__ == '__main__':
    main()
