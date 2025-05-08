import random
four_uniform_randoms = [random.random() for _ in range(4)]

print(four_uniform_randoms)

# Pseudorandoms
random.seed(10) # set the seed to 10
print(random.random()) # 0.57140259469
random.seed(10) # reset the seed to 10
print(random.random()) # 0.57140259469 again


print(random.randrange(10)) # choose randomly from range(10) = [0, 1, ..., 9]
print(random.randrange(3, 6)) # choose randomly from range(3, 6) = [3, 4, 5]


up_to_ten = range(10)
random.shuffle(up_to_ten)
print(up_to_ten)

#choose a sample of elements without replacement 
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) # [16, 36, 10, 6, 25, 9]

#sample of elements with replacement
four_with_replacement = [random.choice(range(10))
 for _ in range(4)]
# [9, 4, 4, 2]
