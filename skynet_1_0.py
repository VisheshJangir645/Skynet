import google.generativeai as genai

GEMINI_API_KEY = "Your_gemini_api_key"

genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def main():
    user_prompt = input("Enter your prompt: ")
    
    print("Fetching response...")
    gemini_response = get_gemini_response(user_prompt)
    
    print("\nGemini AI Response:\n", gemini_response)

if __name__ == "__main__":
    main()
