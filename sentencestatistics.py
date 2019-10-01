#Amanda Maglaras
#amanda.maglaras1@marist.edu
#Sentence Statistics Project 5
#This project will find the number of characters & words, and average word length

def main():
    sentence= input("Please enter your sentence: ")

    #This next line will determine the number of characters in the sentence
    charinsen=len(sentence)
    print("Number of characters: ", charinsen)

    #This next line will determine the number of words in the sentence
    words= len(sentence.split())
    print("Number of words: ", words)

    #This next line will count the average length of the words
    #This cannot include the whitespace between each word so I used .replace
    x=len(sentence.replace(" ", ""))/words
    print("Average Word Length: ", x)

main() 
