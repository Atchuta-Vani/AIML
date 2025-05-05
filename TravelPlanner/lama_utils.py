# Store the LLM response
def print_llm_response(prompt):
    from openai import OpenAI
    ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
    MODEL = "llama3.2"
    messages = [
        {"role": "user", "content": prompt}
    ]
    response = ollama_via_openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=False
    )
    #print(response.choices[0].message.content)
    return response.choices[0].message.content;

# Print in Markdown format
#display(Markdown(response.choices[0].message.content))

def llm_response_for_UI(city,country,duration):
    prompt = f"""I will visit {city}, {country}, for a duration of {duration}. 
Please create a detailed daily itinerary."""
    llm_response = print_llm_response(prompt)
    return llm_response
