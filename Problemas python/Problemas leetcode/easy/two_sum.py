enter = input()
target = int(input("target = "))
nums = [ int(number)for number in enter.strip("[]").split(",")]
for numero in nums:
    for num in nums:
        if numero+num == target:
           index_1 = nums.index(numero)
           index_2 = nums.index(num)
    break
print(f"[{index_1},{index_2}]")