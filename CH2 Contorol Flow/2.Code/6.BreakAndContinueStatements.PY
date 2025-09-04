# Break and continue statements 

# Break statement is used to exit a loop prematurely when a certain condition is met.
# Example of break statement
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
print("Loop ended with break statement")


# Continue statement is used to skip the current iteration of a loop and move to the next iteration.
# Example of continue statement
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
print("Loop ended with continue statement")

