while True:
    one_line = input("Evaluate: ")
    one_line = one_line.replace(" ", "")

    if '+' in one_line:
        i = one_line.find('+')
        ans = int(one_line[:i]) + int(one_line[i+1:])
    elif '-' in one_line:
        i = one_line.find('-')
        ans = int(one_line[:i]) - int(one_line[i+1:])
    elif '*' in one_line:
        i = one_line.find('*')
        ans = int(one_line[:i]) * int(one_line[i+1:])
    elif '/' in one_line:
        i = one_line.find('/')
        ans = int(one_line[:i]) / int(one_line[i+1:])
        
    print(ans)
    
    again = input("Calculate Again(y/n): ")
    if again.lower() == 'n':
        break