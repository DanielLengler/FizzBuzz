play_until = input("How many rounds do you want to play?")

for i in range(1, int(play_until) + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue

    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
