# Changelog

All notable changes to `@openephemeris/mcp-server` are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Version numbering follows [Semantic Versioning](https://semver.org/).

---

## [3.5.0] — 2026-03-28

### Added
- `POST /ephemeris/draconic` — Draconic chart: full planetary set shifted to True Node as 0° Aries (Explorer tier, 1 credit)
- `POST /ephemeris/prenatal-lunation` — Finds the prenatal new and full moon preceding a subject's birth date (Developer tier, 5 credits)
- `POST /predictive/primary-directions` — Placidian semi-arc primary directions with configurable arc length and body/angle targets (Developer tier, 5 credits)

### Changed
- Total production endpoints: **107 → 110**
- `dev-allowlist.json`, `endpoint-tier-matrix.json`, `llms.txt` all updated to reflect new surface

---

## [3.4.1] — 2026-03-25


### Fixed
- Chiron position fallback for edge-date calculations now uses full Swiss Ephemeris path instead of simplified approximation
- SSE server chart wheel responses now correctly deliver native MCP image blocks instead of raw base64 JSON

### Changed
- Explorer tier daily cap set to 50 credits/day (resets midnight UTC)
- Catalog and metadata endpoints (`/acg/meta`, `/acg/datasets`, `/catalogs/*`) moved to free tier (0 credits)

---

## [3.4.0] — 2026-03-22

### Added
- `hd_planetary_return` tool — finds the exact date when a planet returns to its natal position in HD context
- `hd_opposition` tool — finds the exact date/age of a planet's first opposition (age cycle milestone)
- `venus_star_points`, `venus_eight_year_star`, `venus_elongations`, `venus_phase`, `venus_stations` — complete Venus Star Point toolkit
- `ephemeris_planetary_return` — generic multi-planet support for solar, lunar, and outer planet returns
- `ephemeris_lunar_return` — dedicated monthly lunar return chart

### Changed
- Asteroid data (Chiron, Ceres, Pallas, Juno, Vesta, Pholus) now included by default in natal chart responses
- `ephemeris_transits` tool now includes explicit `aspect_angle` parameter with examples for returns and oppositions

---

## [3.3.0] — 2026-03-21

### Added
- Timezone parameter added to all natal/transit/predictive tools — resolves ambiguous local-time inputs
- `ephemeris_composite_midpoint` — Davison midpoint composite chart
- `ephemeris_fixed_stars` — Ptolemaic fixed star positions with orb and conjunction data
- `ephemeris_hermetic_lots` — Arabic parts / Hermetic Lots (Lot of Fortune, Spirit, etc.)

### Fixed
- ACG power lines now correctly render for southern hemisphere birth locations
- Timezone resolution for "America/Denver" and similar IANA names no longer defaults to UTC

---

## [3.2.0] — 2026-03-21

### Added
- SSE (Server-Sent Events) transport support — enables remote MCP clients without local `npx` installs
- `ephemeris_chart_wheel` and `ephemeris_bi_wheel` tools now deliver native MCP image blocks (PNG)
- Payload size safety cap — responses over 500kb return a structured `PAYLOAD_TOO_LARGE` error

### Fixed
- Composite chart endpoint route corrected in allowlist

---

## [3.1.0] — 2026-03-20

### Added
- `human_design_composite` — dual-chart BodyGraph overlay for relationship analysis
- `human_design_penta` — 5-person Penta composite for group/team dynamics
- `ephemeris_progressed_chart` — secondary progressions (day-for-a-year method)

### Changed
- Personal tier: 1,500 credits/month (formerly 'Maker' at 750)
- Startup tier: 15,000 credits/month (formerly 'Pro')
- Developer tier: 75,000 credits/month

---

## [3.0.0] — 2026-03-15

### Added
- Full tool allowlist security model — default-deny with `config/dev-allowlist.json`
- `dev.call` and `dev.list_allowed` generic proxy tools for allowlisted operations
- `welcome_to_open_ephemeris` MCP Prompt — orientation guide available to MCP clients
- Server icon registered at `https://mcp.openephemeris.com/icon.png`
- `verify:release` npm gate script for pre-publish validation

### Breaking
- Environment variable renamed from `ASTROMCP_API_KEY` to `OPENEPHEMERIS_API_KEY` (old name kept as fallback)
- Package renamed from `@astromcp/server` to `@openephemeris/mcp-server`

---

## [2.x] — Legacy

Earlier versions published under `@astromcp/server`. All users should migrate to `@openephemeris/mcp-server`.

---

*[Unreleased changes are tracked in commit history.]*
