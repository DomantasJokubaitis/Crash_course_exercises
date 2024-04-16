messages = ["Hi guys", "What's up", "Are you British?"]
sent_messages = []
    

def send_messages(messages):

    while messages:
        for message in messages:
            sent_message = messages.pop()
            print(sent_message)
            sent_messages.append(sent_message)

send_messages(messages[:])

print(messages)
print(sent_messages)