# print
# print("Hello, everyone")

# add
# def addition(a, b):
#     return a + b
# print(addition(2,3)== 5)
# print(addition(-3,-6) == -9)
# print(addition(7,3)== 10)

# 
# def fam(name):
#     if name "Darth vader"
# print(name("Darth Vader"), "Luke, I am your father.")
# Test.assert_equals(relation_to_luke("Leia"), "Luke, I am your sister.")

# 
# def relation_to_luke(name):
#     family ={
#     "Darth Vader":	"father",
#     "Leia":  "sister",
#     "Han" :	"brother in law",
#     "R2D2" :" droid"
#     }
#     family = family[name]
#     return "Luke, I am your "  +  family + "."

# a = relation_to_luke("Leia")
# print(a)


# 
def reverse_char(char):
    """
    Reverse a character either lower or capital. 
    """
    # define alphabet
    alphabets = 'abcdefghijklmnopqrstuvwsyz'

    if char in alphabets.upper():
        alphabets = alphabets.upper()

    index_of_char = alphabets.index(char)
    # find opp index
    opposite_index = 26 - index_of_char
    # find opp char based on opp index
    opposite_char = alphabets[opposite_index - 1]

    return opposite_char
    # print(opposite_index)

    # print(reverse('a') == 'z')
    # print(reverse('b') == 'y')
    # print(reverse('c') == 'x')

    # reverse('c') 
    # x = reverse('a')
    # print(x)

    print(reverse_char('A') == 'Z')
    print(reverse_char('a') == 'z')

# loop
# for x in "hello":
#   print(x) 