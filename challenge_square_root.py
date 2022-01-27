'''Create a dictionary which keys are numbers from 1 to 1000 and their 
   values will be its square root.
'''

def run():
    my_dict = {num: round(num ** 0.5, 4) for num in range(1, 1001)}
    print(my_dict)


if __name__=='__main__':
    run()