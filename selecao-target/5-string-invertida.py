def convertList(reversed_string):
    str = ''
    for i in reversed_string:
        str += i
    return str

string = input("Insira a string que deseja inverter: ")

reversed_string = []
i = len(string)
while i > 0:
    reversed_string += string[i - 1]
    i = i - 1

print("String invertida:", convertList(reversed_string))
