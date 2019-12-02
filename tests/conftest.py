import pytest


@pytest.fixture()
def template():
    return """
version: 1
files: []
templates: {}
"""
