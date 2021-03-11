"""
You are implementing your own HTML editor. To make it more comfortable for developers you would like to add an auto-completion feature to it.

Given the starting HTML tag, find the appropriate end tag which your editor should propose.

If you are not familiar with HTML, consult with this note.

Example

For startTag = "<button type='button' disabled>", the output should be
htmlEndTagByStartTag(startTag) = "</button>";
For startTag = "<i>", the output should be
htmlEndTagByStartTag(startTag) = "</i>".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string startTag

Guaranteed constraints:
3 ≤ startTag.length ≤ 75.

[output] string
"""


def htmlEndTagByStartTag(startTag):
    tag = ""
    i = 1
    # itterate through the start tag for the length of the string
    while i != len(startTag):
        # if one of the characters value is equal to a space or > break out of the loop
        if startTag[i] == " " or startTag[i] == ">":
            break
        # otherwise keep adding the tag to the string
        tag += startTag[i]
        i += 1
    # finally return the closing tag with the closing tags around them
    return "</" + tag + ">"