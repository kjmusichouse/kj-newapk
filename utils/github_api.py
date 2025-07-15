import requests

GITHUB_USERNAME = "kjmusichouse"
GITHUB_REPO = "mcq-bank"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{BRANCH}/questions"

def fetch_quiz_json(cls, subject, chapter, topic):
    path = f"class_{str(cls)}/{subject}/{chapter}/{topic}.json"
    url = f"{RAW_BASE}/{path}"
    print(f"Attempting to fetch from: {url}")
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("❌ Could not fetch quiz file:", e)
        return []
