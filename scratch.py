# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s = 'abcdefghijklmnopqrstuvwxyz'
conseqStrLen = 1
longestConseqStrLen = 0
endIndex = 0
for charIndex in range(1, len(s)):
    if s[charIndex] >= s[charIndex-1]:
        conseqStrLen += 1
        if conseqStrLen > longestConseqStrLen:
            longestConseqStrLen = conseqStrLen
            endIndex = (charIndex)
    else:
        conseqStrLen = 1
if endIndex == 0:
    print("Longest substring in alphabetical order is: " +  \
      s[(endIndex):(endIndex+1)])
else:
    print("Longest substring in alphabetical order is: " +  \
      s[(endIndex-longestConseqStrLen+1):(endIndex+1)])
    

lyrics = ['I', 'found', 'the', 'love']

def lyricsToDict(lyrics):
    myDict = {}
    for eachWord in lyrics:
        if eachWord in myDict:
            myDict[eachWord] += 1
        else:
            myDict[eachWord] = 1
    return myDict