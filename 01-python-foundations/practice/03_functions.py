# create a function to take input from user to check environment
# if the en is prod, make the user not deploy on friday

def check_env(env):
    if env == "dev" or env == "staging":
        print("I will deploy on friday")
    elif env == "prod":
        print("I can't deploy on friday")   
    else:
        print("safe to deploy any day")

# env = input("Enter the env: ")
# check_env(env)