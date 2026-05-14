# Practice Problem: Write a program to find how many times the substring “Emma” appears in a given string.

# Exercise Purpose: Text analysis and pattern matching are core pillars of programming. This exercise introduces searching for a “needle in a haystack,” a fundamental concept for building search engines or data validation tools.

str1="Emma is a good writer , Emma is very good poet also , Emma and mother of Emma is very rich"

ser=input("Enter a word to search: ")

count=str1.count(ser)

print(f"Count of {ser} = {count}")