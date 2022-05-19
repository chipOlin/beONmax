import csv
from typing import Iterable

from believe.game_status import GameStatus


class Game:
    def __init__(self, allowed_misses: int = 2):
        self.__allowed_misses = allowed_misses
        self.__tries_counter = 0
        self.__game_status = GameStatus.NOT_STARTED
        # self.__questions_dict = {}

    def generate_questions(self, filename: str) -> Iterable[dict]:
        # filename = 'data/Questions.csv'
        with open(filename, newline='', encoding='utf8') as csvfile:
            questions = csv.reader(csvfile, delimiter=';')
            for i, row in enumerate(questions):
                questions[i] = row
        return questions
