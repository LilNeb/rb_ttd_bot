import cv2
import os
import utils

coordinate_sets = utils.coordinate_sets

# Coordinates sets

def crop_image_with_coordinates(image_path, coordinates_name):
    # Extraire les coordonnées du dictionnaire
    coordinates = coordinate_sets[coordinates_name]
    
    # Charger l'image
    image = cv2.imread(image_path)

    # Obtenir les dimensions de l'image
    height, width, _ = image.shape

    # Convertir les coordonnées relatives en coordonnées réelles
    x = int(coordinates['x_rel'] * width)
    y = int(coordinates['y_rel'] * height)
    w = int(coordinates['w_rel'] * width)
    h = int(coordinates['h_rel'] * height)

    # Recadrer l'image
    crop_image = image[y:y+h, x:x+w]

    # Sauvegarder l'image recadrée
    cropped_image_path = os.path.splitext(image_path)[0] + f"_{coordinates_name}_cropped.png"
    cv2.imwrite(cropped_image_path, crop_image)

    # Retourner le chemin de l'image recadrée
    return cropped_image_path

# Exemple d'utilisation
# image_path = r"/Users/nicolasm./Documents/GitHub/rb_ttd_bot/screenshots/Roblox_1717076914.png"
# cropped_image_path = crop_image_with_coordinates(image_path, 'lobby_menus')
# print("Cropped image saved at:", cropped_image_path)

# cropped_image_path = crop_image_with_coordinates(image_path, 'start_button')
# print("Cropped image saved at:", cropped_image_path)
