# album_manager.py
import os

class AlbumManager:
    def __init__(self):
        self.albums_file = "data/albums.txt"
        self.albums = self.load_albums()

    def load_albums(self):
        if os.path.exists(self.albums_file):
            with open(self.albums_file, "r") as file:
                return [line.strip() for line in file.readlines()]
        else:
            return []

    def save_albums(self):
        with open(self.albums_file, "w") as file:
            for album in self.albums:
                file.write(album + "\n")

    def create_album(self, album_name):
        if album_name not in self.albums:
            self.albums.append(album_name)
            self.save_albums()
            print(f"Album '{album_name}' créé avec succès.")
        else:
            print("Cet album existe déjà.")

    def delete_album(self, album_name):
        if album_name in self.albums:
            self.albums.remove(album_name)
            self.save_albums()
            print(f"Album '{album_name}' supprimé avec succès.")
        else:
            print("Cet album n'existe pas.")
            
    def display_albums(self):
        if self.albums:
            print("\nListe des albums :")
            for album in self.albums:
                print(album)
        else:
            print("Aucun album trouvé.")
