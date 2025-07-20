"""Module to manage all the constant values used for this repository."""

from typing import ClassVar


class Breaks:

    """Line breaks & Spaces."""

    newline: str = "\n"
    space_2: str = "  "
    strikethrough_start = "\033[9m"
    reset_formatting = "\033[0m"
    tab_2: str = "\t\t"


class Messages:

    """Messages used to be printed during this code execution."""

    default_int_err: str = "Expected integer value. Please retry. (Attempt left : {attempts_left})"
    constrain_err: str = "Only allowed values are {constrains}.\nPlease retry. (Attempt left : {attempts_left})"
    correct_answer: str = ("\nCongratulations {player}! Your answer is correct.\n"
                           "You've won - ${money}.")
    friend_response: str = "Your AI friend thinks the answer for the question : '{question}' could be '{answer}'."
    fifty_fifty_response: str = ("After shortlisting 50-50 process..\n"
                                 "Possible answers could be either '{choice_1}' or '{choice_2}'.\n")
    max_attempt_reached: str = ("You have reached the maximum attempt limit."
                               "Max attempt reached. You must be 'Blind' or 'illiterate'.")
    no_lifeline: str = "\nNo lifeline available. You've already used all the lifelines available.\n"
    player_quit: str = ("That was a wise decision.!\n"
                        "{player} chose to quit the game and leaving with prize money - ${money}.")
    wrong_answer: str = ("\nOops! the answer wasn't correct. You lost the GAME! Mr. {player}\n"
                         "We are sorry to say you are not going to proceed further.! Better luck next time!.\n")


class LLMConst:

    """Open AI LLM constant values used in this repository."""

    api_key: str = "API_KEY"
    api_endpoint: str = "API_ENDPOINT"
    llm_model: str = "MODEL"


class GameValues:

    """Game values constant values used in this repository."""

    answer: str = "answer"
    choices: str = "choices"
    lifeline: tuple = ("l", "L")
    lifeline_options: ClassVar = {
        1: "Phone a Friend",
        2: "50-50",
    }
    player_name: str = "name"
    prize_money: ClassVar = {
        1: 100,  # One Hundred Dollars
        2: 200,  # Two Hundred Dollars
        3: 300,  # Three Hundred Dollars
        4: 500,  # Five Hundred Dollars
        5: 1_000,  # One Thousand Dollars
        6: 2_000,  # Two Thousand Dollars
        7: 4_000,  # Four Thousand Dollars
        8: 8_000,  # Eight Thousand Dollars
        9: 16_000,  # Sixteen Thousand Dollars
        10: 32_000,  # Thirty-Two Thousand Dollars
        11: 64_000,  # Sixty-Four Thousand Dollars
        12: 125_000,  # One Hundred Twenty-Five Thousand Dollars
        13: 250_000,  # Two Hundred Fifty Thousand Dollars
        14: 500_000,  # Five Hundred Thousand Dollars
        15: 1_000_000,  # One Million Dollars (the ultimate grand prize)
    }
    possible_answers: ClassVar = ["1", "2", "3", "4", "L", "l"]
    total_questions: int = 15


class LLMPrompts:

    """LLM prompts constant values used in this repository."""

    fifty_fifty_prompt: str = ("For the question '{question}'."
                               "Form the options : '{choices}', Select exactly two choices."
                               "One must be the correct answer, and one must be a wrong option."
                               "Return the result as a JSON with this format:"
                               "'choices' : ['<choice1>', '<choice2>'], correct_answer: '<correct answer>")
    phone_a_friend_prompt: str = ("Please give me an answer to the question : '{question}' which may have the "
                           "possible answers '{choices}'. What is the correct answer for this question.")
    player_name_prompt: str = "Give me a random scientist name."
    question_prompt: str = ("Generate a General Knowledge question with difficulty level as {difficulty_level} on "
                            "the scale of 1-5, also provide 4 multiple choice to pick the write answer.")
    question_history: str = "The question should not be in the below list of already asked questions."
