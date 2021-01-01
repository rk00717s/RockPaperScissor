from random import choice

def is_win(player, opponent):
    if(player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True
    else:
        return False

def play():
    user_choice = input('Choose Rock(R), Paper(P), or Scissor(S) : ')
    user_choice = user_choice.upper()
    system_choice = choice(['R', 'P', 'S'])

    display_result = "null"
    if(user_choice == system_choice):
        display_result = "Match Draw"
    else:
        display_result = "You Won by Me" if(is_win(user_choice, system_choice)) else "You Lost by Me"

    print(display_result)
    

if __name__ == '__main__':
    play()