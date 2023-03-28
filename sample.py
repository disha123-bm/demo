import argparse

def reverse_string(string):
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

parser = argparse.ArgumentParser(description='Reverse a string')
parser.add_argument('input_string', type=str, help='The string to reverse')

args = parser.parse_args()
input_string = args.input_string

reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
