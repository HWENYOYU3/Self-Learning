# x = [1, 2, 3]
# x[1] = 4
# print(x)       #[1, 4, 3] list is mutable

# friends = ["Wilson", "Ruby", "Irene", "Doreen", "Kevin"]
# friends.insert(2, "Jason")
# print(friends)  #['Wilson', 'Ruby', 'Jason', 'Irene', 'Doreen', 'Kevin']

# nums = [3, 4, 2, 5, 1]
# nums.sort()
# print(nums) #[1, 2, 3, 4, 5]


# friends = ["Wilson", "Ruby", "Irene", "Doreen", "Kevin"]
# friends.reverse()
# print(friends)  #['Kevin', 'Doreen', 'Irene', 'Ruby', 'Wilson']

# 用 slicing 來進行 List reverse,  記住 slicing 是 immutable
# friends = ["Wilson", "Ruby", "Irene", "Doreen", "Kevin"]
# friends[::-1]
# print(friends)

# nums = [1, 2, 3]
# nums.append(4)
# print(nums) #[1, 2, 3, 4]

# nums = [1, 3, 5, 2, 4, 6]
# nums.pop()
# print(nums)  #[1, 3, 5, 2, 4]
# print(nums.pop())  #4


nums = [1, 2, 3, 4]
nums2 = nums.copy()
nums2[0] = 5
print(nums)  #[1, 2, 3, 4] 
print(nums2)  #[5, 2, 3, 4]