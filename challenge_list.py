''' Creat a list, using list comprehension, with the numbers from 1 to 99999
    if they are multiple of 4, 6 and 9 at the same time.
'''

def run():
    num_list = [num for num in range(1, 99999) if num % 36 == 0]                
    
    print(num_list)

if __name__=='__main__':
    run()