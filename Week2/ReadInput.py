import sys

def main():
    readvalues = sys.stdin.read()
    #print(readvalues)
    
    lines = readvalues.split("\n")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()