"""Smoke test: verify fin_bot package binds (imports) correctly."""

import fin_bot


def test_package_imports():
    assert fin_bot is not None


def test_version_is_accessible():
    assert hasattr(fin_bot, "__version__")
    assert isinstance(fin_bot.__version__, str)
    assert fin_bot.__version__ != ""
