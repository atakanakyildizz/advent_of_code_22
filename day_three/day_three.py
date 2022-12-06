FILENAME = "day_three.txt"

def main():

    with open(FILENAME, 'r') as f:
        lines = f.readlines()

    print(lines)

    #print(lines)

if __name__ == '__main__':
    main()