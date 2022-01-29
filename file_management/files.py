def read():
    numbers = []
    with open("./files_dir/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["David", "Mario", "Pedro", "Arturo", "Darío"]
    with open("./files_dir/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()

if __name__ == '__main__':
    run()