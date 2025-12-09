n = int(input("Enter the number of messages: "))
data = {}

for i in range(n):
    name, msg = input().split(":")
    msg = msg.strip()

    if name in data:
        data[name].append(msg)
    else:
        data[name] = [msg]

print("\nChat Data:", data)

choices = {
    1: 'Count total number of messages',
    2: 'Identify unique users in chat',
    3: 'Count total words in chat',
    4: 'Calculate average words per message',
    5: 'Find the longest message sent',
    6: 'Find the most active user',
    7: 'Get message count for a specific user',
    8: 'Find the most frequently used word by a specific user',
    9: 'Retrieve the first and last message sent by a user',
    10: 'Check if a user is present in the chat',
    11: 'Find commonly repeated words',
    12: 'Identify the user with the longest average message length',
    13: 'Count how many messages mention a specific user',
    14: 'Remove duplicate messages',
    15: 'Sort messages alphabetically',
    16: 'Extract all questions asked in the chat',
    17: 'Calculate the reply ratio between two users',
    18: 'Check for deleted messages',
    19: 'Exit'
}

while True:
    print("\n--- Menu ---")
    for i in sorted(choices):
        print(f"{i}. {choices[i]}")

    
    choice = input("Enter your choice: ").strip()

    if choice == "":
        print("❗ Please enter a number.")
        continue

    if not choice.isdigit():
        print("❗ Only numbers allowed.")
        continue

    ch = int(choice)

    if ch == 1:
        cnt = sum(len(data[user]) for user in data)
        print("Total messages in chat:", cnt)

    elif ch == 2:
        print("Unique users in chat:", len(data))
        print("Users:", ", ".join(data.keys()))

    elif ch == 3:
        total_words = sum(len(msg.split()) for user in data for msg in data[user])
        print("Total words in chat:", total_words)

    elif ch == 4:
        total_messages = sum(len(data[user]) for user in data)
        total_words = sum(len(msg.split()) for user in data for msg in data[user])
        avg = total_words / total_messages if total_messages else 0
        print("Average words per message:", avg)

    elif ch == 5:
        longest = ""
        user_longest = ""
        for user in data:
            for msg in data[user]:
                if len(msg) > len(longest):
                    longest = msg
                    user_longest = user
        print("Longest message:", longest, " (by ", user_longest, ")")

    elif ch == 6:
        most_active = max(data, key=lambda u: len(data[u]))
        print("Most active user:", most_active)

    elif ch == 7:
        user = input("Enter username: ")
        if user in data:
            print(user, "sent", len(data[user]), "messages.")
        else:
            print("User not found.")

    elif ch == 8:
        user = input("Enter username: ")
        if user in data:
            word_count = {}
            for msg in data[user]:
                for w in msg.split():
                    word_count[w] = word_count.get(w, 0) + 1
            max_word = max(word_count, key=word_count.get)
            print("Most frequent word by", user, "is:", max_word)
        else:
            print("User not found.")

    elif ch == 9:
        user = input("Enter username: ")
        if user in data:
            print("First message:", data[user][0])
            print("Last message:", data[user][-1])
        else:
            print("User not found.")

    elif ch == 10:
        user = input("Enter username: ")
        print("User exists." if user in data else "User NOT found.")

    elif ch == 11:
        word_count = {}
        for user in data:
            for msg in data[user]:
                for w in msg.split():
                    word_count[w] = word_count.get(w, 0) + 1
        repeated = {w: c for w, c in word_count.items() if c > 1}
        print("Repeated words:", repeated)

    elif ch == 12:
        max_avg = 0
        selected_user = ""
        for user in data:
            total_len = sum(len(msg) for msg in data[user])
            count = len(data[user])
            avg = total_len / count
            if avg > max_avg:
                max_avg = avg
                selected_user = user
        print("User with longest average message:", selected_user)

    elif ch == 13:
        target = input("Enter name to check mentions: ")
        count = sum(target in msg for user in data for msg in data[user])
        print("Mentions of", target, ":", count)

    elif ch == 14:
        for user in data:
            new_list = []
            for msg in data[user]:
                if msg not in new_list:
                    new_list.append(msg)
            data[user] = new_list
        print("Duplicates removed.")
        print(data)

    elif ch == 15:
        for user in data:
            data[user].sort()
        print("Messages sorted.")
        print(data)

    elif ch == 16:
        questions = [msg for user in data for msg in data[user] if msg.endswith("?")]
        print("Questions:", questions)

    elif ch == 17:
        u1 = input("Enter first user: ")
        u2 = input("Enter second user: ")

        if u1 in data and u2 in data:
            if len(data[u2]) == 0:
                print("Reply ratio: Infinity")
            else:
                ratio = len(data[u1]) / len(data[u2])
                print("Reply ratio (", u1, ":", u2, ") =", ratio)
        else:
            print("One or both users not found.")

    elif ch == 18:
        deleted = [msg for user in data for msg in data[user] if "deleted" in msg.lower()]
        print("Deleted messages:", deleted)

    elif ch == 19:
        print("End of program")
        break

    else:
        print("Invalid choice, try again!")

