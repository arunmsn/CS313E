lines = [[None] * 3 for i in range(3)]

for i in range(3):
    lines[i] = input().split()

TOTAL_SALES = 0
COUNT = 1

for line in lines:
    print(line)

for line in lines:
    if len(line) != 0:
        if len(lines[1]) != 0:
            print(f"Order #{COUNT}")
        area = int(line[1]) * int(line[2])
        carpet_cost = area * 1.2 * float(line[0])
        labor_cost = area * 0.75
        tax_cost = (carpet_cost + labor_cost) * 0.07
        total_cost = carpet_cost + labor_cost + tax_cost

        print("Room:", area, "sq ft")
        print(f"Carpet: ${carpet_cost:.2f}")
        print(f"Labor: ${labor_cost:.2f}")
        print(f"Tax: ${tax_cost:.2f}")
        print(f"Cost: ${total_cost:.2f}")
        print()
        if len(lines[1]) != 0:
            TOTAL_SALES += total_cost
            COUNT += 1
    else:
        break
if len(lines[1]) != 0:
    print(f"Total Sales: ${TOTAL_SALES:.2f}")