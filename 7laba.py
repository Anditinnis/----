class albom:
    def __init__(self, nameAlbom, yerAlbom, listening):
        self.nameAlbom = nameAlbom
        self.yerAlbom = yerAlbom
        self.listening = listening

    def display_info(self):
        print(f"Альбом: {self.nameAlbom} ")
        print(f"Год: {self.yerAlbom} ")
        print(f"Прослушано: {self.listening} раз")
        
class song(albom):
    def __init__(self, nameAlbom, yerAlbom, listening, name):
        #унаследование
        super().__init__(nameAlbom, yerAlbom, listening)
        self.name = name

    def display_info(self):
        super().display_info()
        print(f"Автор: {self.name} \n")


song1 = song("Aladdin Sane", 1973, 17453, "David Bowie")
song2 = song("News Of The World", 1977, 19457, "Queen")

song1.display_info()
song2.display_info()

input()