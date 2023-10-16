import random

def main():

    print("- Guessing Game -")
    number = random.randint(1,100)

    userinput = input("I'm thinking of a number. Make a guess (1-100): ")
    counter = 0
    while True:
        if int(userinput) < 0:
            print("Invalid input - should be within range 1-100.", end=" ")
        elif int(userinput) == number:
            counter += 1
            print(f"Congrats you got it in {counter} tries")
            break
        elif int(userinput) < number:
            counter += 1
            print("Too low!", end=" ")
        elif int(userinput) > number:
            counter += 1
            print("Too high!", end=" ")
        userinput = input("Guess again(1-100): ")
        


main()