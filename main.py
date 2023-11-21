# main.py
from album_manager import AlbumManager
from photo_manager import PhotoManager

def main():
    album_manager = AlbumManager()
    photo_manager = PhotoManager()

    while True:
        print("\n===== Photo Album Manager =====")
        print("1. Créer un nouvel album")
        print("2. Ajouter une photo à un album")
        print("3. Afficher la liste des albums")
        print("4. Afficher les photos d'un album")
        print("5. Supprimer un album")
        print("6. Supprimer une photo d'un album")
        print("0. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            album_name = input("Nom de l'album : ")
            album_manager.create_album(album_name)
        elif choice == "2":
            album_name = input("Nom de l'album : ")
            photo_path = input("Chemin de la photo : ")
            photo_manager.add_photo(album_name, photo_path)
        elif choice == "3":
            album_manager.display_albums()
        elif choice == "4":
            album_name = input("Nom de l'album : ")
            photo_manager.display_photos(album_name)
        elif choice == "5":
            album_name = input("Nom de l'album : ")
            album_manager.delete_album(album_name)
        elif choice == "6":
            album_name = input("Nom de l'album : ")
            photo_name = input("Nom de la photo : ")
            photo_manager.delete_photo(album_name, photo_name)
        elif choice == "0":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
