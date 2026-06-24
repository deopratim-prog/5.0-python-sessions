# Second Largest Element
def second_largest(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second


# Third Largest Element
def third_largest(arr):
    first = second = third = float('-inf')

    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

    return third


# Reverse an Array
def reverse_array(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# Reverse Array in Groups
def reverse_in_groups(arr, k):
    for i in range(0, len(arr), k):
        arr[i:i + k] = reversed(arr[i:i + k])

    return arr


# Rotate Array
def rotate_array(arr, k):
    n = len(arr)
    k %= n

    return arr[-k:] + arr[:-k]


# Three Great Candidates
def max_product(arr):
    arr.sort()

    return max(
        arr[-1] * arr[-2] * arr[-3],
        arr[0] * arr[1] * arr[-1]
    )


# Max Consecutive Ones
def max_consecutive_ones(arr):
    count = ans = 0

    for num in arr:
        if num == 1:
            count += 1
            ans = max(ans, count)
        else:
            count = 0

    return ans


# Move All Zeroes To End
def move_zeroes(arr):
    pos = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1

    return arr


# Wave Array
def wave_array(arr):
    arr.sort()

    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


# Plus One
def plus_one(digits):
    num = int("".join(map(str, digits)))
    num += 1

    return list(map(int, str(num)))


# Stock Buy and Sell – One Transaction
def max_profit(prices):
    min_price = float('inf')
    profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


# Stock Buy and Sell – Multiple Transactions
def max_profit_multiple(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


# Remove Duplicates from Sorted Array
def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1


# Alternate Positive Negative
def alternate_pos_neg(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]

    result = []
    i = j = 0

    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1

    result.extend(pos[i:])
    result.extend(neg[j:])

    return result


# Array Leaders
def leaders(arr):
    result = []
    max_right = arr[-1]

    result.append(max_right)

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            result.append(arr[i])

    return result[::-1]


# Missing and Repeating in Array
def find_missing_repeating(arr):
    n = len(arr)
    seen = set()
    repeating = -1

    for num in arr:
        if num in seen:
            repeating = num
        seen.add(num)

    missing = next(i for i in range(1, n + 1) if i not in seen)

    return missing, repeating


# Missing Ranges of Numbers
def missing_ranges(nums, lower, upper):
    result = []
    prev = lower - 1

    for i in range(len(nums) + 1):
        curr = nums[i] if i < len(nums) else upper + 1

        if curr - prev >= 2:
            result.append([prev + 1, curr - 1])

        prev = curr

    return result


# Sum of all Subarrays
def sum_of_subarrays(arr):
    n = len(arr)
    total = 0

    for i in range(n):
        total += arr[i] * (i + 1) * (n - i)

    return total