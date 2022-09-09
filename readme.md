# One Line Calculator

1. Ask user for input once
``` Python
one_line = input("Evaluate: ")
```

2. remove any spaces in the input string
``` Python
one_line = one_line.replace(" ", "")
```

3. find the operand
``` Python
if '+' in one_line:
```

4. get the numbers and evacuate
``` Python
i = one_line.find('+')
ans = int(one_line[:i]) + int(one_line[i+1:])
```

5. Print the result
``` Python
print(ans)
```
6. Repeat again
``` Python
while True:
    again = input("Calculate Again(y/n): ")
    if again.lower() == 'n':
        break
```
