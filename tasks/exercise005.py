# Introduction
# The wave (known as the Mexican wave in the English-speaking world outside North America)
# is an example of metachronal rhythm achieved in a packed
# stadium when successive groups of spectators briefly stand, yell, and raise their arms.
# Immediately upon stretching to full height, the spectator
# returns to the usual seated position.

# The result is a wave of standing spectators that travels through the crowd, even though
# individual spectators never move away from their seats.
# In many large arenas the crowd is seated in a contiguous circuit all the way around the
# sport field, and so the wave is able to travel continuously
# around the arena; in discontiguous seating arrangements, the wave can instead reflect
# back and forth through the crowd. When the gap in seating is narrow,
# the wave can sometimes pass through it. Usually only one wave crest will be present at
# any given time in an arena, although simultaneous, counter-rotating
# waves have been produced. (Source Wikipedia)

# Task
# In this simple Kata your task is to create a function that turns a string into a
# Mexican Wave. You will be passed a string and you must return that string in an array
# where an uppercase letter is a person standing up.

# Rules
#  1.  The input string will always be lower case but maybe empty.
#  2.  If the character in the string is whitespace then pass over it as if it was an
# empty seat
# Example
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

'''
assert wave("") == []
assert wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
assert wave("codewars") == ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
assert wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
assert wave(" gap ") ==  [" Gap ", " gAp ", " gaP "]
'''


def mexican_waving_blank():
    def wave(people):
        msg = input('Press enter: ')
        wave = list(msg)
        return f'("{msg}") == {wave}'
    return wave(people=input('Mexican waving: '))

print(mexican_waving_blank())

def single_words():
    def wave(people):
        msg = str(input('Enter hello or codewars: '))

        # The for loop it works for hello until if len(msg) > 4
        newmsg = []
        for x in range(len(msg)):
            x = msg[0].upper() + msg[1:]
            newmsg.append(x)
            x = msg[0] + msg[1].upper() + msg[2:]
            newmsg.append(x)
            x = msg[0:2] + msg[2].upper() + msg[3:]
            newmsg.append(x)
            x = msg[0:3] + msg[3].upper() + msg[4:]
            newmsg.append(x)
            x = msg[0:4] + msg[4].upper()
            newmsg.append(x)

            # here if the length of the word is longer then 4 until 8
            if len(msg) > 5:
                x = msg[0:5] + msg[5].upper() + msg[6:]
                newmsg.append(x)
                x = msg[0:6] + msg[6].upper() + msg[7:]
                newmsg.append(x)
                x = msg[0:7] + msg[7].upper()
                newmsg.append(x)
        sortmsg = sorted(list(set(newmsg)))

        return f'("{msg}") == {sortmsg}'
    return wave(people=input('Press enter: '))

print(single_words())

def with_gap():
    def wave(people):
        msg = str(input('Enter ( gap ) start and end with empty space: '))
      # is start with empty space
        newmsg = []

        for x in range(len(msg)):
            x = msg[1].lstrip().upper() + msg[2:]
            newmsg.append(x)
            x = msg[0:1] + msg[2].upper() + msg[3:]
            newmsg.append(x)
            # x = msg[0:2] + msg[2].upper() #+ msg[4:]
            # newmsg.append(x)

        sortmsg = sorted(list(set(newmsg)))

        return f'("{msg}") == {sortmsg}'
    return wave(people=input('Press enter: '))

print(with_gap())
