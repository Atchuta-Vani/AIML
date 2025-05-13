import requests

UNSPLASH_ACCESS_KEY = "Uf2MpOGSuEvt-d9KxyNoooEA-1sQTkOcdsrWwchpVPM"



def fetch_image_from_unsplash(place):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": place,
        "per_page": 1,
        "client_id": UNSPLASH_ACCESS_KEY
    }
    print("🔍 Type of url:", type(url))
    print("🔍 URL:", url)
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        #print("✅ Data from Unsplash:", data)
        if data["results"]:
            return data["results"][0]["urls"]["regular"]
    return None  # fallback if no image

def print_llm_response(prompt):
    from openai import OpenAI
    ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
    MODEL = "llama3.2"
    messages = [{"role": "user", "content": prompt}]
    response = ollama_via_openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=False
    )
    return response.choices[0].message.content

def llm_response_for_UI(city, country, arrival, departure):
    prompt = f"""I will visit {city}, {country}, for a duration between {arrival} and {departure}.
Please create a daily travel itinerary."""
    
    itinerary_text = print_llm_response(prompt)
    
    # Combine city and country to fetch the image
    place_query = f"{city}, {country}"
    image_url = fetch_image_from_unsplash(place_query)
    
    return {
        "itinerary": itinerary_text,
        "image_url": image_url
    }
    