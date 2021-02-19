user_input = ''
list_of_el = []

while user_input != 'stop':
    user_input = input("Enter something, "
                       "if you want to stop, write 'stop' -> ")
    if user_input == 'stop':
        break
    list_of_el.append(user_input)

_len = (len(list_of_el), len(list_of_el) - 1)[len(list_of_el) % 2]
for index in range(0, _len, 2):
    list_of_el[index], list_of_el[index + 1] = list_of_el[index + 1], list_of_el[index]

print(list_of_el)
