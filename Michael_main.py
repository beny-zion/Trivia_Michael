from Michael_Functions import *
import argparse
def main():
    parser = argparse.ArgumentParser(description='Quiz game with multiple levels and players.')
    parser.add_argument('--players', type=int, choices=[2, 3], required=True, help='Number of players (2 or 3)')
    args = parser.parse_args()
    players = enrollment(args.players)
    randomly(players)

if __name__ == "__main__":
    main()
