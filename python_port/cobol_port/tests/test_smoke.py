"""Smoke tests for auto-generated `cobol_port` port."""

import importlib

PKG = "cobol_port"


def test_package_imports():
    mod = importlib.import_module(PKG)
    assert mod.__cobol_program__ == "ESCAL056"
    assert mod.__paragraphs__ == 8


def test_tables_loaded():
    tables = importlib.import_module(f"{PKG}.tables")
    assert tables.TABLES, "no tables loaded"


def test_return_codes_complete():
    from cobol_port import return_codes
    assert len(return_codes.RETURN_CODES) == 9
