'''
Yana Rankine
CS 5001, Fall 2023
Homework 5 -- Program 1 -- ReMix Master

This is a program is a song mixing solution
'''
from music import PLAYLIST
from music import SONGS

# Create function that returns a boolean if old word is found in song lyrics
def substitute(song: list, old_word: str, new_word: str ) -> bool:
    """
    Function: takes user input to replace original word in song with new word
    Input: Song (list), old word (string), new word (string)
    Returns: Boolean indicating whether replacement was successful
    """

    # Initialize boolean as false
    flag = False

    # Iterate through each lyrics and replace old word and change boolean
    for x in range(len(song)):
        if old_word in song[x]:
            song[x] = song[x].replace(old_word, new_word)
            flag = True

    # If flag is true, then remove the punctuation
    if flag is True:
        for q in range(len(song)):
            song[q] = remove_punctuation(song[q])

    # Return flag boolean
    return flag

# Create remove punctuation function that words for strings
def remove_punctuation(song: str):
    """
    Function: displays song choice and song title of user's choosing
    Input: Selection (integer)
    Returns: list containing song lyrics and string of song title
    """

    # Create list of punctuation
    punctuation = ['.', ',', ':', '?', '!']

    # Iterate each lyric in song and replace punctation with a space
    for d in song: 
        if d in punctuation:
            song = song.replace(d, '')

    # Return song
    return song

# Create function that reverses song lyrics
def reverse_it(song: list) -> list:
    """
    Function: takes song and reverses the word order
    Input: Song (list)
    Returns: list in reverse word order
    """
    
    # For each lyric, remove punctuation reverse the lyric
    for y in range(len(song)):
        song[y] = remove_punctuation(song[y])
        song[y] = " ".join(song[y].split(' ')[::-1])
    
    # Return a list
    return song

# Create function that loads song into player    
def load_song(selection: int) -> list:
    """
    Function: displays song choice and song title of user's choosing
    Input: Selection (integer)
    Returns: list containing song lyrics and string of song title
    """

    # Initialize list that will hold song lyrics and title
    title_lyrics = []        

    # Create if statement for if input is out of range
    if selection > len(PLAYLIST) or selection <= 0:
        return []

    # Create for loop that iterates list of songs and selects user's choice
    for song in range(len(SONGS)):
        song = (selection - 1)
        song_selection = SONGS[song]

    # Create another loop that iterates list of song titles and selects
    for title in range(len(PLAYLIST)):
        title_selection = PLAYLIST[song]

    # Mutate song lyrics (list) and title (string) at indexes using insert
    title_lyrics.insert(0, song_selection)
    title_lyrics.insert(1, title_selection) 

    # Return mutated song_selection list
    return title_lyrics

# Create function that displays menu options
def menu():
    ''' Function: choose_menu
        Parameters: none
        Returns: nothing
    '''
    # Display menu options
    options = input("ReMix-Master:\n"
                    "L: Load a different song\n"
                    "T: Title of current song\n"
                    "S: Substitute a word\n"
                    "P: Playback your song\n"
                    "R: Reverse it!\n"
                    "X: Reset to original song\n"
                    "Q: Quit?\n" "Your choice: ")

    # Store user's input as a lowercase letter 
    choice = options.lower()

    # Return lowercase letter of user's choice
    return choice

  
def main():

    # Initalize variable outside of the loop
    lyrics_title = load_song(1)
    loaded_song = lyrics_title[0]

    # Use while loop to replay menu() function after each option is satisfied
    while True:
        choice = menu()

        # If loop to load song if user inputs 'l'
        if choice == "l":
            # Print instructions to choose song
            print("Choose the number for the song you want to load:")

            # Create loop that prints the name of each song based on PLAYLIST
            for i in range(len(PLAYLIST)):
                number_option = i + 1
                print(number_option, ":", PLAYLIST[i])
                i = i + 1

            # Once loop prints all options, prompt user to select a number
            user_choice = int(input("Your choice: "))

            # Store loaded song function into lyrics_title for 't' recall
            lyrics_title = load_song(user_choice)

            if lyrics_title == []:
                print('Song choice is out of range.')
            else:
                # Store the lyrics in loaded_song variable for easier recall
                loaded_song = lyrics_title[0]

                print('Song was loaded to mix successfully!\n')
            
        # Create loop if user chooses 't' that prints song title
        elif choice == 't':

            # Create loop that selects default song if no song is chosen
            if loaded_song == []:
                # Load first song & title 
                default_song = SONGS[0]
                default_title = PLAYLIST[0]

                # Copy song lyrics to loaded song list
                loaded_song = default_song[:]

                # Add default title to loaded song list
                loaded_song.insert(1, default_title)

            # If song was choosen
            else:
                loaded_song = loaded_song

            # Print title of loaded song
            title = lyrics_title[1]
            print(title, '\n')

        # Create if loop if user chooses 's' that substitutes word
        elif choice == 's':

            # Store user's word input in variables
            old_word = str(input('What word do you want to replace? '))
            new_word = str(input('Choose a replacement word for the song? '))

            # Store Substitute function's boolean result in valid_replacement             
            valid_replacement = substitute(loaded_song, old_word, new_word)

            # Create message notifying user's if replacement was succesful
            if valid_replacement is True:
                print('Word replacement was successful!\n')
            
            else:
                print('Uh-oh, word replacement was not successful.\n')         

        # Create loop if user chooses 'p' that playbacks lyrics
        elif choice == 'p':

            # Initialize string
            playback = ''

            # Print loaded_song as a string
            for z in loaded_song:
                playback += ' ' + z
                # Remove trailing white spaces using strip()
                playback.lstrip()

            # Print lyrics
            print(playback, "\n")

        # Create loop to reverse lyrics 'r'
        elif choice == 'r':

            # Store reverse_it list in loaded_song variable
            loaded_song = reverse_it(loaded_song)

            # Print line space to improve readability
            print('Song lyrics were reversed successfully!\n')
            
        # Create loop to reset to original song 'x'
        elif choice == 'x':

            # Recall original user's choice from 'l' loop load_song function
            lyrics_title = load_song(user_choice)

            # Reset loaded_song variable
            loaded_song = lyrics_title[0]

            # Print message to let user know that reset was successful
            print("Song reset was successful!\n")
            
        # Break loop if user inputs 'q'
        else:
            if choice == "q":
                print("Bravo! Your Grammy Award is being shipped to you now!")
                break
    
if __name__ == "__main__":
    main()
