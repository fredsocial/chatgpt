import requests

def chat_with_gpt(prompt, api_key):
    """
    Send a prompt to ChatGPT and return the response.

    Parameters:
    prompt (str): The prompt to send to ChatGPT.
    api_key (str): Your API key for authentication.

    Returns:
    str: The response from ChatGPT.
    """
    url = "https://api.openai.com/v1/engines/chatgpt-model-name/completions"  # replace with the actual API endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150  # adjust as needed
    }

    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    return response_json.get("choices", [{}])[0].get("text", "")

if __name__ == "__main__":
    api_key = "your-api-key"  # replace with your actual API key
    prompt = "Hello, world!"  # replace with your desired prompt
    
    response = chat_with_gpt(prompt, api_key)
    print(response)