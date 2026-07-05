"""SEO Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_research_keywords():
    """Test Research keywords by volume, difficulty, and search intent."""
    tools = AgentTools()
    result = await tools.research_keywords(seed_keywords="test", market="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_audit_technical_seo():
    """Test Audit website for technical SEO issues."""
    tools = AgentTools()
    result = await tools.audit_technical_seo(url="test", checks="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_backlinks():
    """Test Analyze backlink profile quality and opportunities."""
    tools = AgentTools()
    result = await tools.analyze_backlinks(domain="test", include_competitors=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_rankings():
    """Test Track keyword rankings over time."""
    tools = AgentTools()
    result = await tools.track_rankings(keywords="test", domain="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.seo_agent_agent import SeoAgentAgent
    agent = SeoAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
