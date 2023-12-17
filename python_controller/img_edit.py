import cv2

class IMG_Edit:
    def __init__(self):
        pass

    def crop(image,name, top_l,bot_r): 
        cropped_image = image[top_l[1]:bot_r[1], top_l[0]:bot_r[0]]
        # Save the cropped image
        cv2.imwrite(name, cropped_image)
        return name

    def scale(image_path, new_name, scale):
        # Load the image
        image = cv2.imread(image_path)

        # Define the scale down size
        # You can set these values according to the size you want
        scale = 30  # percentage of original size

        # Calculate the new dimensions
        width = int(image.shape[1] * scale / 100)
        height = int(image.shape[0] * scale / 100)
        dim = (width, height)

        # Resize the image
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        # Save the resized image
        cv2.imwrite(new_name, resized)

    def to_grey(image_path, new_name):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(new_name, image)

    def blur(image_path, new_name):
        image = cv2.imread(image_path)
        image = cv2.GaussianBlur(image, (5, 5), 0)
        cv2.imwrite(new_name, image)
