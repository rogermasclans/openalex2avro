
SCHEMA_PATH = "./works/Work.avsc"

from commons import fix_institution, fix_dehydrated_concept

def reverse_inverted_index(inverted_index):
    """
    Reverse the inverted index to reconstruct the original text.
    """
    # Create a list of tuples (term, doc_id) for each occurrence
    occurrences = [(term, doc_id) for term, doc_ids in inverted_index.items() for doc_id in doc_ids]

    # Sort occurrences based on the doc_id and term
    sorted_occurrences = sorted(occurrences, key=lambda x: (x[1], x[0]))

    # Extract the terms to reconstruct the original text
    reconstructed_text = ' '.join([term for term, _ in sorted_occurrences])

    return reconstructed_text

def fix_ids(ids:dict) -> dict:
    """
    Fix the ids object
    :param ids: ids to fix
    :return: fixed ids
    """
    if not ids:
        return {
            "doi": None,
            "mag": None,
            "pmid": None,
            "pmid": None,
            "pmcid": None
        }
    return {
        "doi": ids.get("doi"),
        "mag": ids.get("mag"),
        "pmid": ids.get("pmid"),
        "pmcid": ids.get("pmcid")
    }
    
def fix_source(source:dict) -> dict:
    if not source:
        return {
            "display_name": None,
            "host_organization": None,
            "host_organization_lineage": [""],
            "host_organization_name": None,
            "id": None,
            "is_in_doaj": None,
            "is_oa": None,
            "issn": [""],
            "issn_l": None,
            "type": None
        }
    return {
        "display_name": source.get("display_name"),
        "host_organization": source.get("host_organization"),
        "host_organization_lineage": source.get("host_organization_lineage") or [""],
        "host_organization_name": source.get("host_organization_name"),
        "id": source.get("id"),
        "is_in_doaj": source.get("is_in_doaj"),
        "is_oa": source.get("is_oa"),
        "issn": source.get("issn") or [""],
        "issn_l": source.get("issn_l"),
        "type": source.get("type")
    }

def fix_location(location:dict) -> dict:
    if not location:
        return {
            "is_accepted": None,
            "is_oa": None,
            "is_published": None,
            "landing_page_url": None,
            "license": None,
            "source": fix_source(None),
            "pdf_url": None,
            "version": None
        }
    else:
        return {
            "is_accepted": location.get("is_accepted"),
            "is_oa": location.get("is_oa"),
            "is_published": location.get("is_published"),
            "landing_page_url": location.get("landing_page_url"),
            "license": location.get("license"),
            "source": fix_source(location.get("source")),
            "pdf_url": location.get("pdf_url"),
            "version": location.get("version")
        }

def fix_open_access(open_access:dict) -> dict:
    if not open_access:
        return {
            "is_oa": None,
            "oa_status": None,
            "oa_url": None,
            "any_repository_has_fulltext": None,
        }
    return {
        "is_oa": open_access.get("is_oa"),
        "oa_status": open_access.get("oa_status"),
        "oa_url": open_access.get("oa_url"),
        "any_repository_has_fulltext": open_access.get("any_repository_has_fulltext"),
    }

def fix_author(authors:dict) -> dict:
    if not authors:
        return {
            "id": None,
            "display_name": None,
            "orcid": None,
        }
        
    return {
        "id": authors.get("id"),
        "display_name": authors.get("display_name"),
        "orcid": authors.get("orcid"),
    }

def fix_authorship(authorship:dict)->dict:
    if not authorship:
        return {
            "author": fix_author(None),
            "author_position": None,
            "countries": [""],
            "institutions": [fix_institution(None)],
            "is_corresponding": None,
            "raw_affiliation_string": None,
            "raw_author_name": None
        }
    return {
        "author": fix_author(authorship.get("author")),
        "author_position": authorship.get("author_position"),
        "countries": authorship.get("countries") or [""],
        "institutions": [fix_institution(institution) for institution in authorship.get("institutions") or [None]],
        "is_corresponding": authorship.get("is_corresponding"),
        "raw_affiliation_string": authorship.get("raw_affiliation_string"),
        "raw_author_name": authorship.get("raw_author_name")
    }

def fix_topic(topic:dict)->dict:
    if not topic:
        return {
            "id": None,
            "display_name": None,
            "subfield": None,
            "field": None,
            "domain": None,
            "score": None
        }
    return {
        "id": topic.get("id"),
        "display_name": topic.get("display_name"),
        "subfield": topic.get("subfield"),
        "field": topic.get("field"),
        "domain": topic.get("domain"),
        "score": topic.get("score")
    }


def fix_biblio(biblio:dict)->dict:
    if not biblio:
        return {
            "volume": None,
            "issue": None,
            "first_page": None,
            "last_page": None
        }
    return {
        "volume": biblio.get("volume"),
        "issue": biblio.get("issue"),
        "first_page": biblio.get("first_page"),
        "last_page": biblio.get("last_page")
    }

def fix_mesh(mesh:dict)-> dict:
    if not mesh:
        return {
            "descriptor_ui": None,
            "descriptor_name": None,
            "qualifier_ui": None,
            "qualifier_name": None,
            "is_major_topic": None
        }
    return {
        "descriptor_ui": mesh.get("descriptor_ui"),
        "descriptor_name": mesh.get("descriptor_name"),
        "qualifier_ui": mesh.get("qualifier_ui"),
        "qualifier_name": mesh.get("qualifier_name"),
        "is_major_topic": mesh.get("is_major_topic")
    }

