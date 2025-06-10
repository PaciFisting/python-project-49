from brain_games.games import brain_prime
from brain_games import engine


def main():
    RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine.game_engine(RULE, brain_prime.is_it_prime)


if __name__ == "__main__":    
    main()