def swap_elements(nums: list, i: int, j: int):
    num1 = nums[i]
    nums[i] = nums[j]
    nums[j] = num1


def next_permutation(nums: list, n: int):
    j = n - 2
    while j != -1 and nums[j] >= nums[j + 1]:
        j -= 1
    if j == -1:
        return False
    k = n - 1
    while nums[j] >= nums[k]:
        k -= 1
    swap_elements(nums, j, k)
    t = j + 1
    r = n - 1
    while t < r:
        swap_elements(nums, t, r)
        t = t + 1
        r = r - 1
    return True
