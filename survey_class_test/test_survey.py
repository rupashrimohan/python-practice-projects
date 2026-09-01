import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """A language survey that is available to all test functions"""
    question = "Which language did you learn first to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_anonynous_survey_single_response(language_survey):
    """Testing the class Anonyous survery in the survey module"""
    language_survey.store_responses("English")
    assert "English" in language_survey.responses


def test_anonymous_survey_multiple_response(language_survey):
    """Testing the class for multiple responses"""
    responses = ["English", "Tamil", "Spanish"]
    for each_res in responses:
        language_survey.store_responses(each_res)

    for response in responses:
        assert response in language_survey.responses
