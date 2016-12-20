__author__ = 'dsbatista'

"""
- Segment a long string into a set of valid words using a dictionary.
Return false if the string cannot be segmented. What is the complexity of
your solution?
"""

dictionary = {'this': True,
              'that': True,
              'done': True,
              }


def simple_case(input_string):
    """
    only splits the string in two
    :param input_string:
    :return:
    """
    for i in range(0, len(input_string)):
        prefix = input_string[0:i]
        if prefix in dictionary.keys():
            suffix = input_string[i:len(input_string)]
            if suffix in dictionary.keys():
                print prefix + " " + suffix


def simple_case_recursive(input_string):
    if len(input_string) == 0:
        return True
    for i in range(len(input_string)):
        prefix = input_string[:i+1]
        print input_string, i, prefix, dictionary.keys(), input_string[i+1:len(input_string)+1]
        if prefix in dictionary.keys() and \
                simple_case_recursive(input_string[i+1:len(input_string)+1]):
            return True


# TODO: Knuth-Morris-Pratt algorithm


def main():
    #string = "thisthat"
    string = "thatdonethisthat"
    if simple_case_recursive(string):
        print "true"
    else:
        print "false"

if __name__ == '__main__':
    main()