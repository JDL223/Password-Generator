from faker import Faker
import os
import time
import random


# Clear console
os.system('cls' if os.name == 'nt' else 'clear')


# Create an instance of the Faker generator
fake = Faker()


# Fun loading animation
def loading_animation(message="Generating password"):
    print(f"\n{message}", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")


# Save a generated password to file
def save_password(password):
    save_choice = input("💾 Do you want to save this password? (y/n): ").strip().lower()
    if save_choice == 'y':
        password_label = input("📝 Enter a description for this password (ex: 'for Gmail' or 'for Discord'): ")
        data_to_write = f"{password_label} | {password}\n"
        with open("passwords.txt", "a") as file:
            file.write(data_to_write)
        print("✅ Password saved to passwords.txt!")
    else:
        print("❌ Password not saved.")


# Random motivational messages
def fun_message():
    messages = [
        "🚀 You're a password master now!",
        "🔥 Strong password, strong security!",
        "✨ Keep your secrets safe!",
        "💡 Remember: unique passwords are your superpower!"
    ]
    print(random.choice(messages))


# Main menu
def menu():
    print("🎉 Welcome to my Password Generator! 🎉")
    while True:
        print("\nWhat kind of password do you want to have?")
        print("1️⃣ Basic Secure password")
        print("2️⃣ Custom length password")
        print("3️⃣ No special characters (letters + numbers only)")
        print("4️⃣ Lowercase only (no digits or uppercase)")
        print("5️⃣ Strong custom password (18 characters, includes everything)")
        print("6️⃣ Quit")


        choice = input("\nEnter your choice (1-6): ").strip()


        if choice == "1":
            loading_animation()
            pw = fake.password()
            print(f"🔑 Your password: {pw}")
            save_password(pw)
            fun_message()


        elif choice == "2":
            try:
                pw_length = int(input("🔢 Enter your password length: "))
                loading_animation(f"Generating a {pw_length}-character password")
                pw = fake.password(length=pw_length)
                print(f"🔑 Your password: {pw}")
                save_password(pw)
                fun_message()
            except ValueError:
                print("❌ That’s not a valid number! Try again.")


        elif choice == "3":
            loading_animation("Generating letters + numbers password")
            pw = fake.password(special_chars=False)
            print(f"🔑 Your password: {pw}")
            save_password(pw)
            fun_message()


        elif choice == "4":
            loading_animation("Generating lowercase-only password")
            pw = fake.password(digits=False, upper_case=False)
            print(f"🔑 Your password: {pw}")
            save_password(pw)
            fun_message()


        elif choice == "5":
            loading_animation("Generating super strong password")
            pw = fake.password(length=18, special_chars=True)
            print(f"🔑 Your password: {pw}")
            save_password(pw)
            fun_message()


        elif choice == "6":
            print("\n👋 Goodbye! Stay safe out there!")
            break


        else:
            print("❌ Invalid choice! Pick a number from 1 to 6.")
            input("Press Enter to continue...")


        again = input("\n🔄 Do you want to make another password? (y/n): ").strip().lower()
        if again != "y":
            print("\n👋 Goodbye! Stay secure!")
            break


# Run the menu
menu()