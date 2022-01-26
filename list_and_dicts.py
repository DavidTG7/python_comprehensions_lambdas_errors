# Nested lists and dictionaries:

def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "David", "lastname": "Torres"}
    
    super_list = [
        {"firstname": "David", "lastname": "Torres"},
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Diego", "lastname": "Morillo"},
        {"firstname": "Sarah", "lastname": "Torres"},
        {"firstname": "Emilia", "lastname": "Morillo"}

    ]

    super_dict = {
        "natural_nums": [1, 2, 4, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for dicts in super_list:
        print(dicts["firstname"], dicts["lastname"])


if __name__=='__main__':
    run()