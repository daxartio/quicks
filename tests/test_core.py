from quicks import parse_template_by_stream


def test_parse_template(template):
    files, templates, version = parse_template_by_stream(template)
    assert version == 1
    assert files == []
    assert templates == {}
