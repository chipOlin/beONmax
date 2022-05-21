from believe.game import Game
from believe.game_result import GameResult
from believe.game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f"Questions asked:{result.questions_passed}. Mistakes made:{result.mistakes_made}")
    print("You won!" if result.won else "You lost!")


game = Game(r'data\Questions.csv', end_of_game_handler, allowed_mistakes=3)

while game.game_status == GameStatus.IN_PROGRESS:
    q = game.get_next_question()
    print("Do you believe in the nex statement or question? 'y' or 'n'")
    print(q.text)

    answer = input() == "y"

    if q.is_true == answer:
        print("Good job!")
    else:
        print("Oops, actually you re mistaken! Here is the explanation:")
        print(q.explanation)

    game.give_answer(answer)
