nums = [1, 2, 3, 4, 5]
print(nums)
print(type(nums))

# adicionando numero ao final da lista
nums.append(3)
nums.append(6)

print(len(nums))

nums[3] = 100

print(nums)

# adicionando numero em qlqr lugar da lista

nums.insert(2, -200)

print(nums)

# acessando itens de tras pra frente
print(nums[-1])
print(nums[-2])