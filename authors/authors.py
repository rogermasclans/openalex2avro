# Description: This file contains the code to process the author json
# More information on authors can be found here: https://docs.openalex.org/api-entities/authors/author-object

from commons import fix_count_by_year, fix_summary_stats, fix_x_concept, fix_institution

SCHEMA_PATH = './authors/Author.avsc'


def fix_affiliation(affiliation: dict) -> dict:
    """
    Fix the affiliation
    :param affiliation: affiliation to fix
    :return: fixed affiliation
    """
    if affiliation is None:
        return {
            "institution": fix_institution(None),
            "years": None
        }
    return {
        "institution": fix_institution(affiliation.get("institution")),
        "years": affiliation.get("years")
    }

def fix_ids(ids: dict) -> dict:
    """
    Fix the ids
    :param ids: ids to fix
    :return: fixed ids
    """
    if ids is None:
        return {
            "openalex": None,
            "orcid": None,
            "scopus": None,
            "twitter": None, 
            "wikipedia": None
        }

    return {
        "openalex": ids.get("openalex"),
        "orcid": ids.get("orcid"),
        "scopus": ids.get("scopus"),
        "twitter": ids.get("twitter"),
        "wikipedia": ids.get("wikipedia")
    }

def process_author(author:dict)->dict:
    """
    Process the author json
    :param author: author dict
    :return: processed author
    """

    return {
        "affiliations": [fix_affiliation(affiliation) 
            for affiliation in author.get("affiliations") or [None]
        ],
        "cited_by_count": int(author.get("cited_by_count")),
        "counts_by_year": [fix_count_by_year(count_by_year)
            for count_by_year in author.get("counts_by_year") or [None]
        ],
        "created_date": author.get("created_date"),
        "display_name": author.get("display_name"),
        "display_name_alternatives": author.get("display_name_alternatives") or [""],
        "id": author.get("id"),
        "ids": fix_ids(author.get("ids")),
        "last_known_institutions": [fix_institution(institution) 
            for institution in author.get("last_known_institutions") or [None]
        ],
        "orcid": author.get("orcid"),
        "summary_stats": fix_summary_stats(author.get("summary_stats")),
        "updated_date": author.get("updated_date"),
        "works_api_url": author.get("works_api_url"),
        "works_count": int(author.get("works_count")),
        "x_concepts": [fix_x_concept(concept)
            for concept in author.get("x_concepts") or [None]
        ]
    }
