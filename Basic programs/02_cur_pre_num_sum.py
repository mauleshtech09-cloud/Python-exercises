# Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

# Exercise Purpose: This exercise teaches “State Tracking.” In programming, you often need to remember a value from a previous loop iteration to calculate results in the current one. This is the basis for algorithms like Fibonacci sequences or running totals.

print("printing previous and current number sum")

prev_num=0

for i in range(11):
    
    sum=prev_num+i
    
    print(f"Sum of previus num : {prev_num} +  current number: {i} = sum : {sum}")

    prev_num=i    
    
    
    