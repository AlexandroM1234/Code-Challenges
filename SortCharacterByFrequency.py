class Solution:
    def frequencySort(self, s: str) -> str:
        """
        loop through the string and have a hashtable to keep track of the amount of times the char shows up in the string
        afterwards have s be a sorted array which is sorted by the sorted function
        you pass in check the key is the keys in the hashtable 
        and you reverse it because we want to sort descending
        now that we have a sorted array of the characters you loop through it and look up the character in the hashtable and then multiply
        it buy the value at the key and add it to the output string
        """
        check = {}
        output = ""
        for char in s:
            if char not in check:
                check[char] = 1
            else:
                check[char] += 1
        s = sorted(check, key =lambda x:check[x],reverse=True)
        for i in s:
            output += i * check[i]
        return output