def fix_sustainable_development_goal(sustainable_development_goal:dict) -> dict:
    if not sustainable_development_goal:
        return {
            "id": None,
            "display_name": None,
            "score": None
        }
    return {
        "id": sustainable_development_goal.get("id"),
        "display_name": sustainable_development_goal.get("display_name"),
        "score": sustainable_development_goal.get("score")
    }

def fix_keyword(keyword:dict) -> dict:
    if not keyword:
        return {
            "id": None,
            "display_name": None,
            "score": None
        }
    return {
        "id": keyword.get("id"),
        "display_name": keyword.get("display_name"),
        "score": keyword.get("score")
    }

def fix_grant(grant:dict) -> dict:
    if not grant:
        return {
            "funder": None,
            "funder_display_name": None,
            "award_id": None
        }
    return {
        "funder": grant.get("funder"),
        "funder_display_name": grant.get("funder_display_name"),
        "award_id": grant.get("award_id")
    }

def fix_price(price:dict) -> dict:
    if not price:
        return {
            "currency": None,
            "value": None,
            "provenance": None,
            "value_usd": None
        }
    return {
        "currency": price.get("currency"),
        "value": price.get("value"),
        "provenance": price.get("provenance"),
        "value_usd": price.get("value_usd")
    }

def fix_cpy(cpy:dict)->dict:
    if not cpy:
        return {
            "min": None,
            "max": None
        }
    return {
        "min": cpy.get("min"),
        "max": cpy.get("max")
    }

def fix_cby(cby:list)->list:
    if not cby:
        return [{
            "year": None,
            "cited_by_count": None
        }]
    return [{
        "year": cby.get("year"),
        "cited_by_count": cby.get("cited_by_count")
    } for cby in cby]

def process_work(work:dict)->dict:
    return {
        "id": work.get("id"),
        "doi": work.get("doi"),
        "doi_registration_agency": work.get("doi_registration_agency"),
        "display_name": work.get("display_name"),
        "title": work.get("title"),
        "publication_year": work.get("publication_year"),
        "publication_date": work.get("publication_date"),
        "language": work.get("language"),
        "ids": fix_ids(work.get("ids")),
        "primary_location": fix_location(work.get("primary_location")),
        "best_oa_location": fix_location(work.get("best_oa_location")),
        "type": work.get("type"),
        "type_crossref": work.get("type_crossref"),
        "open_access": fix_open_access(work.get("open_access")),
        "authorships": [fix_authorship(authorship) for authorship in work.get("authorships") or [None]],
        "countries_distinct_count": int(work.get("countries_distinct_count")) if \
            work.get("countries_distinct_count") is not None else None,
        "institutions_distinct_count": int(work.get("institutions_distinct_count")) if \
            work.get("institutions_distinct_count") is not None else None,
        "corresponding_author_ids": work.get("corresponding_author_ids") or [""],
        "corresponding_institution_ids": work.get("corresponding_institution_ids") or [""],
        "cited_by_count": int(work.get("cited_by_count")) if\
            work.get("cited_by_count") is not None else None,
        "biblio": fix_biblio(work.get("biblio")),
        "is_retracted": bool(work.get("is_retracted")) if\
            work.get("is_retracted") is not None else None,
        "is_paratext": bool(work.get("is_paratext")) if\
            work.get("is_paratext") is not None else None,
        "concepts": [fix_dehydrated_concept(concept) for concept in work.get("concepts") or [None]],
        "mesh": [fix_mesh(mesh) for mesh in work.get("mesh") or [None]],
        "locations_count": int(work.get("locations_count")) if\
            work.get("locations_count") is not None else None,
        "locations": [fix_location(location) for location in work.get("locations") or [None]],
        "referenced_works": work.get("referenced_works") or [""],
        "referenced_works_count": int(work.get("referenced_works_count")) if\
            work.get("referenced_works_count") is not None else None,
        "sustainable_development_goals": [fix_sustainable_development_goal(goal) for goal in work.get("sustainable_development_goals") or [None]],
        "keywords": [fix_keyword(keyword) for keyword in work.get("keywords") or [None]],
        "grants": [fix_grant(grant) for grant in work.get("grants") or [None]],
        "apc_list": fix_price(work.get("apc_list")),
        "apc_paid": fix_price(work.get("apc_paid")),
        "cited_by_percentile_year": fix_cpy(work.get("cited_by_percentile_year")),
        "related_works": work.get("related_works") or [""],
        "counts_by_year": fix_cby(work.get("counts_by_year")),
        "cited_by_api_url": work.get("cited_by_api_url"),
        "updated_date": work.get("updated_date"),
        "created_date": work.get("created_date"),
        "has_fulltext": bool(work.get("has_fulltext")) if\
            work.get("has_fulltext") is not None else None,
        "fulltext_origin": work.get("fulltext_origin"),
        "license": work.get("license"),
        "abstract": reverse_inverted_index(work.get('abstract_inverted_index')) if work.get('abstract_inverted_index') else None,
        "topics": [fix_topic(topic) for topic in work.get("topics") or [None]]
    }
