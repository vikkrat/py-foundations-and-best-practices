from models.messages import messages

# Starts the session and says Hello! How can I help you?
def start_session()-> None:
    print(messages['hello'])