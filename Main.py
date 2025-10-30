from faker import Faker
import os

os.system('cls')
# Create an instance of the Faker generator
fake = Faker()

# Save a generated password to file
def save_password(password):

    save_choice = input("Do you want to save this password? (y/n): ").strip().lower()
    if save_choice == 'y':

        # ask what the password is for
        password_label = input("Enter a description for this password (ex: 'for Gmail' or 'for Discord'): ")

       # Save task to file

        data_to_write = f"{password_label} | {password}\n"

        # open the file and add the new line
        with open("passwords.txt", "a") as file:
            file.write(data_to_write)
        print("Password saved to passwords.txt!")
    else:
        print("Password not saved.")

#Menu
print("Welcome to the Password Generator!")
while True:
    print("\nWhat kind of password do you want to have?")
    print("\n1. Basic Secure password")
    print("\n2. Custom length password")
    print("\n3. No special characters (letters + numbers only)")
    print("\n4. Lowercase only (no digits or uppercase)")
    print("\n5. Strong custom password (18 characters, includes everything)")
    print("\n6. Quit")


    choice = input("\nEnter your choice (1-6): ")


    if choice == "1":
        pw = fake.password()
        print("\nYour password:", pw)
        save_password(pw)
       
    elif choice == "2":
            
    # Checks for number
        pw_length = int(input("Enter your password length: "))
        pw = fake.password(length=pw_length)
        print("\nYour password:", pw)
        save_password(pw)  
        
    elif choice == "3":
        pw = fake.password(special_chars=False)
        print("\nYour password:", pw)
        save_password(pw)

    elif choice == "4":
        pw = fake.password(digits=False, upper_case=False)
        print("\nYour password:", pw)
        save_password(pw)

    elif choice == "5":
        pw = fake.password(length=18, special_chars=True)
        print("\nYour password:", pw)
        save_password(pw)

    elif choice == "6":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice! Pick a number from 1 to 6.")
        input("Press Enter to continue...")
        continue


    again = input("\nDo you want to make another password? (y/n): ").strip().lower()
    if again != "y":
        print("\nGoodbye!")
        break