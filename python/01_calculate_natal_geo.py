import os
import requests
import json

# OpenEphemeris Python Integration
# Calculate a Natal Chart with exact planetary positions and aspects

API_KEY = os.getenv("OPENEPHEMERIS_API_KEY", "your_test_key_here")
BASE_URL = "https://api.openephemeris.com"

def generate_natal_data(birth_date: str, longitude: float, latitude: float, format_type="json"):
    """
    Calls the OpenEphemeris API to get precise planetary data for a birth chart.
    If you are feeding this to ChatGPT or Claude, use format_type='llm' to
    drastically compress the JSON tree while maintaining mathematical intent.
    """
    url = f"{BASE_URL}/ephemeris/natal-chart"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # ISO 8601 string or YYYY-MM-DD HH:MM
    payload = {
        "datetime": birth_date,
        "longitude": longitude,
        "latitude": latitude,
        "zodiac": "tropical",
        "house_system": "placidus",
        "include_aspects": True,
        "include_dignities": True
    }
    
    # We support ?format=llm as a query parameter for 50% API response token reduction
    params = {}
    if format_type == "llm":
        params["format"] = "llm"
        
    response = requests.post(url, headers=headers, json=payload, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print("Generating Natal Chart for Carl Jung (born July 26, 1875)...")
    try:
        data = generate_natal_data(
            birth_date="1875-07-26T19:32:00Z",
            longitude=9.3275, # Kesswil, Switzerland
            latitude=47.5939,
            format_type="llm" # Optimised for AI analysis
        )
        print(json.dumps(data, indent=2))
        print("\nNotice how format=llm removed the heavy geometry properties and kept the narrative data!")
    except Exception as e:
        print(e)
