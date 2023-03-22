# Create a dictionary to hold user account details
users = {}

# Define a function to validate user authentication
def validate_user(user):
    return True

# Define a function to provide savings schemes based on user age
def provide_savings_schemes(user):
    age = user.get('age')
    if age < 18:
        return "Guide for education camps schemes"
    elif age < 35:
        return "Provide educational scholarship scheme"
    else:
        return "Guide for retirement plans"

# Create multiple user accounts and validate their authentication
users['user1'] = {'name': 'John Doe', 'age': 25, 'address': '123 Main St', 'contact': '555-1234', 'pin': '1234'}
if validate_user(users['user1']):
    print("Authentication successful")
else:
    print("Authentication failed")

users['user2'] = {'name': 'Jane Smith', 'age': 16, 'address': '456 Maple Ave', 'contact': '555-5678', 'pin': '5678'}
if validate_user(users['user2']):
    print("Authentication successful")
else:
    print("Authentication failed")

# Provide savings schemes based on user age
for user in users.values():
    savings_scheme = provide_savings_schemes(user)
    print(f"{user['name']} ({user['age']}): {savings_scheme}")
