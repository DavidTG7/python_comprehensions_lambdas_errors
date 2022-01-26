# Program to print the saquare of numbers from 1 to 100:

def run():
    square_nums = []

    for num in range(1, 101):
        num *= num
        if num % 3 != 0:
            square_nums.append(num)

    print(square_nums)

    # Doing the same but now using list comprehensions:
    squares_comp = [num1**2 for num1 in range(1, 101) if num1 %3 != 0]

    print(squares_comp)


if __name__=='__main__':
    run()