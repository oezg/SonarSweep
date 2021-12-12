with open("day1_input") as inp:
    nums = inp.readlines()
nums = [int(num.rstrip()) for num in nums]
increased = 0
for i, num in enumerate(nums[3:]):
    if num > nums[i]:
        increased +=1
print(increased)
        
    