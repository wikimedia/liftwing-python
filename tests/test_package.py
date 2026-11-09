import liftwing


def test_star_import_exports_all_names():
    namespace = {}
    exec("from liftwing import *", namespace)

    for name in liftwing.__all__:
        assert name in namespace


def test_every_metadata_entry_names_an_exported_class():
    for metadata in liftwing.__metadata__:
        assert hasattr(liftwing, metadata.classname), metadata.classname


def test_metadata_links_do_not_use_the_retired_api_portal():
    # The API portal pages on api.wikimedia.org/wiki redirect to a generic page.
    for metadata in liftwing.__metadata__:
        assert "api.wikimedia.org/wiki" not in metadata.api_documentation_url
        assert "/Proposed/" not in (metadata.wmf_model_card_url or "")
