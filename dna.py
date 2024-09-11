"""
DNA
"""


def longest_subsequence(string_1, string_2):
    sequence_1 = string_1.split()
    sequence_2 = string_2.split()
    print(sequence_1)
    print(sequence_2)



def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    input_file = open("dna.in")
    # number of lines
    # n_lines = int(input())
    n_lines = int(input_file.readline())
    print(n_lines)

    # for each pair
    for _ in range(0, n_lines):
        # str_1 = input()
        # str_2 = input()
        str_1 = input_file.readline()
        str_2 = input_file.readline()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
