def run():
    num_dict = {}
    
    for value in range(1, 101):
        if value % 3 != 0:
            num_dict[value] = value ** 3
    
    print(num_dict)

    # Using dictionary comprehensions:

    dict_comp = {num: num **3 for num in range(1, 101) if num % 3 != 0}

    print(dict_comp)


if __name__=='__main__':
    run()