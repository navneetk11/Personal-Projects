def get_float_input(prompt, min_value, max_value):  # define get_float_input fuction to get float
    while True:
        answer = float(input(prompt))
        if min_value <= answer <= max_value:
            break
    return answer


def get_int_input(prompt, min_value, max_value):  # define  get_int_input fuction  to get integer
    while True:
        answer = int(input(prompt))
        if min_value <= answer <= max_value:
            break
    return answer


def compute_return(amount: float, rate: float, years: int):  # define compute_return for amount, rate and years
    for _ in range(years):
        amount = amount + amount * rate
    return amount


def get_yes():  # define get_yes if user would like to continue
    while True:
        answer = input("Compute New investment [Y/N]? ")
        if (answer == 'Y' or answer == 'y' or answer == 'N' or answer == 'n'):
            break
    return answer


while True:
    amount1 = get_float_input("Input initial investment amount [1, 10000]? ", 1, 1000)
    rate1 = get_float_input("Annual return rate [0-1]? ", 0, 1)
    years1 = get_int_input("How many years [1-10]?", 1, 10)
    compute = compute_return(amount1, rate1, years1)

    if years1 == 1:
        print(f"Return in 1 year is: $ {compute:10.2f}")
    else:
        print(f"Return in {years1} years is: $ {compute:10.2f}")

    answer = get_yes()

    if (answer == 'n' or answer == 'N'):
        break
