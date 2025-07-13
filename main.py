from google import generativeai as genai
import os
from dotenv import load_dotenv
from system_inst import instruction


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=instruction
)

chat = model.start_chat(history=[])

print("Chatbot initialized. Type 'exit' to end the conversation.")

while True:
    user_input = input('\nUser: ')

    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    print("Chatbot:")
    try:
        response = chat.send_message(
            user_input,
            generation_config=genai.types.GenerationConfig(
                temperature=1.0,
            ),
            stream=True
        )

        for chunk in response:
            print((chunk.text).replace("*",""), end="")
        print()

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again or check your API key/network connection.")