import cv2

def crop_image_with_coordinates(image_path, coordinates):
    # Load the image
    image = cv2.imread(image_path)

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Convert relative coordinates to actual coordinates
    x = int(coordinates['x_rel'] * width)
    y = int(coordinates['y_rel'] * height)
    w = int(coordinates['w_rel'] * width)
    h = int(coordinates['h_rel'] * height)

    # Crop the image
    crop_image = image[y:y+h, x:x+w]

    # Display the cropped image
    cv2.imshow("Cropped", crop_image)
    cv2.waitKey(0)

# Example usage
lobby_menus = {
    'x_rel': 0,    # relative x start point (0 means start of image)
    'y_rel': 1/3,  # relative y start point (1/3 means 1/3rd of image height)
    'w_rel': 1/10,  # relative width (1/7 means 1/7th of image width)
    'h_rel': 1/3   # relative height (1/3 means 1/3rd of image height)
}

image_path = r"/Users/nicolasm./Documents/GitHub/rb_ttd_bot/screenshots/Roblox_1717069284.png"
crop_image_with_coordinates(image_path, lobby_menus)
