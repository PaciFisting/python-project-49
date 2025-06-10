from brain_games.games import brain_gcd
from brain_games import engine


def main():
    RULE = 'Find the greatest common divisor of given numbers.'
    engine.game_engine(RULE, brain_gcd.find_gcd)


if __name__ == "__main__":    
    main()