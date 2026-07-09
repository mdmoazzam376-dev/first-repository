
def data(name,age,number):

    return name,age,number


name = input('Name: ')
age = input('age: ')
number = input('number: ')
data(name,age,number)

print(f'\nname:{name} \nage:{age} \nnumber:{number}')