# Initialize first three values of the sequence
# Check if user input is larger than 3,
# If it is we add three numbers together, get the new one and shift the variables up the sequence
# we stop when we have the n numbers requested
n = int(input("Enter the length of the sequence: ")) # Do not change this line

n_1,n_2,n_3 = 1,2,3

if n < 4:
    n_1 = 0
    for i in range(0,n):
        n_1 += 1
        print(n_1)
else:
    for number in (n_1,n_2,n_3):
        print(number)
    for number in range(0,n-3):
        value = n_1 + n_2 + n_3
        print(value)
        n_1 = n_2
        n_2 = n_3
        n_3 = value
