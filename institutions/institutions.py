SCHEMA_PATH = "./institutions/Institution.avsc"

from commons import fix_count_by_year, fix_role, fix_summary_stats, fix_x_concept

def fix_dehydrated_institution(institution:dict) -> dict:
    if not institution:
        return {
            "id": None,
            "ror": None,
            "display_name": None,
            "country_code": None,
            "type": None,
            "relationship": None
        }
    return {
        "id": institution.get("id"),
        "ror": institution.get("ror"),
        "display_name": institution.get("display_name"),
        "country_code": institution.get("country_code"),
        "type": institution.get("type"),
        "relationship": institution.get("relationship")
    }


def fix_geo(geo: dict) -> dict:
    """
    Fix the geo
    :param geo: geo
    :return: fixed geo
    """
    if geo is None:
        return {
            "city": None,
            "geonames_city_id": None,
            "region": None,
            "country_code": None,
            "country": None,
            "latitude": None,
            "longitude": None
        }
    return {
        "city": geo.get("city"),
        "geonames_city_id": geo.get("geonames_city_id"),
        "region": geo.get("region"),
        "country_code": geo.get("country_code"),
        "country": geo.get("country"),
        "latitude": float(geo.get("latitude")) if geo.get("latitude") else None,
        "longitude": float(geo.get("longitude")) if geo.get("longitude") else None
    }
def fix_ids(ids: dict) -> dict:
    """
    Fix the ids
    :param ids: ids to fix
    :return: fixed ids
    """
    if ids is None:
        return {
            "grid": None,
            "mag": None,
            "openalex": None,
            "ror": None,
            "wikipedia": None, 
            "wikidata": None
        }
    return {
        "grid": ids.get("grid"),
        "mag": int(ids.get("mag")) if ids.get("mag") else None,
        "openalex": ids.get("openalex"),
        "ror": ids.get("ror"),
        "wikipedia": ids.get("wikipedia"),
        "wikidata": ids.get("wikidata")
    }

def fix_repository(repository: dict) -> dict:
    """
    Fix the repository
    :param repository: repository
    :return: fixed repository
    """
    if repository is None:
        return {
            "id": None,
            "display_name": None,
            "host_organization": None,
            "host_organization_name": None,
            "host_organization_lineage": [""],
        }
    return {
        "id": repository.get("id"),
        "display_name": repository.get("display_name"),
        "host_organization": repository.get("host_organization"),
        "host_organization_name": repository.get("host_organization_name"),
        "host_organization_lineage": repository.get("host_organization_lineage") or [""],
    }

def process_institution(institution:dict)->dict:
    """
    Process the author json
    :param author: author dict
    :return: processed author
    """

    return {
        "associated_institutions": [fix_dehydrated_institution(associated_institution)
            for associated_institution in institution.get("associated_institutions") or [None]
        ],
        "cited_by_count": int(institution.get("cited_by_count")) if institution.get("cited_by_count") is not None else None,
        "country_code": institution.get("country_code"),
        "counts_by_year": [fix_count_by_year(count_by_year)
            for count_by_year in institution.get("counts_by_year") or [None]
        ],
        "created_date": institution.get("created_date"),
        "display_name": institution.get("display_name"),
        "display_name_acronyms": institution.get("display_name_acronyms") or [""],
        "display_name_alternatives": institution.get("display_name_alternatives") or [""],
        "geo": fix_geo(institution.get("geo")),
        "homepage_url": institution.get("homepage_url"),
        "id": institution.get("id"),
        "ids": fix_ids(institution.get("ids")),
        "image_thumbnail_url": institution.get("image_thumbnail_url"),
        "image_url": institution.get("image_url"),
        "lineage": institution.get("lineage") or [""],
        "repositories": [fix_repository(repository)
            for repository in institution.get("repositories") or [None]
        ],
        "roles": [fix_role(role)
            for role in institution.get("roles") or [None]
        ],
        "ror": institution.get("ror"),
        "summary_stats": fix_summary_stats(institution.get("summary_stats")),
        "type": institution.get("type"),
        "updated_date": institution.get("updated_date"),
        "works_api_url": institution.get("works_api_url"),
        "works_count": int(institution.get("works_count")) if institution.get("works_count") is not None else None,
        "x_concepts": [fix_x_concept(concept)
            for concept in institution.get("x_concepts") or [None]
        ]
    }