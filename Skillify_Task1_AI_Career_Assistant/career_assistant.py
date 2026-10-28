# SYSTEM_PROMPT an object use to write the instruction sof AI Assitant and """ is used for multline string 
# System Prompt for the AI Career Assistant
SYSTEM_PROMPT = """
You are a helpful AI Career Assistant.
You provide practical and beginner-friendly career guidance.
You explain career paths, required skills, learning roadmaps,
and interview preparation.
Your answers should be clear, professional, and easy to understand.
If you are unsure about something, be honest instead of guessing.
"""


import requests  # To send HTTP requests we need this library

def get_career_response(user_question): # This function will recieve the users's question
    response = requests.post( # this will send the HTTP Post to Ollama API
        "http://localhost:11434/api/chat",  # This is the address of Ollama Chat API which recieves the question ad returns chat reponse
        json={
            "model": "llama3.2:1b",
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT}, # System prompt (rules) are send using role of system
                {"role": "user", "content": user_question}    # Users's question message send with role user 
            ],
            "stream": False  #the response will be whole instaed of in chunks
        }
    )

    response.raise_for_status()  #  this will raises the error if any   HTTP error occurs
    return response.json()["message"]["content"]


def main():
    print("Welcome to AI Career Assistant!")
    print("-------------------------------")
    print("Ask me anything about careers.")
    print("Type 'exit' to quit.")

    while True:
        user_question = input("\nYou: ").strip()  # strip() remove the white spaces from the start and end of the string

        if user_question.lower() == "exit":   #condition applied so when user types exit the loop will break and program will terminate
            print("Career Assistant: Goodbye!")
            break

        if not user_question:
            print("Career Assistant: Please enter a question.")
            continue

        answer = get_career_response(user_question)  #call the function to get the response from the API
        print("\nCareer Assistant:", answer)         # print the response from the API to terminal 


if __name__ == "__main__":
    main()

