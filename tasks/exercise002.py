# The clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make the 'past' function return the time converted to milliseconds.
# More examples in the test cases below.

'''
assert past(0,1,1) == 61000
assert past(1,1,1) == 3661000
assert past(1,0,1) == 3601000
assert past(1,0,0) == 3600000
'''

def past(h, m, s):
    h_to_millisec = h * 60 * 60 * 1000
    m_to_millisec = m * 60 * 1000
    s_to_millisec = s * 1000

    result = int(h_to_millisec + m_to_millisec + s_to_millisec)

    return result

print(past(h=int(input('Enter h: ')), m=int(input('Enter m: ')), s=int(input('Enter s: '))))
