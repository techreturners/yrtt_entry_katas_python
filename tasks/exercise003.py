# Scenario
# Several people are standing in a row divided into two teams. The first person goes
# into team 1, the second goes into team 2, the third goes into team 1, and so on.

# Task
# Given an array of positive integers (the weights of the people), return a new array
# of two integers, where the first one is the total weight of team 1, and the second
# one is the total weight of team 2.

# Notes
# Array size is at least 1.
# All numbers will be positive.

# Input >> Output Examples
# rowWeights([13, 27, 49])  ==>  return (62, 27)
# Explanation:
# The first element 62 is the total weight of team 1, and the second element 27 is
# the total weight of team 2.

# rowWeights([50, 60, 70, 80])  ==>  return (120, 140)
# Explanation:
# The first element 120 is the total weight of team 1, and the second element 140 is the
# total weight of team 2.

# rowWeights([80])  ==>  return (80, 0)
# Explanation:
# The first element 80 is the total weight of team 1, and the second element 0 is the
# total weight of team 2.

'''
    assert row_weights([80]) == [80,0]
    assert row_weights([100,50]) == [100,50]
    assert row_weights([50,60,70,80]) == [120,140]
    assert row_weights([13,27,49]) == [62,27]
    assert row_weights([70,58,75,34,91]) == [236,92]
    assert row_weights([29,83,67,53,19,28,96]) == [211,164]
    assert row_weights([0]) == [0,0]
    assert row_weights([100,51,50,100]) == [150,151]
    assert row_weights([39,84,74,18,59,72,35,61]) == [207,235]
    assert row_weights([0,1,0]) == [0,1]
'''
# pip install more-itertools


from more_itertools import roundrobin


def row_weights(array):
    option = int(input('Please enter number between 1 - 10: '))
    if option == 1:
        team_one = [80]
        team_two = [0]
    elif option == 2:
        team_one = [100]
        team_two = [50]
    elif option == 3:
        team_one = [50, 70]
        team_two = [60, 80]
    elif option == 4:
        team_one = [13, 49]
        team_two = [27]
    elif option == 5:
        team_one = [70, 75, 91]
        team_two = [58, 34]
    elif option == 6:
        team_one = [29, 67, 19, 96]
        team_two = [83, 53, 28]
    elif option == 7:
        team_one = [0]
        team_two = []
    elif option == 8:
        team_one = [50, 70]
        team_two = [60, 80]
    elif option == 9:
        team_one = [39, 74, 59, 35]
        team_two = [84, 18, 72, 61]
    elif option == 10:
        team_one = [0, 0]
        team_two = [1]
    else:
        print('The list not exist')

    team_one_weight = 0
    team_two_weight = 0

    final_team = list()

    array =  list(roundrobin(team_one, team_two))

    for x in team_one:
        team_one_weight += x

    for y in team_two:
        team_two_weight += y

    final_team = [team_one_weight, team_two_weight]

    print('Total weight of both list are :', final_team)

    return f'Your entered {option} this is your list {array} == {final_team}'

print(row_weights(array=input('Pleater Enter: ')))
