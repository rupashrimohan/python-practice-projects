def send_messages(unsent_messages, sent_messages):
    """Send the unsent messages and move the sent message to anew list"""
    while unsent_messages:
        message = unsent_messages.pop()
        sent_messages.append(message)


unsent_messages = [
    "Hello, how are you?",
    "Is everything ojay wuth you?",
    "Hope, you're having a great day.",
]
sent_messages = []

send_messages(unsent_messages, sent_messages)
print(unsent_messages)
print(sent_messages)

unsent_mess = [
    "Hello, how are you?",
    "Is everything ojay wuth you?",
    "Hope, you're having a great day.",
]
send_messages(unsent_mess[:], sent_messages)
print(unsent_mess)
print(sent_messages)
