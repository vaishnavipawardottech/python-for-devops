from functions import check_env

# for loop
for i in range(5):
    env = input("Enter the env: ")
    check_env(env)

# while loop
num = 1
while num < 5:
    print("yes the value is: ", num)
    num = num + 1