def rev_string(str, i=0):
    #sanity check
    if len(str) == 0:
        return ""
    #base case
    elif i == len(str)-1:
        return str[0]
    else:
        #recursive case
        return str[-1-i] + rev_string(str, i+ 1)


print(rev_string("tacobell"))
print(rev_string("makes"))
print(rev_string("my"))
print(rev_string("tummy"))
print(rev_string("hurt"))
