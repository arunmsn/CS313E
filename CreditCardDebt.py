def read_customer_data(filename):
    """Read and return data from filename as a list of lists (name, state, debt)"""
    names = []
    states = []
    debts = []

    with open(filename) as f:
        rows = f.readlines()
    for row in rows:
        row = row.split(',')
        names.append(row[0])
        states.append(row[1])
        debts.append(float(row[2].strip()))
    return names, states, debts

# Main portion of the program
if __name__ == '__main__':
    # number of rows to consider
    num_customers = int(input())

    names, states, debts = read_customer_data("CustomerData.csv")

    # Type your code here.
    debt_limit = int(input())
    search_phrase = input()
    state_abbr = input()

    # to find the customer with the highest debt
    HIGHEST_DEBT = 0
    NAME_I = 0
    for i in range(num_customers):
        if debts[i] > HIGHEST_DEBT:
            HIGHEST_DEBT = debts[i]
            NAME_I = i

    # to find the number of customers starting with a specific sequence of letters
    COUNT = 0
    for name in names[0:num_customers]:
        if name.startswith(search_phrase):
            COUNT += 1

    # to find the number of customers who are past the debt limit and those debt-free
    PAST_DEBT_LIMIT_COUNT = 0
    for debt in debts[0:num_customers]:
        if debt > debt_limit:
            PAST_DEBT_LIMIT_COUNT += 1

    DEBT_FREE_COUNT = 0
    for debt in debts[0:num_customers]:
        if debt == 0:
            DEBT_FREE_COUNT += 1

    # to repeat the steps for the country for a specific state
    STATE_COUNT = 0
    for state in states[0:num_customers]:
        if state == state_abbr:
            STATE_COUNT += 1

    STATE_HIGHEST_DEBT = 0
    STATE_NAME_I = 0
    for i in range(num_customers):
        if states[i] == state_abbr:
            if debts[i] > STATE_HIGHEST_DEBT:
                STATE_HIGHEST_DEBT = debts[i]
                STATE_NAME_I = i

    STATE_NAME_COUNT = 0
    for i in range(num_customers):
        if states[i] == state_abbr:
            if names[i].startswith(search_phrase):
                STATE_NAME_COUNT += 1

    STATE_PAST_DEBT_LIMIT_COUNT = 0
    STATE_DEBT_FREE_COUNT = 0
    for i in range(num_customers):
        if states[i] == state_abbr:
            if debts[i] > debt_limit:
                STATE_PAST_DEBT_LIMIT_COUNT += 1
            elif debts[i] == 0:
                STATE_DEBT_FREE_COUNT += 1

    print("U.S. Report")
    print(f"Customers: {num_customers}")
    print(f"Highest debt: {names[NAME_I]}")
    print(f"Customer names that start with \"{search_phrase}\": {COUNT}")
    print(f"Customers with debt over ${debt_limit}: {PAST_DEBT_LIMIT_COUNT}")
    print(f"Customers debt free: {DEBT_FREE_COUNT}")
    print()
    print(f"{state_abbr} Report")
    print(f"Customers: {STATE_COUNT}")
    print(f"Highest debt: {names[STATE_NAME_I]}")
    print(f"Customer names that start with \"{search_phrase}\": {STATE_NAME_COUNT}")
    print(f"Customers with debt over ${debt_limit}: {STATE_PAST_DEBT_LIMIT_COUNT}")
    print(f"Customers debt free: {STATE_DEBT_FREE_COUNT}")
