# Description: This file contains the functions to process the concept dict

SCHEMA_PATH = './concepts/Concept.avsc'

from commons import fix_count_by_year, fix_dehydrated_concept

def fix_dehydrated_concept_without_score(concept: dict) -> dict:
    """
    Fix the concept
    :param concept: concept to fix
    :return: fixed concept
    """
    if concept is None:
        return {
            "id": None,
            "wikidata": None,
            "display_name": None,
            "level": None,
        }
    return {
        "id": concept.get("id"),
        "wikidata": concept.get("wikidata"),
        "display_name": concept.get("display_name"),
        "level": int(concept.get("level")) if concept.get("level") else None,
    }


def fix_ids(ids: dict) -> dict:
    """
    Fix the ids
    :param ids: ids to fix
    :return: fixed ids
    """
    if ids is None:
        return {
            "mag": None,
            "openalex": None,
            "umls_cui": [""],
            "umls_aui": [""],
            "wikidata": None,
            "wikipedia": None
        }
    return {
        "mag": ids.get("mag"),
        "openalex": ids.get("openalex"),
        "umls_cui": ids.get("umls_cui") or [""],
        "umls_aui": ids.get("umls_aui") or [""],
        "wikidata": ids.get("wikidata"),
        "wikipedia": ids.get("wikipedia")
    }

def process_concept(concept:dict)->dict:
    """
    Process the author json
    :param author: author dict
    :return: processed author
    """

    return {
        "ancestors": [fix_dehydrated_concept_without_score(concept)
            for concept in concept.get("ancestors") or [None]
        ],
        "cited_by_count": int(concept.get("cited_by_count")) if concept.get("cited_by_count") is not None else None,
        "counts_by_year": [fix_count_by_year(count_by_year)
            for count_by_year in concept.get("counts_by_year") or [None]
        ],
        "created_date": concept.get("created_date"),
        "description": concept.get("description"),
        "display_name": concept.get("display_name"),
        "id": concept.get("id"),
        "ids": fix_ids(concept.get("ids")),
        "image_thumbnail_url": concept.get("image_thumbnail_url"),
        "image_url": concept.get("image_url"),
        "related_concepts": [fix_dehydrated_concept(concept)
            for concept in concept.get("related_concepts") or [None]
        ],
        "updated_date": concept.get("updated_date"),
        "wikidata": concept.get("wikidata"),
        "works_api_url": concept.get("works_api_url"),
        "works_count": int(concept.get("works_count")) if concept.get("works_count") is not None else None
    }
