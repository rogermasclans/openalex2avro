SCHEMA_PATH = "./funders/Funder.avsc"

from commons import fix_count_by_year, fix_role, fix_summary_stats

def fix_ids(ids: dict) -> dict:
    """
    Fix the ids
    :param ids: ids to fix
    :return: fixed ids
    """
    if ids is None:
        return {
            "crossref": None,
            "doi": None,
            "openalex": None,
            "ror": None,
            "wikidata": None
        }
    return {
        "crossref": str(ids.get("crossref")),
        "doi": ids.get("doi"),
        "openalex": ids.get("openalex"),
        "ror": ids.get("ror"),
        "wikidata": ids.get("wikidata")
    }

def process_funder(funder:dict)->dict:
    """
    Process the author json
    :param author: author dict
    :return: processed author
    """

    return {
        "alternate_titles": funder.get("alternate_titles") or [""],
        "cited_by_count": int(funder.get("cited_by_count")) if funder.get("cited_by_count") is not None else None,
        "country_code": funder.get("country_code"),
        "counts_by_year": [fix_count_by_year(count_by_year)
            for count_by_year in funder.get("counts_by_year")
        ],
        "created_date": funder.get("created_date"),
        "description": funder.get("description"),
        "display_name": funder.get("display_name"),
        "grants_count": int(funder.get("grants_count")) if funder.get("grants_count") is not None else None,
        "homepage_url": funder.get("homepage_url"),
        "id": funder.get("id"),
        "ids": fix_ids(funder.get("ids")),
        "image_thumbnail_url": funder.get("image_thumbnail_url"),
        "image_url": funder.get("image_url"),
        "roles": [fix_role(role)
            for role in funder.get("roles")
        ],
        "summary_stats": fix_summary_stats(funder.get("summary_stats")),
        "updated_date": funder.get("updated_date"),
        "works_count": int(funder.get("works_count")) if funder.get("works_count") is not None else None
    }