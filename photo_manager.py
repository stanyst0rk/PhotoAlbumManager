# photo_manager.py
import os

class PhotoManager:
    def __init__(self):
        self.photos_dir = "data/photos/"
        self.load_photos()

    def load_photos(self):
        self.photos = {}
        albums = os.listdir(self.photos_dir)
        for album in albums:
            album_path = os.path.join(self.photos_dir, album)
            if os.path.isdir(album_path):
                photos = os.listdir(album_path)
                self.photos[album] = photos

    def add_photo(self, album_name, photo_path):
        if album_name in self.photos:
            album_path = os.path.join(self.photos_dir, album_name)
            os.makedirs(album_path, exist_ok=True)
            photo_name = os.path.basename(photo_path)
            new_photo_path = os.path.join(album_path, photo_name)
            os.replace(photo_path, new_photo_path)
            self.load_photos()
            print(f"Photo ajoutée à l'album '{album_name}' avec succès.")
        else:
            print(f"L'album '{album_name}' n'existe pas.")

    def delete_photo(self, album_name, photo_name):
        if album_name in self.photos and photo_name in self.photos[album_name]:
            photo_path = os.path.join(self.photos_dir, album_name, photo_name)
            os.remove(photo_path)
            self.load_photos()
            print(f"Photo '{photo_name}' supprimée de l'album '{album_name}' avec succès.")
        else:
            print(f"La photo '{photo_name}' ou l'album '{album_name}' n'existe pas.")

    def display_photos(self, album_name):
        if album_name in self.photos:
            photos = self.photos[album_name]
            if photos:
                print(f"\nPhotos de l'album '{album_name}' :")
                for photo in photos:
                    print(photo)
            else:
                print(f"Aucune photo dans l'album '{album_name}'.")
        else:
            print(f"L'album '{album_name}' n'existe pas.")
