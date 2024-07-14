import json
import random

class Player():
    def __init__(self,name,points = 0):
        self.name = name
        self.points = points
def enrollment():
    players = []
    number_players = int(input("How many players are you? (2/3): "))
    for i in range (number_players):
        name = input(f"what is your name [actor {i+1}]?")
        player = Player(name)
        players.append(player)
    return players

def json_to_python(level):
    with open(r'C:\Users\beni4\Desktop\new_project\Michael_Project\Michael.json', 'r') as file:
        data = json.load(file)
    weak   = data[0]
    medium = data[1]
    strong = data[2]
    if level == 1:
        return weak
    if level == 2:
        return medium
    if level == 3:
        return strong

def levels(level = 1):
    questions = json_to_python(level)
    random.shuffle(questions)
    return questions

def the_winner(players):
    pints = 0
    for result in players:
        print(result.name, ":", result.points)
        if result.points > pints:
            pints = result.points
            winner = result.name
    print(f"The winner is {winner}!!!!")

def randomly(players):
    number_level = 1
    current_player = 0
    while number_level <= 3:
        questions = levels(number_level)
        print(f"level -{number_level}")
        number_question = 1
        while number_question <= len(questions):
            for question, answers in questions[number_question-1].items():
                print(f"Question {number_question}: {question}")
                random.shuffle(answers)
                print("Answers:")
                number_answers = 1
                for answer,point in answers:
                    print(f"{number_answers} - {answer}")
                    number_answers += 1
                comment = int(input(f"{players[current_player].name}, enter the correct number of answer: "))
                players[current_player].points += answers[comment - 1][1]
                if answers[comment - 1][1] == 1:
                    print("Correct!")
                    number_question += 1
                else:
                    print("Incorrect.")
                current_player = (current_player + 1) % len(players)
        number_level += 1
    the_winner(players)
def main():
    players = enrollment()
    randomly(players)
main()









