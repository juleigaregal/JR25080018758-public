# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 17:45:08 2025

@author: juleigar
"""

class Album_management:
    
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
        

class Albums(Album_management):
    
    def __init__(self):
        self.albums = []
        
    
    def album_store(self, album_list):
        for (names, num_songs, artist) in album_list:
            music_lib = Album_management(names, num_songs, artist)
            self.albums.append(music_lib)
            #print(self.names, self.artist, self.num_songs)
            
            
            
    def album_display(self):
            for i in self.albums:
                    print(i.album_name, i.album_artist, i.number_of_songs)
    
    def album_swap(self, index, index1):
        if index <len(self.albums) and index1 <len(self.albums):
            self.albums[index], self.albums[index1] = self.albums[index1], self.albums[index]

albums1 = [ ("Thriller", 15, "Michael Jackson"),
           ("Best hits of 80s", 1, "Madonna"),
           ("Best hits of 90s", 8, "Boy George"),
           ("Good times", 11, "George Michael"),
           ("Hero", 6, "Barbar Streisand"),
           ("Like a prayer", 16, "Madonna")]

albums2 =  [ ("Forever young", 3, "Michael Jackson"),
           ("Best hits of 70s", 17, "Irvine levine"),
           ("Best hits of 20s", 2, "Somebody cool"),
           ("Bad times", 11, "George Oliver"),
           ("Dickens", 6, "Streisand"),
           ("Like a god", 16, "Boreao")]

albums2 = albums2 + albums1

albums2_add = [("Dark Side of the Moon", 9,"Pink Floyd"),("Oops!... I Did It Again",16,"Britney Spears") ]
albums2 = albums2 + albums2_add


print(albums2)

music = Albums()
music.album_store(sorted(albums1, key=lambda albums1: albums1[1]))
music.album_display()

music.album_swap(0,1)

print("\nAfter swap")
music.album_display()

store_sorted_ablum2 =  sorted(albums2, key=lambda album: album[0])



print("Combined and sorted albums2:\n")
for album in store_sorted_ablum2:
    print(album)

def search_parameters(target, album_list):
        
        for index, (x, y, z) in enumerate(album_list): #if you want to return index need to use enumerate
            if x == target:
                return index
            
        else:
            print("Does not exist")

x = search_parameters("Dark Side of the Moon",store_sorted_ablum2) 
print(x)   