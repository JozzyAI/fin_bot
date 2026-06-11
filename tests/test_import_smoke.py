"""Smoke test: verify fin_bot package binds (imports and installs) correctly."""

from importlib.metadata import version

import fin_bot


def test_package_imports():
    assert fin_bot is not None


def test_version_is_accessible():
    assert hasattr(fin_bot, "__version__")
    assert isinstance(fin_bot.__version__, str)
    assert fin_bot.__version__ != ""


def test_package_is_installed_distribution():
    """Catches a broken build/install binding that a plain import would miss.

    pytest adds the repo root to sys.path, so `import fin_bot` succeeds even
    when the package was never actually installed (e.g. a bad build-backend
    breaks `pip install -e .`). Checking the installed distribution metadata
    confirms the package genuinely binds via the packaging toolchain.
    """
    assert version("fin_bot") == fin_bot.__version__
