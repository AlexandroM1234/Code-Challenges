"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
"""
def DNA_strand(dna):
    # code here
    copy = ""
    for letter in dna:
        if letter == "A":
            copy = copy + "T"
        if letter =="T":
            copy = copy + "A"
        if letter == "C":
            copy = copy + "G"
        if letter == "G":
            copy = copy + "C"
    return copy

def tests():
    assert DNA_strand("AAAA") == "TTTT" ,"String AAAA is"
    assert DNA_strand("ATTGC") == "TAACG","String ATTGC is"
    assert DNA_strand("GTAT")=="CATA","String GTAT is"



if __name__ == "__main__":
    tests()
    print("Everything passed")
