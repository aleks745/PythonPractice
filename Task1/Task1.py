import re

str = input("Enter your string: ")

nums = re.findall(r'\d+', str)
str = re.sub(r"\d+", "", str, flags=re.UNICODE)
nums = [int(i) for i in nums]

print(str)
if not nums:
    print("There are no numbers in your string")
else:
    print(nums)
        
str, res = str.title(), ""
for word in str.split():
    res += word[:-1] + word[-1].upper() + " "

print( "" + res)

if not nums:
    print("There are no numbers in your string")
else:
    mnum = max(nums)
    print("\nMax number in array:", mnum)

if not nums:
    print("There are no numbers in your string")
else:
    arr_c = []
    for i in range(len(nums)):
        if i !=nums.index(mnum):
            temp = nums[i]         
            stup = temp ** i
            arr_c.insert(i, stup)
    print("An array of numbers elevated to the power of their index:\n", arr_c)
