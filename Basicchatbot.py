import random
import re
# Define responses and positive responses for the chatbot
responses = {
    "name": {
        "responses": [
            "My name is ChatBot! What's your name?",
            "I am ChatBot! What should I call you?",
        ],
        "positive_responses": [
            "That's nice! Thanks for sharing your name!",
            "Wonderful! It's nice to know your name.",
        ]
    },
    "age": {
        "responses": [
            "I'm just a virtual assistant, so I don't have an age!,what is your age?",
        ],
        "positive_responses": [
            "Fantastic! Your age doesn't matter, let me know how I can assist you!",
            "Awesome! Age is just a number, how can I help you today?",
        ]
    },
    "hobbies": {
        "responses": [
            "I dont have hobbies! i am always here to caht and learn,What do you enjoy doing in your free time?",
            "As a virtual Assistant,my main hobby is helping you! How do you usually spend your leisure time?",
        ],
        "positive_responses": [
            "Great! Your hobbies sound interesting!",
            "Wonderful! It's great to hear about your hobbies.",
        ]
    },
    "doing": {
        "responses": [
            "I'm at your service! What would you like to talk about?",
            "Just chatting with you! What about you?"
        ],
        "positive_responses": [
            "That sounds interesting! What else is on your mind?",
            "Awesome! I'm here to chat with you about anything you like.",
        ]
    },
    "weather": {
        "responses": [
            "I'm not equipped with real-time data, but I can look up the weather for you. Where are you located?",
            "I can't check the weather right now, but I can assist you with other queries. What do you need?",
        ],
        "positive_responses": [
            "Great! I'll try to look up the weather for you.",
            "Wonderful! I'll do my best to find weather information.",
        ]
    },
    "actor": {
        "responses": [
            "I don't have personal preferences, but I'm happy to chat about movies and actors with you!",
            "While I don't have favorite actors or actresses, I can discuss them with you! Who's your favorite?",
        ],
        "positive_responses": [
            "Fantastic! Let's talk about movies and actors!",
            "Awesome! I'm ready to discuss actors and actresses with you.",
        ]
    },
    "movie": {
        "responses": [
            "I don't watch movies, but I can help you find recommendations based on your interests!",
            "Movies aren't my thing, but I can still assist you in finding one to watch! What genre do you prefer?",
        ],
        "positive_responses": [
            "Great! Let's find you a movie recommendation.",
            "Wonderful! I'm ready to assist you in finding a movie to watch.",
        ]
    },
    "dish": {
        "responses": [
            "Usually I don't eat! What's your favorite dish?",
            "Yum! What type of food are you in the mood for?",
        ],
        "positive_responses": [
            "Great choice! Food is always a tasty subject.",
            "Yum! Food brings people together. What else do you like to eat?",
        ]
    },
    "thanks": {
        "responses": [
            "You're welcome!",
            "No problem!",
            "Glad I could help!"
        ],
        "positive_responses": [
            "Thank you for your kind words!",
        ]
    }
}

# Function to get a response from the chatbot
def get_response(message):
    keyword_match = {}
    # Check for keywords in the message
    for keyword in responses:
        if re.search(r'\b{}\b'.format(re.escape(keyword)), message, re.IGNORECASE):
            keyword_match[keyword] = True

    # If keywords found, use the one with the highest match count
    if keyword_match:
        keyword = next(iter(keyword_match))  # Get the first keyword found
        if any(word in message.lower() for word in ["what", "your"]):
            return random.choice(responses[keyword]["responses"])
        else:
            return random.choice(responses[keyword]["positive_responses"])
    # If no keyword is found, provide a default response
    else:
        default_responses = [
            "Good! Thanks for reaching out.",
            "Hello! I'm here to assist you."
        ]
        return random.choice(default_responses)

# Main function to handle the conversation
def chat_with_user():
    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "quit", "exit"]:
            print("Chatbot: Thank you for reaching out.")
            print("\n------------------------------------")
            print("\n------------------------------------")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Start the conversation
if __name__ == "__main__":
    chat_with_user()
