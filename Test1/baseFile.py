"""just the base file"""
valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ."

def create_blank_grid(length, width):
    """creates a blank grid"""
    grid = []
    for i in range(length):
        grid.append([])
        for _ in range(width):
            grid[i].append(0)

    return grid

def print_grid(grid):
    """prints the grid out"""
    printed_grid = create_blank_grid(len(grid), len(grid[0]))

    maxLength = [-1] * len(grid)

    for j in range (len(grid[0])):
        for i in range (len(grid)):
            printed_grid[i][j] = (str(grid[i][j]) + " ")
            if len(printed_grid[i][j]) > maxLength[j]:
                maxLength[j] = len(printed_grid[i][j])

    for i in range (len(printed_grid)):
        row = ""
        for j in range (len(printed_grid[0])): 
            row += (printed_grid[i][j] + " " * (maxLength[j] - len(printed_grid[i][j]) + 1))
        print(row)


def create_key(row, col):
    key = create_blank_grid(8,8)
    valid_chars_list = list(valid_chars)
    count = 0
    for c in range(8):
        if c % 2 == 0:
            for r in range(8):
                key[r][c] = valid_chars_list[count]
                count += 1
        else:
            for r in range(8):
                key[7-r][c] = valid_chars_list[count]
                count += 1

    return key

def encrypt(phrase, grid):
    encrypted = ""
    for char in phrase:
        if char in valid_chars:
            for r in range(8):
                for c in range(8):
                    if grid[r][c] == char:
                        encrypted += valid_chars[(r * 8 + c) % len(valid_chars)]
                        break
                else:
                    continue
                break
        else:
            encrypted += char
    return encrypted

def decrypt(phrase, grid):
    decrypted = ""
    for char in phrase:
        if char in valid_chars:
            index = valid_chars.index(char)
            decrypted += grid[index // 8][index % 8]
        else:
            decrypted += char
    return decrypted

def main():
    while True:
        try:
            mode = input().strip()
            row = int(input())
            col = int(input())
            phrase = input().strip()

            grid = create_key(row, col)

            # Uncomment the next line to print the grid for debugging
            # print_grid(grid)

            if mode == "encryption":
                result = encrypt(phrase, grid)
            elif mode == "decryption":
                result = decrypt(phrase, grid)
            else:
                print(f"Invalid mode: {mode}")
                continue

            print(result)

        except EOFError:
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
    # print_grid(create_key(6,1))