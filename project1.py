# Max Bader Project 1 ICS31 11/12/202import random
from project1_quotes import *


def is_question(string):
    """
    Access the last character of a string by using -1 as the index af this character is a '?' then the function is True.
    
    Returns_
        The function returns True if the string is a question. Otherwise it returns False.
    """
    if string[-1] == '?':
        return True
    else:
        return False


def get_first_quotes(data):
    """
    List is searched through each tuple and gets the first element of every tuple which are added to first_items.
    
    Args_
        data: (list) this list contains a list of tuples containing quotes
    Returns_
        The function returns a new list containing the first elements of each of the tuples
    """
    first_items = []
    for tuples in data:
        first_items.append(tuples[0])
    return first_items


def get_first_questions(data):
    """
    Function checks every element inside every tuple in a given list. The function checks if the element
    is a question using the is_question function and then the function will add that element to a new list
    called first_questions. This list will eventually contain every string that is a question.
    
    Args_
        data: (list) this list contains a list of tuples containing quotes from movies
    Returns_
        The function returns a new list called first_questions. This list contains all of the questions inside
        of the given list.
    """
    first_questions = []
    for element in get_first_quotes(data):
        if is_question(element):
            first_questions.append(element)
    return first_questions


def count_questions_quotes(data):
    """
    Function gets the length of the list returned by the function get_first_questions.
    
    Args_
        data: (list) this list contains a list of tuples containing quotes from movies
    Returns_
        The function returns the length of the list that is returned from the function get_first_questions.
        It will return the number of elements inside of the list.
    """
    return len(get_first_questions(data))


quotes = get_quotes()
count_questions_quotes(quotes)
# There are 71117 quotes that are questions


def get_average_question_length(data):
    """
    Function returns the average length of the elements inside of the list returned by the previous function get_first_questions().
    
    Args_
        data: (list) this list contains a list of tuples containing quotes from movies.
    Returns_
        The function returns a number which is the average length of the questions inside of the list returned
        from the get_first_questions() function.
    """
    length = 0
    first_questions = get_first_questions(data)
    for question in first_questions:
        length += len(question)
    return length / len(first_questions)


# ------------------------------------------------------------
# Chatbot Section

def get_responses(data, question):
    """
    Function iterates through a list of tuples. If the parameter, question, is inside of a tuple, it will
    return the response paired to that tuple. It accesses the first element inside of a tuple and if it is equal
    to the question it will return the second element of that tuple.
    
    Args_
        data: (list) this is a list of tuples that contain movie quotes with a question and response
        question: (string) this string is a question that the user wants to find inside of the list of tuples
    Returns_
        The function returns a list of responses to the provided question.
    """
    first_questions = []
    for tuples in data:
        if question == tuples[0]:
            first_questions.append(tuples[1])
    return first_questions

def get_random_from_list(data):
    """
    Function takes in a list and gets a random number from the range of how long the list is. It will then
    give the list at the index of that random number.
    
    Args_
        data: (list) the function takes in any list
    Returns_
        The function returns the list at the index of the random number provided from the range of the length
        of the list
    """
    index = random.randrange(len(data)-1)
    return data[index]


def respond(data, question):
    """
    Function gives a random response from the list of responses returned from get_responses if the question
    exactly matches a question in the data set.
    
    Args_
        list: (list) this list has tuple pairs that contain movie questions and answers
        question: (string) this question is a string provided by the user
    Returns_
        The function returns a random response if the provided question is matched with a question from the list.
        If there is a question then the function will return the random response, but if there is not an exact
        match it will return the string "I don't know."
    """
    responses = get_responses(data, question)
    if len(responses) > 0:
        random_response = get_random_from_list(responses)
        return random_response
    else:
        return "I don't know."


# the constant THRESH is set to 0.6 because I wanted the response to give an answer that was close to matching other questions
THRESH = 0.6
def similar_response(data, question):
    """
    Function takes a question and splits it into each word. Then it iterates through the given list and for
    every element in the list it takes the element at index 0 and splits it. This makes it so that we can check
    every word in this question and compare it to the question that the user is looking for. If there is a word
    that matches the word in the question from the data it will add one to a variable score. We divide by the
    length of the question from the data and if that score is greater than 0.6 the function returns the response.
    
    Args_
        list: (list) this list has many tuples containing questions and answers
        question: (string) this question is the one that the user is looking for in the data
    Returns_
        The function returns an answer from a tuple if the question matches similarity from 60 percent or higher.
        This returns a string.
    """
    split_question = question.split()
    for element in data:
        score = 0
        words_in_question = element[0].split()
        for word in words_in_question:
            if word in split_question:
                score += 1
        score /= len(words_in_question)
        if score >= THRESH:
            return element[1]


def better_similar_response(data, question):
    """
    Function takes a question and splits it into each word. Then it iterates through the given list and for
    every element in the list it takes the element at index 0 and splits it. This makes it so that we can check
    every word in this question and compare it to the question that the user is looking for. If there is a word
    that matches the word in the question from the data it will add one to a variable score. We divide by the
    length of the question from the data. If the score is greater than 0.6 and greater than the variable max
    we set best answer equal to the response at that index from the tuple, and set max equal to the score. This
    will allow for the answer to have the highest similarity score.
    
    Args_
        list: (list) this list has many tuples containing questions and answers
        question: (string) this question is the one that the user is looking for in the data
    Returns_
        The function returns an answer from a tuple if the question matches similarity from 60 percent or higher
        based on the max score. Once the program has found the highest score it will return the best_answer which
        is a string.
    """
    max_similarity = 0
    best_answer = ""
    split_question = question.split()
    for element in data:
        score = 0
        words_in_question = element[0].split()
        for word in words_in_question:
            if word in split_question:
                score += 1
        score /= len(words_in_question)
        if score >= THRESH and score >= max_similarity:
            best_answer = element[1]
            max_similarity = score
    return best_answer


def chatbot(version):
    """
    Chatbot has three versions. All versions will take in a user input and return some sort of string. If the input
    is not a question it will return "I only respond to questions!" If it is a question then the chatbot will
    return a string from the quotes that best matches the question. If there is no match then the chatbot will
    respond with "I don't know." for version 0. Version 1 and 2 will respond with the closest match to that
    question. Once the user is done talking to chatbot they can type "bye" and the program will close.

    Args_
        version: (int) this decides what version of chatbot will be used
    """
    if version == 0:
        print("Welcome!")
        user_quest = input("Ask me anything. When your done, just type 'bye'\n")
        while user_quest != 'bye':
            if not is_question(user_quest):
                print("I only respond to questions!")
                user_quest = input()
            elif is_question(user_quest):
                response = respond(quotes, user_quest)
                print(response)
                user_quest = input()
    if version == 1:
        print("Welcome to version 1!")
        user_quest = input("Ask me anything. When your done, just type 'bye'\n")
        while user_quest != 'bye':
            if not is_question(user_quest):
                print("I only respond to questions!")
                user_quest = input()
            elif is_question(user_quest):
                response = similar_response(quotes, user_quest)
                print(response)
                user_quest = input()
    if version == 2:
        print("Welcome to version 2!")
        user_quest = input("Ask me anything. When your done, just type 'bye'\n")
        while user_quest != 'bye':
            if not is_question(user_quest):
                print("I only respond to questions!")
                user_quest = input()
            elif is_question(user_quest):
                response = better_similar_response(quotes, user_quest)
                print(response)
                user_quest = input()
