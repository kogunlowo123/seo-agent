# SEO Agent

[![CI](https://github.com/kogunlowo123/seo-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/seo-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Marketing | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

SEO analysis and optimization agent that performs keyword research, audits technical SEO, analyzes backlink profiles, tracks search rankings, and generates optimization recommendations.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `research_keywords` | Research keywords by volume, difficulty, and search intent |
| `audit_technical_seo` | Audit website for technical SEO issues |
| `analyze_backlinks` | Analyze backlink profile quality and opportunities |
| `track_rankings` | Track keyword rankings over time |
| `generate_recommendations` | Generate prioritized SEO improvement recommendations |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/seo/create` | Create or generate |
| `POST` | `/api/v1/seo/analyze` | Analyze performance |
| `POST` | `/api/v1/seo/optimize` | Optimize |
| `POST` | `/api/v1/seo/schedule` | Schedule |
| `POST` | `/api/v1/seo/report` | Generate report |

## Features

- Seo
- Analytics
- Optimization

## Integrations

- Hubspot Marketing
- Marketo
- Mailchimp
- Google Analytics
- Meta Ads

## Architecture

```
seo-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── seo_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Marketing Platform + LLM + Analytics**

---

Built as part of the Enterprise AI Agent Platform.
