import random
ROCK = '🤘'
PAPER = '📝'
SCISSORS = '✂️'
RPS_MOVES = [ROCK, PAPER, SCISSORS]

GAME_RULES = {
    ROCK: [PAPER, ROCK, SCISSORS],
    PAPER: [SCISSORS, PAPER, ROCK],
    SCISSORS: [ROCK, SCISSORS, PAPER]
}


def simulate_game(user_choice):
    cpu_choice = random.choice(RPS_MOVES)

    if cpu_choice == GAME_RULES[user_choice][0]:
        return 'LOSS', cpu_choice
    elif cpu_choice == GAME_RULES[user_choice][1]:
        return 'DRAW', cpu_choice
    else:
        return 'WIN', cpu_choice


