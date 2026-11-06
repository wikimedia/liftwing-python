import liftwing


def test_every_metadata_entry_names_an_exported_class():
    for metadata in liftwing.__metadata__:
        assert hasattr(liftwing, metadata.classname), metadata.classname
