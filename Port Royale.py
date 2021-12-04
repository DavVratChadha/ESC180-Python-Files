#Program to give bribe to hide name at Port Royale (chech video on the course website)

shilling = 1
name = "Jack Sparrow"

if shilling >=3:
    print("Welome to Port Royale! Mr Smith.")
elif shilling >=1:
    print("Welcome to Port Royale! " + name)
else:
    print("Go away please.")

#note: the program below will not work properly because the >=3 condition will never get executed
"""

if shilling >=1:
    print("Welcome to Port Royale! " + name)
elif shilling >=3:
    print("Welome to Port Royale! Mr Smith.")
else:
    print("Go away please.")
    """