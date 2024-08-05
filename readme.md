# openalex2avro

This library transforms OpenAlex snapshots into Avro files, which can then be imported into data warehouses like Google BigQuery, Amazon Redshift, Snowflake, and Microsoft Azure.

[OpenAlex](https://docs.openalex.org/) is a comprehensive and open dataset of scholarly works, authors, institutions, and other entities involved in scientific research. It provides detailed metadata and relationships between these entities, making it a valuable resource for research and analysis in the academic and scientific communities.

## Key Features

- Converts OpenAlex snapshot data into Avro format.
- Ensures compatibility with major data warehouse platforms.
- The Avro file schema adheres to the structure outlined in OpenAlex's documentation, with adjustments based on data inspection.

## Schema Details

The schema of the Avro files is designed to match the structure described in [OpenAlex's documentation](https://docs.openalex.org/api-entities/works/work-object). Due to discrepancies between the documentation and the actual data, some schema adjustments are made based on visual data inspection.

## Getting Started

To use this library, follow the instructions in the [Installation Guide](link-to-guide).

For any questions, feel free to email me at roger.masclans@duke.edu


## Versions

- 1.0.0:
    - Initial version.
    - `summary_stats.2yr_mean_citedness` is renamed to `summary_stats.secondyr_mean_citedness` due to constrain with names beggining with numbers in Apache Avro.
    - international field is dropped from all tables
    - Only the schema for `works` is adapted to include the new variables related to `topics`
