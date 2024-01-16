"""Name:Kyaw Zaww Linn Date started:18/12/23 GitHub
URL:https://github.com/kyawzawwlinn/cp1404practicals/tree/master/cp1404-song-list-assignment-1-kyawzawwlinn-master"""

import csv

# Constants
SONGS_FILE = 'songs.csv'
UNLEARNED = 'u'
LEARNED = 'l'
STATUS_INDEX = 3


def load_songs():
    try:
        with open(SONGS_FILE, 'r') as file:
            reader = csv.reader(file)
            return [song for song in reader]
    except FileNotFoundError:
        return []


def save_songs(song_list):
    with open(SONGS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(song_list)


def display_songs(song_list):
    if not song_list:
        print("No songs available.")
        return

    for i, song in enumerate(song_list, start=1):
        status = '*' if song[STATUS_INDEX] == UNLEARNED else ''
        plural_suffix = 's' if song[STATUS_INDEX] == UNLEARNED else ''
        print(f"{i}. {song[0]} - {song[1]} ({song[2]}) {status} {plural_suffix}")


def get_valid_year():
    while True:
        year = input("Year: ")
        if year.isdigit() and int(year) > 0:
            return int(year)
        else:
            print("Invalid input; enter a valid number.")


def add_song(song_list):
    title = input("Title: ")
    artist = input("Artist: ")
    year = get_valid_year()

    song_list.append([title, artist, year, UNLEARNED])
    print(f"{title} by {artist} ({year}) added to the song list.")


def complete_song(song_list):
    unlearned_songs = [i for i, song in enumerate(song_list) if song[STATUS_INDEX] == UNLEARNED]

    if not unlearned_songs:
        print("No more songs to learn!")
        return

    display_songs(song_list)
    number = input("\nEnter the number of a song to mark as learned: ")

    while not number.isdigit() or int(number) <= 0 or int(number) > len(song_list):
        print("Invalid song number")
        number = input("\nEnter the number of a song to mark as learned: ")

    index = int(number) - 1

    if song_list[index][STATUS_INDEX] == LEARNED:
        print(f"You have already learned {song_list[index][0]}")
    else:
        song_list[index][STATUS_INDEX] = LEARNED
        print(f"{song_list[index][0]} by {song_list[index][1]} learned")


def main():
    """Name: Kyaw Zaww Linn
    Date started: 18/12/23
    GitHub URL: https://github.com/kyawzawwlinn/cp1404practicals/tree/master/cp1404-song-list-assignment-1-kyawzawwlinn-master

    Song List 1.0 - by Kyaw Zaww Linn
    """

    print("Song List 1.0 - by Kyaw Zaww Linn\n")

    songs = load_songs()
    print(f"{len(songs)} songs loaded.\n")

    while True:
        print("Menu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit\n")

        choice = input(">>> ").lower()

        if choice == 'd':
            display_songs(songs)
        elif choice == 'a':
            add_song(songs)
        elif choice == 'c':
            complete_song(songs)
        elif choice == 'q':
            save_songs(songs)
            print(f"\n{len(songs)} songs saved to {SONGS_FILE}\n\nMake some music!\n")
            break
        else:
            print("Invalid menu choice\n")


if __name__ == "__main__":
    main()
