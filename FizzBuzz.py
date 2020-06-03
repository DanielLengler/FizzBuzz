multiples_list = [[3, "Fizz"], [8, "Buzz"]]


def game():
    for i in range(1, int(play_until) + 1):
        output = ""

        for multiple in multiples_list:
            if i % multiple[0] == 0:
                output += multiple[1]

        if output == "":
            output += str(i)

        print(output)


play_until = input("How many rounds do you want to play?")
game()
