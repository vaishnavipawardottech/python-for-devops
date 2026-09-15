# if my current env is dev or staging I will deploy on friday
# but if the env id prod then dont deploy on friday

env = input("Enter the env: ")

if env == "dev" or env == "staging":
    print("I will deploy on friday")
elif env == "prod":
    print("I can't deploy on friday")
else:
    print("safe to deploy any day")
    