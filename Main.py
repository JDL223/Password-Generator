from faker import Faker
import os

# Create an instance of the Faker generator
fake = Faker()

def save_password(password):
    """Ask the user if they want to save the password and then save it to a file."""
    save_choice = input("Do you want to save this password? (y/n): ").strip().lower()


    if save_choice == 'y':
        # Ask what the password is for
        label = input("Enter a description for this password (ex: 'for Gmail' or 'for Discord'): ")


        # Put the label and password together
        data = f"[{label}] {password}\n"


        try:
            # Open the file and add the password to it
            with open("passwords.txt", "a", encoding="utf-8") as file:
                file.write(data)
            print(" Password saved to passwords.txt!")
        except Exception as e:
            print(f" Error saving password: {e}")
    else:
        print("Password not saved.")


    # Menu
print("Welcome to the Password Generator!")

while True:
    print("\nWhat kind of password do you want to have?")
    print("\n1. Basic Secure password")
    print("2. Custom length password")
    print("3. No special characters (letters + numbers only)")
    print("4. Lowercase only (no digits or uppercase)")
    print("5. Strong custom password (18 characters, includes everything)")
    print("6. Quit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        pw = fake.password()
        print("\nYour password:", pw)
        save_password(pw)
        
    elif choice == "2":
            
            pw_length = int(input("Enter your password length (min 4 chars): "))
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

