import requests
import google.generativeai as genai
import openai


DEEPSEEK_API_KEY = "your_deepseek_api_key"
GEMINI_API_KEY = "your_gemini_api_key"
OPENAI_API_KEY = "your_apenai_api_key"

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
        return f"Error from DeepSeek: {response.status_code}, {response.text}"


def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text


def get_chatgpt_summary(deepseek_response, gemini_response):
    openai.api_key = OPENAI_API_KEY

    prompt = (
        "Compare the following responses from DeepSeek and Gemini. "
        "Identify similarities, differences, and provide a summary.\n\n"
        f"DeepSeek Response:\n{deepseek_response}\n\n"
        f"Gemini Response:\n{gemini_response}\n\n"
        "Summary:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]


def main():
    user_prompt = input("Enter your prompt: ")
    
    print("\nFetching responses...")
    deepseek_response = get_deepseek_response(user_prompt)
    gemini_response = get_gemini_response(user_prompt)
    
    print("\nCross-referencing responses with ChatGPT...")
    summary = get_chatgpt_summary(deepseek_response, gemini_response)

    print("\nFinal Summary:\n", summary)

if __name__ == "__main__":
    main()
