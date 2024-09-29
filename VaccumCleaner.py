def clean(floor):
    i, j, row, col = 0, 0, len(floor), len(floor[0])
    for i in range(row):
        if i % 2 == 0:
            for j in range(col):
                if floor[i][j] == 1:
                    print_F(floor, i, j)
                    floor[i][j] = 0
                    print_F(floor, i, j)
        else:
            for j in range(col - 1, -1, -1):
                if floor[i][j] == 1:
                    print_F(floor, i, j)
                    floor[i][j] = 0
                    print_F(floor, i, j)

def print_F(floor, i, j):
    print("The floor matrix is as below:")
    for r in range(len(floor)):
        for c in range(len(floor[r])):
            print(f"{floor[r][c]}", end=" ")
        print(end='\n')

def main():
    floor = []
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    print("Enter clean status for each cell (1-dirty, 0-clean):")
    for i in range(m):
        f = list(map(int, input().split(" ")))
        floor.append(f)
    print()
    clean(floor)

if __name__ == "__main__":
    main()