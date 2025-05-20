import requests

NUTRITIONIX_APP_ID = "a153a35e"  # Your actual app ID
NUTRITIONIX_API_KEY = "0d5303448af59397032abbe4c5157b7f"  # Your actual API key
NUTRITIONIX_API_URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"

def get_diet_suggestions(food_item):
    """Fetch diet-related info from the Nutritionix API."""
    headers = {
        'x-app-id': NUTRITIONIX_APP_ID,
        'x-app-key': NUTRITIONIX_API_KEY,
        'Content-Type': 'application/json'
    }

    payload = {
        "query": food_item,
        "timezone": "US/Eastern"
    }

    response = requests.post(NUTRITIONIX_API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
