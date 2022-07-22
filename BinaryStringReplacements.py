"""
No code will be written for this one but I did like the question a lot

The basic premise of the question is you are given a binary string ex. "10101000"

You are also given an array of instructions to either count or flip the string ex. ["Count", "Flip" ....]

When you iterate through the array if you have a count you count the number of 1's in the string
If you have a flip go from the left and find the first 0 and every 1 or 0 up until that first 0 you flip to the reverse. ex. 1 => 0, 0 => 1

The output will be dependent in the order of the operations so if you have a count then find the number of 1's add that to the array.
For the flips you would append the index of the first 0

Then return the output array
"""
