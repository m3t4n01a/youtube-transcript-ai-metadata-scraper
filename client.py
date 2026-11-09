# Official Python Wrapper for YouTube Transcript, Subtitles & Telemetry Scraper for RAG / LLM Agents (willowy_catamaran_fco/youtube-transcript-extractor)
import os
import json
import urllib.request

APIFY_TOKEN = os.environ.get("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/willowy_catamaran_fco~youtube-transcript-extractor/run-sync-get-dataset-items?token=" + APIFY_TOKEN

def run_extraction(payload: dict) -> list[dict]:
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.loads(resp.read().decode("utf-8"))

if __name__ == "__main__":
    sample_payload = {
    "videoUrls": [
        "https://www.youtube.com/watch?v=aircAruvnKk"
    ],
    "preferredLanguage": "en"
}
    print("Triggering willowy_catamaran_fco/youtube-transcript-extractor...")
    print(json.dumps(run_extraction(sample_payload), indent=2))
