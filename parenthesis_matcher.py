def parenthesis_matcher(input_string):
    index  = 0
    cur_char = input_string[0]

    while cur_char != "(":
        index += 1
        cur_char = input_string[index]

    lefts = 1
    rights = 0
    while lefts != rights:
        index +=1
        if input_string[index] == ")":
            rights +=1
        elif input_string[index] == "(":
            lefts +=1

    return index

#test cases
"""
print "starting tests"

input_string = "()"
#should return 1
print paren_matcher(input_string) ==1

input_string = "(())"
#should return 3
print paren_matcher(input_string) == 3
input_string = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

#should return 79
print paren_matcher(input_string) == 79
"""
