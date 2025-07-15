import requests

GITHUB_USERNAME = "kjmusichouse"
GITHUB_REPO = "mcq-bank"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{BRANCH}/questions"

# Mapping chapter numbers to folder names
CHAPTER_MAP = {
    1: "the_living_world",
    2: "biological_classification",
    3: "plant_kingdom",
    4: "animal_kingdom",
    5: "morphology_of_flowering_plants",
    6: "anatomy_of_flowering_plants",
    7: "structural_organisation_in_animals",
    8: "cell_the_unit_of_life",
    9: "biomolecules",
    10: "cell_cycle_and_cell_division",
    11: "photosynthesis_in_higher_plants",
    12: "respiration_in_plants",
    13: "plant_growth_and_development",
    14: "breathing_and_exchange_of_gases",
    15: "body_fluids_and_circulation",
    16: "excretory_products_and_their_elimination",
    17: "locomotion_and_movement",
    18: "neural_control_and_coordination",
    19: "chemical_coordination_and_integration",
}

def fetch_quiz_json(cls, subject, chapter, topic):
    """Fetch quiz JSON for a given topic from GitHub."""
    chapter_folder = CHAPTER_MAP.get(int(chapter))
    if not chapter_folder:
        print(f"❌ Chapter {chapter} not mapped.")
        return []

    topic_file = topic.lower().replace(" ", "_") + ".json"
    path = f"class_{str(cls)}/{subject}/{chapter_folder}/{topic_file}"
    url = f"{RAW_BASE}/{path}"
    print(f"🌐 Fetching from: {url}")

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        print("✅ Successfully fetched quiz file")
        return res.json()
    except Exception as e:
        print("❌ Could not fetch quiz file:", e)
        return []
