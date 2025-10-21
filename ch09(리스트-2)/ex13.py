def print_list(li):
    for row in range(len(li)):
        for col in range(len(li[row])):
            print(li[row][col], end=" ")
        print()

def init(li):
    for row in range(len(li)):
        for col in range(len(li[row])):
            if (row + col) % 2 == 0:
                li[row][col] = 1

if __name__ == "__main__":
    table = []
    for row in range(10):
        table += [[0] * 10]
    init(table)
    print_list(table)