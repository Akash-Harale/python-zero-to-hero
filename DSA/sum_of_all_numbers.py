# Problem Statement

# Find sum of all numbers.

# Input:

# [1, 2, 3, 4]

# Output:

# 10
# Step-by-Step Thinking

# We need:

# variable to store sum
# loop through array
# add every number
# JavaScript Version
# const arr = [1,2,3,4];

# let total = 0;

# for(let num of arr){
#     total += num;
# }

# console.log(total);

# Python Version
arr = [1, 2, 3, 4]

total = 0

for num in arr:
    total += num

print(total)

# Dry Run (VERY IMPORTANT)


# total = 0

# Loop:

# num	total
# 1	     1
# 2	     3
# 3	     6
# 4	     10

# Final answer: 10