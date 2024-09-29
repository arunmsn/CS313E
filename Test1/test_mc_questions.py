def animal_behavior(animal: str, steps: int, mood: str) -> bool:
    # if animal = dog:
    #   if steps < 10:
    #       EXPLORE unless mood = TIRED
    # if animal = cat:
    #   if steps > 15:
    #       STOP (regardless of mood)
    #   else:
    #       mood = CURIOUS, continue EXPLORING
    # if ANY OTHER ANIMAL:
    #   EXPLORE only if mood = CURIOUS and steps < 12
    #
    # function returns TRUE if animal EXPLORES, otherwise FALSE
    #
    if animal == "dog":
        return steps < 10 and mood != 'tired'
    elif animal == "cat":
        return steps <= 15 and mood == 'curious'
    else:
        return steps < 12 and mood == 'curious'


"""
data =      [4, 'hello', 15, 'world', 8, 'abcd', 7]
output =    [8, 'HELLO', 14, 'WORLD', 16, 'DCBA', 6]
actual =    [3, 'OLH', 45, 'DRW', 7, 'ABDC', 21]

mystery_function([-1, 0, 1, 2, -1, -4, 9, 12, -12, -3, -6])
nums.sort() = [-12, -6, -4, -3, -1, -1, 0, 1, 2, 9, 12]

"""

def mystery_function(nums):
    nums.sort()
    res = []
    
    for i, n in enumerate(nums):
        if n > 0:
            break
        if i > 0 and n == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = n + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
        print(res)
    return res

# mystery_function([-1, 0, 1, 2, -1, -4, 9, 12, -12, -3, -6])

inventory = {'apple': 5, 'orange': 7}
print(inventory.get('banana'))
print(inventory.get('banana', 0))
print(inventory)
