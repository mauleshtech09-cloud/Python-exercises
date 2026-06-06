# Practice Problem: You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78]. Print these as a table with aligned columns.

# Exercise Purpose: This exercise introduces “Parallel Iteration.” It teaches you how to step through two related lists simultaneously and format them to look like an organized database table.

names=["Alice","Bob","Charlie"]
scores=[85,92,78]

print(f"{"name":<10} {"score"}")
print("-"*20)

for name,score in zip(names,scores):
    print(f"{name:<10} {score}")