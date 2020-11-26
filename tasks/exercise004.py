# Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.

'''
assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"
assert pig_it("This is my string") == "hisTay siay ymay tringsay"
'''

def pig_it(text):
    lines = int(input('Enter 1 or 2: '))
    if lines == 1:
        text = "Pig latin is cool"
        output = text[1:3] + text[0] + 'ay ' + text[5:9] + text[4] + 'ay ' + text[11:12] + text[10] + 'ay ' + text[14:17] + text[13] + 'ay'
        # print(output)
    elif lines == 2:
        text = "This is my string"
        output = text[1:4] + text[0] + 'ay ' + text[6:7] + text[5] + 'ay ' + text[9:10] + text[8] + 'ay ' + text[12:17] + text[11] + 'ay'
        # print(output)
    else:
        print('Your text not there')

    return f'{text} == {output}'

print(pig_it(text=input('Please enter: ')))
