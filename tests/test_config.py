"""Tests for the configuration module."""

import pytest

from demo_cli.config import Settings, get_settings


@pytest.mark.unit
def test_settings_defaults() -> None:
    """Test settings with default values."""
    settings = Settings()
    assert settings.app_name == "Demo CLI"
    assert settings.debug is False
    assert settings.log_level == "INFO"
    assert settings.environment == "development"


@pytest.mark.unit
def test_settings_custom_values() -> None:
    """Test settings with custom values."""
    settings = Settings(
        app_name="Test App",
        debug=True,
        log_level="DEBUG",
        environment="production",
    )
    assert settings.app_name == "Test App"
    assert settings.debug is True
    assert settings.log_level == "DEBUG"
    assert settings.environment == "production"


@pytest.mark.unit
def test_get_settings_caching() -> None:
    """Test that get_settings returns cached instance."""
    settings1 = get_settings()
    settings2 = get_settings()
    assert settings1 is settings2
