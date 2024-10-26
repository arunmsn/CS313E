#expected output:
#[3, 5, 3, 6, 3, 9]
#[14, 5, 3, 6, 14, 9]
def main():
    """Main function"""
    edit_list = [14, 5, 3, 6, 14, 9]
    new_list = new_value_int_list(edit_list, 14, 3)
    print(new_list)
    print(edit_list)

def new_value_int_list(edit_list, val_search, val_replace):
    """Progam to replace the element searching for with the element needed to be replaced by"""
    # new_list = list -- this is the problem, as new_list is being set to list,
    #                    and anything that effects new_list affects list
    new_list = []
    for element in edit_list:
        new_list.append(element)
    for i, val in enumerate(new_list):
        if val == val_search:
            new_list[i] = val_replace

    return new_list

main()
