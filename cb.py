from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot('CustomerSupportBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train('chatterbot.corpus.english')

# Simple function to simulate backend processing for complex issues
def escalate_to_human_agent(user_query):
    # In a real scenario, you would perform more complex logic here
    return f"Your issue is complex and has been escalated to a human agent. They will contact you shortly."

# Main function to handle user queries
def customer_support_chatbot(user_query):
    # Use ChatterBot to get a response based on the user's query
    response = chatbot.get_response(user_query)

    # Check if the response confidence is below a certain threshold (indicating uncertainty)
    if response.confidence < 0.5:
        # Escalate to human agent
        response_text = escalate_to_human_agent(user_query)
    else:
        response_text = str(response)

    return response_text

# Example usage
user_input = input("User: ")
while user_input.lower() != 'exit':
    bot_response = customer_support_chatbot(user_input)
    print("Bot:", bot_response)
    user_input = input("User: ")
