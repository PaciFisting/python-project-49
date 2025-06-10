from brain_games.games import brain_calc
from brain_games import engine


def main():
    RULE = 'What is the result of the expression?'
    engine.game_engine(RULE, brain_calc.calculate)


if __name__ == "__main__":    
    main()