# Developer a program which simulates very simpe Music APP.

# Rules:

# 1. Create Nested Tuple with given song list. 
#     - Green Day
#             1. Somewhere Now
#             2. Bang Bang
#             3. Revolution Radio
#             4. Say Goodbye
#             5. Outlaws
#     - Metallica
#             1. Battery
#             2. Master of Puppets
#             3. The Thing That Should Not Be
#             4. Welcome Home (Sanitarium)
#     - U2
#             1. The Miracle
#             2. Every Breaking Wave
#             3. California
#             4. Song for Someone
#             5. Iris (Hold Me Close)
# 2. Show Ascii art logo
# 3. Print Song list
# 4. Ask from user to select a song based on number (1:1). First digit is band 
# number and second digit is song number. 
# For example 1:1 means first band and first song which is "Green Day Somewhere" 
# Now in our case.
# 5. Playing song and asking if a user want to select different song or not. 
# If not app terminates.
# Example Output
# ███    ███ ██    ██ ███████ ██  ██████      █████  ██████  ██████  
# ████  ████ ██    ██ ██      ██ ██          ██   ██ ██   ██ ██   ██ 
# ██ ████ ██ ██    ██ ███████ ██ ██          ███████ ██████  ██████  
# ██  ██  ██ ██    ██      ██ ██ ██          ██   ██ ██      ██      
# ██      ██  ██████  ███████ ██  ██████     ██   ██ ██      ██   
# 1:1 Green Day - Somewhere Now
# 1:2 Green Day - Bang Bang
# 1:3 Green Day - Revolution Radio
# 1:4 Green Day - Say Goodbye
# 1:5 Green Day - Outlaws
# 2:1 Metallica - Battery
# 2:2 Metallica - Master of Puppets
# 2:3 Metallica - The Thing That Should Not Be
# 2:4 Metallica - Welcome Home (Sanitarium)
# 3:1 U2 - The Miracle
# 3:2 U2 - Every Breaking Wave
# 3:3 U2 - California
# 3:4 U2 - Song for Someone
# 3:5 U2 - Iris (Hold Me Close)
# Select a song to play using number:(1:1) 1:2
# Green Day - Bang Bang playing now....
# Press C to change song or any letter to quit APP:

from AsciiArt import musicapp_logo as logo
from MusicAppList import play_list as playlist
from os import system as s
s('cls')
print(logo)
def print_playlist():
    """Songs playlist is displayed"""
    for b_index, band in enumerate(playlist,1):
        name, songs = band
        print(f"{b_index}. {name}")
        for s_index, song in songs:
            print(f"     {s_index}. {song}")

def print_song(p_bnumber:int, p_snumber:int):
    """Song data is displayed using band name and song name 
    \n@p_bnumber: required parameter Band number
    \n@p_snumber: required parameter Song number"""
    band_name = playlist[p_bnumber-1][0]
    song_name = playlist[p_bnumber-1][1][p_snumber-1][1]
    print(f" \n {band_name} - {song_name} playing now...")

while True:
    print_playlist()
    current_play = input ("\nSelect a song to play usin number (1:1) ")
    band_numer = int(current_play[0])
    song_numer = int(current_play[2])
    print_song(band_numer,song_numer)
    change = input ("\nPress C to change the song or any key to quit App: ")
    if change == "C" or change == "c":
        continue
    break
print("Good Bye! ")

            