class lyrics_new:
    def __init__(self ,lyrics):
        self.lyrics=lyrics

    def sing_song(self):
        for line in self.lyrics:
            print line

#song1=lyrics_new()
song1=lyrics_new(["mere rashke ka noor tune peheli nazar","happy bday to u","hello bye"])
song1.sing_song()
