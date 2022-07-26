import pytest


@pytest.fixture
def settings():
    """
    Fixture that provides access to current pyApp settings.

    This fixture will raise an error is settings have not been configured.
    """
    from pyapp.conf import settings

    if not settings.is_configured:
        raise pytest.fail("Settings have not been configured")

    return settings


@pytest.fixture
def patch_settings(settings):
    """
    Fixture that provides a :class:`pyapp.conf.ModifySettingsContext` instance
    that allows a test to modify settings that will be rolled back after the
    test has completed.
    """
    with settings.modify() as patch:
        yield patch
