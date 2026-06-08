import random

class Song:
    def __init__(self,title,artist):
        self.title=title
        self.artist=artist
        
        
class Playlist:
    def __init__(self,title):
        self.title=title
        self.songs=[]
        
    def show_Song(self):
        if len(self.songs) == 0 :
            print("Playlist is empty!")
            
        titles = [s.title for s in self.songs]
        print(f"Playlist : {', '.join(titles)}")
                       
    def add_Song(self,song):
        self.songs.append(song)
        
    def remove_Song(self,title):
        original_count=len(self.songs)
        self.songs=[s for s in self.songs if s.title != title]
        
        if len(self.songs) < original_count:
            print(f"Song removed , {title}")
            
        else:        
            print(f"{title} is not found in the playlist!")
                
    def shuffle_Song(self):
        random.shuffle(self.songs)
        print(f"Playlist shuffled, note that after shuffle order might be change")
        
        
playlist=Playlist("My Mix")
playlist.add_Song(Song("Go Down Deh","DJ Snake"))
playlist.add_Song(Song("Rings","Taylor Swift"))
playlist.add_Song(Song("Sorry","Justin Bieber"))

playlist.show_Song()
playlist.shuffle_Song()
playlist.show_Song()
playlist.remove_Song("Rings")
playlist.show_Song()
                    
        
                  
                    