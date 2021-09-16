import csv

f = open("contacts.txt")

first_last = "FN:"
cell = "TEL;CELL:"
home = "TEL;HOME:"
names = []
phone_numbers = []
final_list = []

for i in f:
    if first_last in i:
        names.append(i[3:-1])
    elif cell in i:
        phone_numbers.append(i[8:-1])
        for j in phone_numbers:
            new_new = j.replace(":", "")
        final_list.append(new_new.replace("+", ""))
        # if not phone_numbers[0].isnumeric():
        #     del phone_numbers[0]
final_names = names[7:]

full_contacts = {}



def add_symbol(string):
    first = []
    second = []
    if len(string) == 11:
        word = '-'.join([string[:1], string[1:4], string[4:7], string[7:]])
        return word
    elif len(string) == 10:
        word = '-'.join([string[:3], string[3:6], string[6:]])
        return word
    elif len(string) == 7:
        word = '-'.join([string[:3], string[3:7]])
        return word
    else:
        return string


last_numbers = []
for numb in final_list:
    words = add_symbol(numb)
    last_numbers.append(words)



for name in final_names:
    full_contacts[name] = last_numbers[0]
    # full_contacts[name].append(final_list[0])
    del last_numbers[0]

print(full_contacts)

with open(
        'C:/Users/Sweat/IdeaProjects/python-masterclass-remaster-shared/current-python-masterclass-remaster/PracticeProblems/test.csv',
        'w') as f:
    for key in full_contacts.keys():
        f.write("%s, %s\n" % (key, full_contacts[key]))
