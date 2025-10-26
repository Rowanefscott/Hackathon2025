from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Story character")

trainer = ListTrainer(chatbot)
trainer.train(['How are you?'])

while True: 
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break