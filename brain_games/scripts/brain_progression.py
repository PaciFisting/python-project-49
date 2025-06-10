from brain_games.games import brain_progression
from brain_games import engine


def main():
    RULE = 'What number is missing in the progression?'
    engine.game_engine(RULE, brain_progression.find_progression_number)


if __name__ == "__main__":    
    main()