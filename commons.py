

def fix_count_by_year(count_by_year: dict) -> dict:
    """
    Fix the count by year
    :param count_by_year: count by year
    :return: fixed count by year
    """
    if count_by_year is None:
        return {
            "year": None,
            "works_count": None,
            "cited_by_count": None
        }
    return {
        "year": int(count_by_year.get("year")),
        "works_count": int(count_by_year.get("works_count")),
        "cited_by_count": int(count_by_year.get("cited_by_count"))
    }

def fix_role(role: dict) -> dict:
    """
    Fix the role
    :param role: role
    :return: fixed role
    """
    if role is None:
        return {
            "role": None,
            "id": None,
            "works_count": None
        }
    return {
        "role": role.get("role"),
        "id": role.get("id"),
        "works_count": int(role.get("works_count")) if role.get("works_count") is not None else None
    }

def fix_summary_stats(summary_stats: dict) -> dict:
    """
    Fix the summary stats
    :param summary_stats: summary stats to fix
    :return: fixed summary stats
    """
    if summary_stats is None:
        return {
            "secondyr_mean_citedness": None,
            "h_index": None,
            "i10_index": None,

        }
    return {
        "secondyr_mean_citedness": float(summary_stats.get("2yr_mean_citedness")),
        "h_index": int(summary_stats.get("h_index")),
        "i10_index": int(summary_stats.get("i10_index")),
    }

def fix_x_concept(concept: dict) -> dict:
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
            "score": None
        }
    return {
        "id": concept.get("id"),
        "wikidata": concept.get("wikidata"),
        "display_name": concept.get("display_name"),
        "level": int(concept.get("level")),
        "score": float(concept.get("score"))
    }

def fix_institution(institution:dict) -> dict:
    if not institution:
        return {
            "id": None,
            "display_name": None,
            "ror": None,
            "country_code": None,
            "type": None,
            "lineage": [""]
        }
    return {
        "id": institution.get("id"),
        "display_name": institution.get("display_name"),
        "ror": institution.get("ror"),
        "country_code": institution.get("country_code"),
        "type": institution.get("type"),
        "lineage": institution.get("lineage") or [""]
    }

def fix_dehydrated_concept(concept: dict) -> dict:
    """
    Fix the small concept
    :param concept: concept to fix

    :return: fixed concept
    """
    if concept is None:
        return {
            "id": None,
            "wikidata": None,
            "display_name": None,
            "level": None,
            "score": None
        }
    return {
        "id": concept.get("id"),
        "wikidata": concept.get("wikidata"),
        "display_name": concept.get("display_name"),
        "level": int(concept.get("level")) if concept.get("level") is not None else None,
        "score": float(concept.get("score")) if concept.get("score") is not None else None
    }