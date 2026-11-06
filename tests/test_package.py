import liftwing


def test_star_import_exports_all_names():
    namespace = {}
    exec("from liftwing import *", namespace)

    for name in liftwing.__all__:
        assert name in namespace


def test_every_metadata_entry_names_an_exported_class():
    for metadata in liftwing.__metadata__:
        assert hasattr(liftwing, metadata.classname), metadata.classname
