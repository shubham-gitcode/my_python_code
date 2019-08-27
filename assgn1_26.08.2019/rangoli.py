import string
alpha = string.ascii_lowercase

n = int(input('Enter no of rows. : '))
output = []

for i in range(n):
    s = "-".join(alpha[i:n])
    output.append((s[::-1] + s[1:]).center(4*n-3, "-"))
    
print('\n'.join(output[:0:-1] + output))


