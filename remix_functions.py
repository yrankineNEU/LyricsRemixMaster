'''
Yana Rankine
CS 5001, Fall 2023
Homework 5 -- Program 1 -- ReMix Master (Functions

This is a program contains additional functions for the RemixMaster

Resources:
Used GeeksforGeeks to learn concise ways to reverse string
Link: https://www.geeksforgeeks.org/python-list-reverse/

Used GeeksforGeeks to understand more how split/join works
Links: https://www.geeksforgeeks.org/python-program-convert-string-list/ 

'''

from music import PLAYLIST
from music import SONGS

def reverse_it(song: list) -> list:
    """
    Function: takes song and reverses the word order
    Input: Song (list)
    Returns: list in reverse word order
    """

    # Initialize string
    string_song = ''
    
    # Break up each element in list and remove punctuation
    for y in song:
        string_song += ' ' + y

    # Split up the string into list words to prevent letters from reversing
    words_string = string_song.split(' ')

    # Reverse song
    song = words_string[-1::-1]

    # Return a list
    return song

def main():


    song = 'old macdonald! had. a farm?'
    
    print(remove_punctuation(song))


                        

if __name__ == "__main__":
    main()
