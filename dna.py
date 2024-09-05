"""
DNA
"""


def longest_subsequence(string_1, string_2):
    """ADD YOUR CODE HERE """



def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

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
