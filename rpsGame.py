from random import seed
import random

def decision_function( move1: str, m2: str) -> int:
    m1: str = move1.upper()
    if m1 == m2:
        return 0
    if m1 == 'R' and m2 =='P':
        return -1
    elif m1 == 'R' and m2 == 'S':
        return 1
    elif m1 == 'P' and m2 == 'R':
        return 1
    elif m1 == 'P' and m2 == 'S':
        return -1
    elif m1 == 'S' and m2 == 'R':
        return -1
    else:
        return 1


def rpsFunction( move: str) -> (int,str):
    seed(random.randint(1,200))
    comp_move: int = random.randint(1,3)
    comp_move_str: str = ""
    if comp_move % 3 == 0:
        comp_move_str = 'R'
    elif comp_move % 3 == 1:
        comp_move_str = 'P'
    else:
        comp_move_str = 'S'
    return (decision_function( move, comp_move_str), comp_move_str)


if __name__=='__main__':
    ct: int = 0
    score: int = 0
    play_again: bool = True
    print("Let's play rock, paper, scissors, shoot!")
    print("Choose how many rounds to play:\t")
    games: int = int(input())
    while ct < games:
        print("Choose your move: [R/P/S]\t")
        move: str = input()
        result, comp_move = rpsFunction(move)
        if result > 0:
            score += 1
            print(f"You win! {move} beats {comp_move}.")
        elif result == 0:
            print("Tie.")
        else:
            print(f"You lost! {comp_move} beats {move}.")
        ct += 1
    print(f"Good game! You won {score} out of {games} games.")