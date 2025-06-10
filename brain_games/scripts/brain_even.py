from brain_games.games import brain_even
from brain_games import engine

def main():
    RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.game_engine(RULE, brain_even.is_it_even)


if __name__ == "__main__":    
    main()