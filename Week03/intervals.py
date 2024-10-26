"""
    File: intervals.py
    Description:
        Input: tuples_list is an unsorted list of tuples denoting intervals
        Output: a list of merged tuples sorted by the lower number of the interval

    Student Name: Arun Mahadevan Sathia Narayanan
    Student UT EID: as235872

    Partner Name: N/A
    Partner UT EID: N/A

    Course Name: CS 313E
    Unique Number: 50184 (Arun)
    Date Created: 09/06/2024
    Date Last Modified: 09/07/2024
"""
import sys

def merge_logic(tuples_list):
    """Method to determine the logic of merging"""
    for i, tuple_item in enumerate(tuples_list):
        if tuple_item is not None:
            for k in range(i+1, len(tuples_list)):
                if tuples_list[k] is not None:
                    if (tuples_list[i][0] <= tuples_list[k][0] and
                        tuples_list[i][1] >= tuples_list[k][0] and
                        tuples_list[k][1] <= tuples_list[i][1]):
                        tuples_list[k] = None
                    elif (tuples_list[i][0] <= tuples_list[k][0] and
                          tuples_list[i][1] >= tuples_list[k][0] and
                          tuples_list[k][1] >= tuples_list[i][1]):
                        tuples_list[i] = (tuples_list[i][0], tuples_list[k][1])
                        tuples_list[k] = None
                    elif (tuples_list[i][0] >= tuples_list[k][0] and
                          tuples_list[i][1] >= tuples_list[k][0] and
                          tuples_list[k][1] <= tuples_list[i][1] and
                          tuples_list[i][0] <= tuples_list[k][1]):
                        tuples_list[i] = (tuples_list[k][0], tuples_list[i][1])
                        tuples_list[k] = None
                    elif (tuples_list[i][0] >= tuples_list[k][0] and
                          tuples_list[i][1] >= tuples_list[k][0] and
                        tuples_list[k][1] >= tuples_list[i][1]):
                        tuples_list[i] = tuples_list[k]
                        tuples_list[k] = None

def merge_tuples (tuples_list):
    """Function taking in a list of tuples and merging them"""
    ranges = []
    for item, tuple_item in enumerate(tuples_list):
        if tuple_item is not None:
            ranges.append(tuples_list[item])
    sorted_range = sorted(ranges)
    tuples_list = []
    for item in sorted_range:
        tuples_list.append(item)
    merge_logic(tuples_list)
    unsorted_ranges = []
    for i, tuple_item in enumerate(tuples_list):
        if tuple_item is not None:
            unsorted_ranges.append(tuples_list[i])
    return sorted(unsorted_ranges)

def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """
    ordered_by_range = []
    to_be_ordered = {}
    for i, tuple_item in enumerate(tuples_list):
        key = tuple_item[1] - tuple_item[0]
        if key not in to_be_ordered:
            to_be_ordered[key] = []
        to_be_ordered[key].append(tuples_list[i])
    ordered = sorted(to_be_ordered)
    for j in ordered:
        ordered_by_range.append(to_be_ordered[j])
    output_array = [item for sublist in ordered_by_range for item in sublist]
    return output_array

def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    # input_file = open("intervals.in")
    # num_intervals = int(input_file.readline())
    sys.stdin.readline()
    tup_list = []
    tup_list = sys.stdin.readlines()
    # for _ in range(num_intervals):
    #     tup_list.append(input_file.readline())

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
