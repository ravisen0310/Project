#!usr/bin/usr/env python 

print("I am from GitHub")

def reverse_complement(sequence):
    output = ""
    complement = {"A":"T","T":"A", "C":"G", "G":"C"}
    for nt in sequence[::-1]:
        output +=nt 
    return output 
