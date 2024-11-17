import sys
responses={
    "hello": "Hi there? How can i assist you?",
    "how are you": "I'm just a program, but I'm here to help you!",
    "bye":"Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't understand that. Can you rephrease?",

}

def chatbot_response(user_inp):
    user_inp=user_inp.lower()
    return responses.get(user_inp,responses["default"])

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_inp=input("You:")
    if user_inp.lower()=="bye":
        print("Chatbot:",responses['bye'])
        sys.exit()
    print("Chatbot:",chatbot_response(user_inp))
    
