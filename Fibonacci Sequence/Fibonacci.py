
def fibonacci_loop(num):
    F0 = 0
    F1 = 1
    if num == 0:
        return F0
    elif num == 1:
        return F1
    else:
        FLast = 0
        FNow = 1
        for i in range(num-1):
            answer = FLast + FNow
            FLast = FNow
            FNow = answer
        return FNow

def fibonacci_rec(num):
    F0 = 0
    F1 = 1
    if num == 0:
        return F0
    elif num == 1:
        return F1
    else:
        return fibonacci_rec(num-1) + fibonacci_rec(num-2)
    

def main():
    while True:
        num = input("Please enter a integer (>=0) or -1 to exit: ")
        try:
            num = int(num)
        except:
            print("Invalid input!\nPlease enter again!")
        if num == -1:
            exit()
        method = input("Please choose a method, l for loop and r for recursive: ")
        if method == "l":
            print("The " + str(num) + "th Fibonacci number is " + str(fibonacci_loop(num)))
        elif method == "r":
            print("The " + str(num) + "th Fibonacci number is " + str(fibonacci_rec(num)))
        else:
            print("Invalid method!\nPlease enter again!")

if __name__ == "__main__":
    main()