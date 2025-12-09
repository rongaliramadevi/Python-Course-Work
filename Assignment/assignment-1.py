id = int(input("Enter the App ID: "))
name = input("Enter Name of the App: ")
version = input("Enter the version of App: ")
price = float(input("Enter the cost of App Subscription: "))
discount = float(input("Enter discount percent for subscription: "))

cat = list(map(str.strip, input("Enter the App categories (comma-separated): ").split(',')))

users = tuple(input("Enter Downloads and Users (space-separated): ").split())

features = set(map(str.strip, input("Enter the features (comma-separated): ").split(',')))

developer_details = {
    'developer_name': input("Enter developer name: "),
    'contact': input("Enter developer contact: "),
    'location': input("Enter developer location: ")
}

print("\n" * 3)



print("App ID:", id)
print("Name:", name)
print("Price of Subscription:", price)

print("Discount for subscription: %.2f" % discount)

print("App Version: %s" % version)

print(f"Categories: {', '.join(cat)}")

print(f"Users: {users[0]}")
print(f"Downloads: {users[1]}")

print("Features: {}".format(", ".join(features)))

for key, value in developer_details.items():
    print("{}: {}".format(key, value))