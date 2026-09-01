from survey import AnonymousSurvey

# Define a question, and make a survey
question = "Which language did you learn to speak first?"
language_survey = AnonymousSurvey(question)

# Display the question to the users
language_survey.show_question()

# Collect the responses
print("Enter 'q' to quit anytime")
while True:
    response = input("Response - ")
    if response.lower() == "q":
        break
    language_survey.store_responses(response)

# show the results
print("\nThank you for participating in the anonymous survey")
language_survey.show_results()
