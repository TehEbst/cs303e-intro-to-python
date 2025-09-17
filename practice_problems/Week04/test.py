s = " "
my_list = []

for letter in s:
    if letter in my_list:
        print('its already there')
    else:
        my_list.append(letter)

print(len(my_list))