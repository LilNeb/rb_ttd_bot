import cv2
import os
import utils

# coordinate_sets = utils.coordinate_sets

coordinate_sets = {
    'lobby_menus': {
        'x_rel': 34/1000,    # relative x start point (0 means start of image)
        'y_rel': 40/100,  # relative y start point (1/3 means 1/3rd of image height)
        'w_rel': 6/100,  # relative width (1/7 means 1/7th of image width)
        'h_rel': 3/100   # relative height (1/3 means 1/3rd of image height)
    },
    'start_button': {
        'x_rel': 44/100,    # relative x start point (1/4 means 1/4th of image width)
        'y_rel': 665/1000,    # relative y start point (2/3 means 2/3rd of image height)
        'w_rel': 1/9,    # relative width (1/2 means half of image width)
        'h_rel': 1/10     # relative height (1/6 means 1/6th of image height)
    }
}

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

# crop image for all coordinates set and return a dictionary with the cropped images paths
def crop_image_for_all_coordinates_sets(image_path):
    cropped_images = {}
    for coordinates_name in coordinate_sets.keys():
        cropped_images[coordinates_name] = crop_image_with_coordinates(image_path, coordinates_name)
    return cropped_images

# Test
# print(crop_image_for_all_coordinates_sets('/Users/nicolasm./Documents/GitHub/rb_ttd_bot/screenshots/Roblox_1717109905.png'))
