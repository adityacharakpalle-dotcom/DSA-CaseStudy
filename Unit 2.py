
# WhatsApp Contact Network

users = ["Aditya", "Rahul", "Priya", "Sneha", "Amit"]
n = len(users)

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

print("WHATSAPP CONTACT NETWORK")
print("\nAdjacency Matrix:")

print("     ", *users)
for i in range(n):
    print(users[i], graph[i])


user1 = "Aditya"
user2 = "Rahul"

i = users.index(user1)
j = users.index(user2)

if graph[i][j] == 1:
    print("\n", user1, "and", user2,
          "have a direct connection.")
else:
    print("\n", user1, "and", user2,
          "do not have a direct connection.")

# Check common group members
group1 = {"Aditya", "Rahul", "Priya"}
group2 = {"Priya", "Sneha", "Amit"}

common = group1.intersection(group2)

print("\nCommon Group Members:", common)
