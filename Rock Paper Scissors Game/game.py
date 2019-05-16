from random import randint

def check_result(player, computer):
    # 1 = rock, 2 = paper, 3 = scissors
    if player == 1:
        if computer == 1:
            print("Tie!")
            print("Player : rock / Computer : rock")
            return 0
        elif computer == 2:
            print("Computer Win!")
            print("Player : rock / Computer : paper")
            return 2
        elif computer == 3:
            print("Player Win!")
            print("Player : rock / Computer : scissors")
            return 1
    elif player == 2:
        if computer == 1:
            print("Player Win!")
            print("Player : paper / Computer : rock")
            return 1
        elif computer == 2:
            print("Tie!")
            print("Player : paper / Computer : paper")
            return 0
        elif computer == 3:
            print("Computer Win!")
            print("Player : paper / Computer : scissors")
            return 2
    elif player == 3:
        if computer == 1:
            print("Computer Win!")
            print("Player : scissors / Computer : rock")
            return 2
        elif computer == 2:
            print("Player Win!")
            print("Player : scissors / Computer : paper")
            return 1
        elif computer == 3:
            print("Tie!")
            print("Player : scissors / Computer : scissors")
            return 0

def main():
    score = [0, 0]
    valid = ['1', '2', '3', '-1']
    while True:
        print("Player : {} wins / Computer : {} wins".format(score[0], score[1]))
        player = input("Please selected (1 = rock, 2 = paper, 3 = scissors, -1 = exit)\n")
        if player not in valid:
            print("Invalid input! Please enter again")
        elif player == "-1":
            exit()
        else:
            result = check_result(int(player), randint(1, 3))
            if result == 1:
                score[0] += 1
            elif result == 2:
                score[1] += 1

if __name__ == '__main__':
    main()