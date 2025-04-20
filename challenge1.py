sentence1 = 'Compute and print out the sum of the digits from 1 to 10.'
print(sentence1)
print()

total = 0

for digits in range (1, 10+1):
    total+= digits 
    
print ('Sum of range (1-10) is', total)
print()

sentence2 = "Compute and print out the sum of the inputs individually squared, from N1 to N2."
print(sentence2)
print()

total = 0 

n1 = int(input('Enter first number(N1):'))
n2 = int(input('Enter second number(N2):'))
for digits in range(n1, n2+1):
    total += digits**2

print()
print('Sum of inputs squared is', total)

