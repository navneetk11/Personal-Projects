import time
from random import randint


def get_int_input(prompt, min_value,
                  max_value):  # returns integer,define get_int_input() to get a number between 2-20.
    while True:
        answer = int(input(prompt))
        if min_value <= answer <= max_value:
            break
    return answer


def get_yes(prompt):  # define get_yes()to ask if the user wants to randomize or not.
    answer = (input(prompt))
    if answer.upper().strip() == "Y":
        return True
    elif answer.upper().strip() == "N":
        return False
    else:
        answer = (input(prompt))


def draw_owl(position, randomize=False):
    eye1 = '{o,o}'
    eye2 = '{-,o}'
    eye3 = '{o,-}'
    body = '/)_) '
    feet = ' " " '
    if randomize:  # if your random number is 1, print eye1; if it is 2, print eye2 , if it is 3, print eye3
        random = randint(1, 3)
        if random == 1:
            eye = eye1
        elif random == 2:
            eye = eye2
        elif random == 3:
            eye = eye3
    else:  # If randomize is False, print eye1 only.
        eye == eye1
    print(
        " " * position + eye)  # The position variable will be the number of spaces  need to print before each variable
    print(" " * position + body)
    print(" " * position + feet)


N = get_int_input("How many times to move [2-20]? ", 2, 20)
T = get_int_input("How long to delay [1-1000ms] ? ", 1, 1000)
r = get_yes("Randomize [Y/N]? ")

for i in range(N):
    draw_owl(i, r)
    time.sleep(T / 1000)  # sleep() function will cause your output to pause for 1/T seconds

