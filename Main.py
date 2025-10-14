from faker import Faker


# Create an instance of the Faker generator
fake = Faker()

# Generate a password
password1 = fake.password()
print("Basic Password:" , password1)

password2 = fake.password(length=14)
print("Costom length( 14 characters):" , password2)