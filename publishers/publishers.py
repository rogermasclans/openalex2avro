
SCHEMA_PATH = "./publishers/Publisher.avsc"

from commons import fix_count_by_year, fix_role, fix_summary_stats

def fix_ids(ids: dict) -> dict:
    """
    Fix the ids
    :param ids: ids to fix
    :return: fixed ids
    """
    if ids is None:
        return {
            "openalex": None,
            "ror": None,
            "wikidata": None
        }
    return {
        "openalex": ids.get("openalex"),
        "ror": ids.get("ror"),
        "wikidata": ids.get("wikidata")
    }

def process_publisher(publisher: dict) -> dict:
    """
    Process the author json
    :param author: author dict
    :return: processed author
    """

    return {
        "alternate_titles": publisher.get("alternate_titles") or [""],
        "cited_by_count": int(publisher.get("cited_by_count")) if publisher.get("cited_by_count") is not None else None,
        "country_codes": publisher.get("country_codes") or [""],
        "counts_by_year": [fix_count_by_year(count_by_year)
            for count_by_year in publisher.get("counts_by_year") or [None]
        ],
        "created_date": publisher.get("created_date"),
        "display_name": publisher.get("display_name"),
        "hierarchy_level": int(publisher.get("hierarchy_level")) if publisher.get("hierarchy_level") is not None else None,
        "id": publisher.get("id"),
        "ids": fix_ids(publisher.get("ids")),
        "image_thumbnail_url": publisher.get("image_thumbnail_url"),
        "image_url": publisher.get("image_url"),
        "lineage": publisher.get("lineage") or [""],
        "parent_publisher": publisher.get("parent_publisher") if not isinstance(publisher.get("parent_publisher"), dict) else publisher.get("parent_publisher").get("id"),
        "roles": [fix_role(role)
            for role in publisher.get("roles") or [None]
        ],
        "sources_api_url": publisher.get("image_url"),
        "summary_stats": fix_summary_stats(publisher.get("summary_stats")),
        "updated_date": publisher.get("updated_date"),
        "works_count": int(publisher.get("works_count")) if publisher.get("works_count") is not None else None,
    }
