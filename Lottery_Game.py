import random


def random_set():  # computes a set of 5 random numbers between 1-20.
    s = set()
    while len(s) < 5:
        s.add(random.randint(1, 20))
    return s


def print_set(s, prompt=''):
    print(prompt, end="")
    print(*s, sep=' ')


YN = "Y"
while YN == "Y":
    numbers = input("Enter 5 numbers between 1-20: ")
    if len(numbers) != 5 or len(set(numbers)) != 5:  # If the user does not input five (5) unique numbers (i.e., less than 5, more than 5, or repeating numbers), keep asking for input.
        continue
    user_set = set(int(x) for x in numbers)

    computer_set = random_set()
    print_set(computer_set, "Computer's numbers: ")
    matches = user_set.intersection(computer_set)  # compute if there is matches with intersection

    if not matches:
        print("NO MATCHES!")
    else:
        print(f"{len(matches)} matches found:", end=" ")  # if match found
        print_set(matches)
        if len(matches) == 5:
            print("YOU WIN!")

    YN = input("Try again [Y/N]? ").upper()