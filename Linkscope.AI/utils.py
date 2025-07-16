import requests

def analyze_with_llm(profile_text):
    prompt = f"""
    You are a career coach. Analyze the following LinkedIn profile content and give:
    1. Strengths
    2. Weaknesses
    3. Suggestions to improve
    4. A rewritten summary
    
    Profile content:
    {profile_text}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )

    return response.json().get("response", "Error generating response.")
