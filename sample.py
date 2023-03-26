def reverse_string(string):
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

string = input("Enter a string: ")
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)
