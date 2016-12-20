__author__ = 'dsbatista'

"""
- Reverse string with recursion
 """


def reverse_string(o_string, k, r_string):
    if k == -1:
        print r_string
    else:
        r_string += o_string[k-1]
        k -= 1
        reverse_string(o_string, k, r_string)


def reverse(a_str):
    if len(a_str) <= 1:
        return a_str
    return reverse(a_str[1:]) + a_str[0]


def main():
    s = "isto1 isto2 isto3 isto4"
    r = ""
    #reverse_string(s, len(s), r)
    print reverse(s)


if __name__ == "__main__":
    main()