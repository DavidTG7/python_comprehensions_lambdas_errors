def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("Negative numbers are not allowed.")
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)

    return ""
    

def run():
    try:
        num = int(input("Write a number: "))
        print(divisors(num))
    except ValueError:
        print("You are just allowed to write integer numbers.")
    print("Program finished.")


if __name__=='__main__':
    run()
