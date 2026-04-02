# OpenEphemeris — MCP Server & API Examples

[![npm version](https://img.shields.io/npm/v/@openephemeris/mcp-server)](https://www.npmjs.com/package/@openephemeris/mcp-server)
[![System Status](https://img.shields.io/badge/Status-Live-success)](https://status.openephemeris.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

Official MCP server and integration examples for [Open Ephemeris](https://openephemeris.com) — a NASA JPL DE440/DE441-backed astronomical computation engine for developers and AI agents.

---

## MCP Server — AI Agents (Claude, Cursor, Windsurf)

Give any AI agent access to **48 typed astrological tools** with zero hallucination. Powered by Swiss Ephemeris.

### Quick Install — Claude Desktop

Add to your config file:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "openephemeris": {
      "command": "npx",
      "args": ["-y", "@openephemeris/mcp-server"],
      "env": {
        "OPENEPHEMERIS_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

Get your free API key at [openephemeris.com/dashboard](https://openephemeris.com/dashboard). Free Explorer tier — no credit card required.

### Quick Install — Cursor

Add to `~/.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "openephemeris": {
      "command": "npx",
      "args": ["-y", "@openephemeris/mcp-server"],
      "env": {
        "OPENEPHEMERIS_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

Get your free API key at [openephemeris.com/dashboard](https://openephemeris.com/dashboard).

> Replace `YOUR_API_KEY_HERE` in Cursor's MCP settings after install.

### Other clients — Windsurf, Zed, etc.

See [SETUP.md](./SETUP.md) for platform-specific walkthroughs.

### What you can ask

```
"Calculate a natal chart for 1990-04-15 at 2:30 PM in Chicago."
"Find all Saturn transits to my natal Sun in the next 6 months."
"Get the current moon phase and void-of-course status."
"Find the next solar eclipse visible from Tokyo."
"Find the best electional window to sign a contract in March."
"Generate a Human Design chart for my birth data."
"What is my Vedic (sidereal) chart?"
"Calculate my Chinese BaZi (Four Pillars) chart."
"Show me my Astrocartography power lines — where is my Venus line?"
"Calculate a synastry chart between two people."
"Find the next Venus Star Point and my relationship to it."
"What planetary stations are coming in the next 3 months?"
```

### Tools at a glance

| Category | Tools | Min Tier |
|---|---|---|
| Natal chart | `ephemeris_natal_chart` | Explorer (free) |
| Moon phase & VOC | `ephemeris_moon_phase` | Explorer (free) |
| Human Design | `human_design_chart`, `human_design_composite`, `human_design_penta`, `hd_planetary_return`, `hd_opposition` | Explorer (free) |
| Vedic chart | `vedic_chart` | Explorer (free) |
| Chinese BaZi | `chinese_bazi` | Explorer (free) |
| Venus Star Points | `venus_star_points` + 4 variants | Explorer (free) |
| Progressed chart | `ephemeris_progressed_chart` | Explorer (free) |
| Eclipse finder | `ephemeris_next_eclipse` | Explorer (free) |
| Transit forecast | `ephemeris_transits` | Personal ($9/mo) |
| Synastry & composite | `ephemeris_synastry`, `ephemeris_composite` | Developer ($29/mo) |
| Electional timing | `ephemeris_electional`, `electional_moment_analysis` | Developer ($29/mo) |
| Astrocartography lines | `acg_power_lines` | Developer ($29/mo) |
| ACG hits at location | `acg_hits` | Scale ($199/mo) |
| Chart wheel image | `ephemeris_chart_wheel`, `ephemeris_bi_wheel` | Developer ($29/mo) |

**Full npm package:** [`@openephemeris/mcp-server`](https://www.npmjs.com/package/@openephemeris/mcp-server)

---

## REST API Examples

Ready-to-run scripts for interacting with the OpenEphemeris API directly.

### Repository structure

| Path | Contents |
|---|---|
| [`/python`](./python) | Natal charts, transit searches, Human Design, deep data queries |
| [`/typescript`](./typescript) | Web rendering, GeoJSON map visualizers, React-ready setups |
| [`/curl`](./curl) | Raw HTTP requests for debugging and rapid prototyping |
| [`openapi.json`](./openapi.json) | Full OpenAPI 3.0 spec — import into Postman, Swagger, or any LLM |

### Quick start

```bash
# 1. Get a free API key
open https://openephemeris.com/dashboard

# 2. Try the API
curl -H "Authorization: Bearer YOUR_KEY" \
  "https://api.openephemeris.com/ephemeris/moon/phase"

# 3. Run a Python example
cd python && pip install requests && python natal_chart.py
```

---

## Why OpenEphemeris?

Most LLMs hallucinate astronomical data — planets, degrees, house positions. OpenEphemeris connects AI agents directly to the math.

- **Zero-hallucination accuracy** — sub-arcsecond precision from NASA JPL DE440/DE441
- **LLM-optimized output** — `format=llm` compresses chart responses by ~50%, cutting inference costs
- **111 REST endpoints** across 6 tiers, starting free
- **48 typed MCP tools** — natal, Human Design, Vedic, BaZi, astrocartography, electional, Venus cycles, and more

---

## Links

| | |
|---|---|
| 🔑 Dashboard & API Keys | [openephemeris.com/dashboard](https://openephemeris.com/dashboard) |
| 📖 Documentation | [openephemeris.com/docs](https://openephemeris.com/docs) |
| 💰 Pricing | [openephemeris.com/#pricing](https://openephemeris.com/#pricing) |
| 🟢 Status | [status.openephemeris.com](https://status.openephemeris.com) |
| 📦 npm | [@openephemeris/mcp-server](https://www.npmjs.com/package/@openephemeris/mcp-server) |
| 🐛 Issues | [GitHub Issues](https://github.com/Spirit-River/openephemeris-examples/issues) |
