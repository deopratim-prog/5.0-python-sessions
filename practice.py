# numbers = [10, 15, 20, 5, 8, 12, 16, 18]

# max_streak = 1
# current_streak = 1

# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         current_streak += 1
#     else:
#         current_streak = 1

#     if current_streak > max_streak:
#         max_streak = current_streak

# print("Longest increasing streak:", max_streak)

# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# duplicates = []

# for i in range(len(numbers)):
#     count = 0

#     for j in range(len(numbers)):
#         if numbers[i] == numbers[j]:
#             count += 1

#     if count > 1 and numbers[i] not in duplicates:
#         duplicates.append(numbers[i])

# print("Duplicates:", duplicates)

# text = input("Enter text: ")

# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# for char in frequency:
#     print(char, ":", frequency[char])

# sentence = input("Enter sentence: ")

# words = sentence.split()

# longest_word = ""

# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word

# print("Longest word:", longest_word)

# amount = int(input("Enter amount: "))

# notes = [2000, 500, 200, 100, 50, 20, 10]

# for note in notes:
#     if amount >= note:
#         count = amount // note
#         print(f"{note} x {count}")
#         amount %= note

# resume = """
# Python developer with experience in Git and Machine Learning.
# """

# keywords = [
#     "Python",
#     "SQL",
#     "Machine Learning",
#     "Git",
#     "Docker"
# ]

# found = 0

# print("Missing Skills:")

# for skill in keywords:
#     if skill.lower() in resume.lower():
#         found += 1
#     else:
#         print("-", skill)

# score = (found / len(keywords)) * 100

# print(f"\nMatch Score: {score:.2f}%")

# transactions = [
#     1000,
#     80000,
#     120000,
#     95000,
#     500,
#     200000
# ]

# consecutive = 0

# for amount in transactions:

#     if amount > 50000:
#         consecutive += 1
#         print("Suspicious Transaction:", amount)

#     else:
#         consecutive = 0

#     if consecutive == 3:
#         print("\nALERT: Possible Fraud Detected")
#         break

# attendance = {
#     "Amit": ["P", "P", "A", "P", "P"],
#     "Riya": ["A", "P", "A", "P", "A"],
#     "Karan": ["P", "P", "P", "P", "P"]
# }

# for student in attendance:

#     present = 0

#     for status in attendance[student]:
#         if status == "P":
#             present += 1

#     percentage = (present / len(attendance[student])) * 100

#     print(student, ":", percentage, "%")

#     if percentage < 75:
#         print("  Warning: Attendance below 75%")

# documents = [
#     "Python is a programming language",
#     "Artificial Intelligence is growing rapidly",
#     "Python is widely used in AI",
#     "Data Science uses Python"
# ]

# query = input("Search: ").lower()

# print("\nResults:\n")

# for doc in documents:
#     if query in doc.lower():
#         print(doc)

# orders = [
#     ["Laptop", "Mouse"],
#     ["Laptop", "Keyboard"],
#     ["Laptop", "Mouse"],
#     ["Mouse", "Keyboard"],
#     ["Laptop", "Mouse"],
# ]

# target = "Laptop"

# recommendations = {}

# for order in orders:

#     if target in order:

#         for item in order:

#             if item != target:

#                 if item in recommendations:
#                     recommendations[item] += 1
#                 else:
#                     recommendations[item] = 1

# best_item = ""
# highest_count = 0

# for item in recommendations:

#     if recommendations[item] > highest_count:
#         highest_count = recommendations[item]
#         best_item = item

# print("Recommended Product:", best_item)

# logs = [
#     "ERROR",
#     "INFO",
#     "ERROR",
#     "WARNING",
#     "INFO",
#     "ERROR",
#     "WARNING"
# ]

# count = {}

# for log in logs:

#     if log in count:
#         count[log] += 1
#     else:
#         count[log] = 1

# print("Log Summary:\n")

# for log_type in count:
#     print(log_type, "->", count[log_type])
