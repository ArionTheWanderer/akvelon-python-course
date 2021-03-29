import helper_functions

# просто перестановки из 4х элементов проще проверить, но и с 7, конечно, работает
# лексикографический порядок соблюден
# p.s. это не рекурсия
n = 4
nums = []
for i in range(n):
    nums.append(i)
print(nums)
while helper_functions.next_permutation(nums, n):
    print(nums)
