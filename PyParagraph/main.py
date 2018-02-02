#################################################################################
# This is the main script for the PyParagraph Homework Assignment
# The scrit asks for the name of the text file to read. It reads the file and produces
# Some analysis on the file that it prints out
#################################################################################

import os
import re

inputFile = input("Please enter the name of the file in the raw_data folder to analyze.  ")

inputPath = os.path.join("raw_data", inputFile)

with open(inputPath, "r") as paraFile:

    text = paraFile.read()

    #split the text into words
    #Not using the '\W+' pattern as it considers "-" as a word
    #words = re.split(r'\W+', text)
    words = re.split(r'[.!?,:;"() -]+', text)
    wordCount = len(words)

    # split the text into sentences
    sentences = re.split(r'[.!?] +', text)
    sentenceCount = len(sentences)

    # The average sentence length in words will be the number of words
    # divided by number of sentences
    avgSentLen = wordCount/sentenceCount

    num = 0

    # get the total number of letters
    for w in words:
        num += len(w)
        
    # letter count = total number of letters/word count
    letterCount = num/wordCount

print("Paragraph Analysis")
print("-----------------------------")
print("Approximate Word Count:  " + str(wordCount))
print("Approximate Sentence Count:  " + str(sentenceCount))
print("Average Letter Count:  " + str(letterCount))
print("Average Sentence Length (in words):  " + str(avgSentLen))


        