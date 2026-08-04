enter,target = input()
nums = [ int(number)for number in enter.strip("[]").split(",")]
for i in range(nums):
    for k in range(nums):
        