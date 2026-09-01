class AnonymousSurvey:
    """Collect anonymous answers to a survey question"""

    def __init__(self, question):
        """initialize the question and responses attributes"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the survey question"""
        print(self.question)

    def store_responses(self, new_response):
        """Add the new responses to the list responses"""
        self.responses.append(new_response)

    def show_results(self):
        """Prints all the responses"""
        print("Survey results:")
        for response in self.responses:
            print(f" - {response}")
