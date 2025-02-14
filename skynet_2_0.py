import requests
import google.generativeai as genai


DEEPSEEK_API_KEY = "your_deepseek_api_key"
GEMINI_API_KEY = "your_gemini_api_key"

genai.configure(api_key=GEMINI_API_KEY)

def get_deepseek_response(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",  
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def cross_reference_responses(response1, response2):
    if response1.lower() in response2.lower():
        return f"The responses are similar:\n{response1}"
    elif response2.lower() in response1.lower():
        return f"The responses are similar:\n{response2}"
    else:
        return f"DeepSeek says:\n{response1}\n\nGemini says:\n{response2}\n\nConclusion: The responses differ. Please analyze manually."

def main():
    user_prompt = input("Enter your prompt: ")
    
    print("Fetching responses...")
    deepseek_response = get_deepseek_response(user_prompt)
    gemini_response = get_gemini_response(user_prompt)

    conclusion = cross_reference_responses(deepseek_response, gemini_response)
    print("\nFinal Conclusion:\n", conclusion)

if __name__ == "__main__":
    main()