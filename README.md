# YouTube Transcript, Subtitles & Telemetry Scraper for RAG / LLM Agents

[![Run on Apify Store](https://img.shields.io/badge/Apify_Store-Run_Actor-00C853?style=for-the-badge&logo=apify)](https://apify.com/willowy_catamaran_fco/youtube-transcript-extractor)
[![MCP Compatible](https://img.shields.io/badge/MCP-AI_Agent_Ready-7C3AED?style=for-the-badge)](https://apify.com/willowy_catamaran_fco/youtube-transcript-extractor/api)
[![n8n & Clay Ready](https://img.shields.io/badge/Integrations-n8n_%7C_Clay_%7C_Make-FF6D5A?style=for-the-badge)](https://apify.com/willowy_catamaran_fco/youtube-transcript-extractor)

Extract clean plain-text transcripts, timestamped Markdown chapters, view counts, and like counts from YouTube videos for AI Agents, RAG pipelines, and n8n workflows.

---

## Why Growth Teams & AI Agents Use This Actor
- **Flat, Pre-Validated JSON Output:** Zero nested arrays - maps directly into **Clay.com columns**, **n8n HTTP Request nodes**, **Make.com**, **HubSpot**, and **Airtable**.
- **High-Concurrency Async Engine:** Powered by concurrent worker pools and TLS browser impersonation (`curl_cffi`) with low 256MB-512MB RAM footprint.
- **MCP & Autonomous Agent Ready:** Runs under `LIMITED_PERMISSIONS` with predictable Pay-Per-Event pricing so Claude, Cursor, LangChain, and CrewAI agents can call it autonomously.

---

## Quick Start: 1-Click API Call (n8n / Clay / cURL)

Use the synchronous endpoint below in **Clay (HTTP API enrichment)** or **n8n (HTTP Request node)** to run the extraction and receive the JSON array in a single request:

```bash
curl -X POST "https://api.apify.com/v2/acts/willowy_catamaran_fco~youtube-transcript-extractor/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "videoUrls": [
    "https://www.youtube.com/watch?v=aircAruvnKk"
  ],
  "preferredLanguage": "en"
}'
```

---

## Sample Input
```json
{
  "videoUrls": [
    "https://www.youtube.com/watch?v=aircAruvnKk"
  ],
  "preferredLanguage": "en"
}
```

## Real Output Sample
```json
{
  "videoId": "aircAruvnKk",
  "title": "But what is a neural network? | Deep learning chapter 1",
  "channelName": "3Blue1Brown",
  "viewCount": 25170338,
  "likeCount": 569649,
  "hasTranscript": true
}
```

---

## Connect to Claude Desktop / Cursor via Apify MCP
Add this Actor to your AI agent toolset using the official Apify MCP Server:
```json
{
  "mcpServers": {
    "apify-b2b-tools": {
      "command": "npx",
      "args": [
        "-y",
        "@apify/actors-mcp-server",
        "--actors",
        "willowy_catamaran_fco/youtube-transcript-extractor"
      ],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

## Keywords & Integrations
`youtube-transcript-api, youtube-scraper, rag-pipeline, llm-data, n8n, langchain, apify-actor, mcp-server`
