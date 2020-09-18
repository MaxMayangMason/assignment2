#!/usr/bin/env python
import csv
from datetime import datetime
from sys import argv
from music import Album, Song


def get_all_albums():
    return "Implement me"


def get_songs_by_date(after=True):
    if len(argv) < 4:
        raise ValueError("use is python3 grittify.py album [album-name]")
    date_object = datetime.strptime(argv[3], '%m/%d/%Y')
    albums = get_all_albums()
    for album in albums:
        for song in album.songs:
            if after and song.after(date_object):
                song.print()
            if not after and song.before(date_object):
                song.print()


if __name__ == '__main__':
    if len(argv) < 2:
        raise ValueError("use is python3 grittify.py [command] [args]")
    if argv[1] == 'albums':
        albums = get_all_albums()
        for album in albums:
            album.print()
    elif argv[1] == 'album':
        if len(argv) < 3:
            raise ValueError("use is python3 grittify.py album [album-name]")
        albums = get_all_albums()
        album_name_param = argv[2]
        print("The songs on {} are:".format(album_name_param))
        for album in albums:
            if album.name == album_name_param:
                for song in album.songs:
                    song.print()
    elif argv[1] == 'songs' and len(argv) == 2:
        albums = get_all_albums()
        for album in albums:
            for song in album.songs:
                song.print()
    elif argv[1] == 'songs' and argv[2] == "after":
        get_songs_by_date(True)
    elif argv[1] == 'songs' and argv[2] == "before":
        get_songs_by_date(False)
    else:
        raise ValueError("use is python3 grittify.py [command] [args]")