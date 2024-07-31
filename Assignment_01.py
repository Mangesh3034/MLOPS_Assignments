#finding orange and printing it's index
def find_orange(list):
    for fruit in list:
        if(fruit=='orange'):
            return list.index('orange')
    return "Not found"

five_fruits=['Apple','Banana','Blackberry','Cherry','orange']
print(find_orange(five_fruits))


#printing array pyramid
def print_pyramid(height):
    for i in range(1,height + 1):
        space = ' ' * (height - i)
        star = '*' * i
        print(space + star)

print_pyramid(5)