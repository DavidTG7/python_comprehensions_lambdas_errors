def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    user_num = int(input("Write a number: "))
    print(divisors(user_num))



if __name__=='__main__':
    run()