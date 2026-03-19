# OpenEphemeris Examples

Welcome to the official integration examples repository for [Open Ephemeris](https://openephemeris.com). This repository contains ready-to-run scripts and recipes for seamlessly interacting with the OpenEphemeris API visually, programmatically, and via AI Agents (MCP).

## Structure
- `/python`: Deep data, math queries, and script automation examples.
- `/typescript`: Web rendering, map visualizers (MVT/GeoJSON), and React-ready setups.
- `/curl`: Raw HTTP requests for debugging and rapid prototyping.
- `openapi.json`: The fully documented public API specification. Perfect for feeding to Postman, Swagger, or any local LLM.

## Why OpenEphemeris?
We've done the hard part. We parse the 17,000 year NASA JPL DE440/DE441 ephemeris tables and wrap the Swiss Ephemeris C-bindings in an incredibly fast, highly scalable set of JSON endpoints. No trigonometry required.

You get perfect astrological accuracy, and your AI Agents / LLMs get clean `format=llm` datasets that cut inference token costs by 50%.
