def print_rangoli(n):
    # your code goes here
    import string
    design = string.ascii_lowercase

    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



'''

The expression s[::-1]+s[1:] concatenates two parts of the string s: the reversed version of s (s[::-1]) and s excluding the first character (s[1:]).

Let's break it down with an example:

Suppose s is the string "abcde".

    s[::-1] reverses the string, resulting in "edcba".
    s[1:] slices the string starting from the second character, resulting in "bcde".

Then, the expression s[::-1]+s[1:] concatenates these two parts, resulting in "edcbabcde".

In summary, s[::-1]+s[1:] takes a string s, reverses it, and appends it to the original string s excluding the first character.
'''    