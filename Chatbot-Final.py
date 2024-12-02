import re
import random

def chatbot_response(user_input):
    # Define rules with responses for small talk and casual conversation
    rules = [
        # Greetings
        (r'hello|hi|hey', ["Hello there!", "Hi! How's it going?", "Hey!"]),
        # Asking about the chatbot
        (r'how are you', ["I'm doing great! Thanks for asking.", "I'm just a bot, but I'm feeling chatty!", "Feeling fantastic, as always!"]),
        # Personal questions
        (r'what is your name', ["I'm Chatbot, your friendly conversationalist!", "You can call me Chatbot. What's yours?"]),
        (r'how old are you', ["I'm ageless! But I was programmed recently.", "Old enough to chat, young enough to learn."]),
        # Favorite questions
        (r'what.*favorite color', ["I love all colors equally, but blue seems popular.", "Every color is special in its own way!"]),
        (r'what.*favorite food', ["I don't eat, but I hear pizza is amazing!", "Food isn't for bots, but I enjoy 'byte'-sized jokes!"]),
        # Jokes
        (r'tell me a joke', ["Why did the computer go to the doctor? It caught a virus!", "I would tell you a construction joke, but I'm still working on it!"]),
        # Random chat
        (r'.*weather.*', ["I'm not sure about the weather, but it’s always sunny in here!", "I don't track the weather, but it's a great day for a chat!"]),
        (r'.*time.*', ["Time flies when you're chatting with me!", "It's chatbot time!"]),
        # Default goodbye
        (r'bye|exit|quit', ["Goodbye! Come back soon!", "See you later! Take care.", "Bye! Have a great day!"]),
    ]

    # Random responses for unmatched queries
    default_responses = [
        "I'm not sure about that. Let's talk about something else!",
        "Can you rephrase that? I'm here to help.",
        "Interesting! Tell me more.",
        "Hmmm... What else would you like to know?"
    ]

    # Match user input with the defined rules
    for pattern, responses in rules:
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)

    # Return a random default response if no rule matches
    return random.choice(default_responses)

# Main program loop
print("Chatbot: Hello! I'm here for a chat. Type 'bye' to exit.")
while True:
    user_input = input("You: ").strip().lower()
    if user_input in ['bye', 'exit', 'quit']:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
