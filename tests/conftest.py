"""Test configuration for SEO Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "seo-agent", "category": "Marketing"}
