from faker import Faker


# Create an instance of the Faker generator
fake = Faker()

# Menu
print("Welcome to the Password Generator!")
print()

while True:
    print("What kind of Password Do you want to have?")
    print()
    print()

    print("1. Basic Secure password")
    print()
    print("2. Costom length password")
    print()
    print("3. No special characters (letters + numbers only)")
    print()
    print("4. Lowercase only (no digits or uppercase)")
    print()
    print("5. Strong costom password (18 characters, includes everythng)")
    print()
    print("6. Quit")
    print()
    print()
    choice = input("Enter your choice (1-6):")

    if choice == "1":
        pw = fake.password()
        print("Your password:" , pw)

    elif choice == "2":
      user_input = input("Enter password length (minimum 4):").strip()
      
      #checks if it is a number
    pw_length = int(user_input)
    if pw_length > 4:
       print("you can't choose a number less than 4")
    pw = fake.password(length = pw_length)
    print("your password (" + str(pw_length) + "characters):" , pw)
    