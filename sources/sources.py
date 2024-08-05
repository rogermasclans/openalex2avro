# Description: This file contains the code to process the source json
# More information on sources can be found here: https://docs.openalex.org/api-entities/sources/source-object

SCHEMA_PATH = './sources/Source.avsc'

from commons import fix_count_by_year, fix_summary_stats, fix_x_concept

def fix_price(price: dict) -> dict:
    """
    Fix the price
    :param price: price to fix
    :return: fixed price
    """
    if price is None:
        return {
            "price": None,
            "currency": None
        }
    return {
        "price": int(price.get("price")) if price.get("price") is not None else None,
        "currency": price.get("currency")
    }

def fix_ids(ids: dict) -> dict:
    """
    Fix the ids
    :param ids: ids to fix
    :return: fixed ids
    """
    if ids is None:
        return {
            "fatcat": None,
            "issn": [""],
            "issn_l": None,
            "mag": None, 
            "openalex": None,
            "wikidata": None
        }

    return {
        "fatcat": ids.get("fatcat"),
        "issn": ids.get("issn") or [""],
        "issn_l": ids.get("issn_l"),
        "mag": int(ids.get("mag")) if ids.get("mag") else None,
        "openalex": ids.get("openalex"),
        "wikidata": ids.get("wikidata")
    }

def fix_society(society: dict) -> dict:
    """
    Fix the society
    :param society: society to fix
    :return: fixed society
    """
    if society is None:
        return {
            "url": None,
            "organization": None
        }
    return {
        "url": society.get("url"),
        "organization": society.get("organization")
    }

def process_source(source:dict)->dict:
    """
    Process the author json
    :param author: author dict
    :return: processed author
    """

    return {
        "abbreviated_title": source.get("abbreviated_title"),
        "alternate_titles": source.get("alternate_titles") or [""],
        "apc_prices": [fix_price(price) 
            for price in source.get("apc_prices") or [None]
        ],
        "apc_usd": int(source.get("apc_usd")) if source.get("apc_usd") is not None else None,
        "cited_by_count": int(source.get("cited_by_count")) if source.get("cited_by_count") is not None else None,
        "country_code": source.get("country_code"),
        "counts_by_year": [fix_count_by_year(count_by_year)
            for count_by_year in source.get("counts_by_year") or [None]
        ],
        "created_date": source.get("created_date"),
        "display_name": source.get("display_name"),
        "homepage_url": source.get("homepage_url"),
        "host_organization": source.get("host_organization"),
        "host_organization_lineage": source.get("host_organization_lineage") or [""],
        "host_organization_name": source.get("host_organization_name"),
        "id": source.get("id"),
        "ids": fix_ids(source.get("ids")),
        "is_in_doaj": bool(source.get("is_in_doaj")) if source.get("is_in_doaj") is not None else None,
        "is_oa": bool(source.get("is_oa")) if not source.get("is_oa") is not None else None,
        "issn": source.get("issn") or [""],
        "issn_l": source.get("issn_l"),
        "societies": [fix_society(society)
            for society in source.get("societies") or [None]
        ],
        "summary_stats": fix_summary_stats(source.get("summary_stats")),
        "type": source.get("type"),
        "updated_date": source.get("updated_date"),
        "works_api_url": source.get("works_api_url"),
        "works_count": int(source.get("works_count")) if source.get("works_count") is not None else None,
        "x_concepts": [fix_x_concept(concept)
            for concept in source.get("x_concepts") or [None]
        ]
    }
