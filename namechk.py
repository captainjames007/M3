# Your name
# The date
print("Hello World")

# Prompt the user to enter their name
user_name = input("Please enter your name: ").strip().lower()  # Normalize input by stripping spaces and converting to lowercase

# Check user name and grant access accordingly
if user_name == "james":
    print("Access granted")  # Grant access for James
elif user_name == "ben":
    print("Access granted")  # Grant access for Ben
else:
    print("YOU ARE NOT AUTHORIZED")  # Deny access for any other name