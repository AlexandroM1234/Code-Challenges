"""
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.

Example

For address = "prettyandsimple@example.com", the output should be
findEmailDomain(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be
findEmailDomain(address) = "codesignal.com".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string address

Guaranteed constraints:
10 ≤ address.length ≤ 50.

[output] string
"""


def findEmailDomain(address):
    # take in the string and start looping through it backwards
    i = -1
    output = ""
    # keep traversing the string backwards while the value of one of the strings isn't a @
    while address[i] != "@":
        # keep appending to the output stnring
        output += address[i]
        i -= 1
    # once you get to the @ the output string is backwards so we have to return it backwards so its forward
    return output[::-1]
