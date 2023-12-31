import pyautogui
import cv2
import numpy as np
import os
import datetime
import json
import pytesseract
from PIL import Image
from controller import Controller as cr
from img_edit import IMG_Edit as img_e


pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

PATH_COLLECTION = 'collected_images'

USE_PREV = True

def main():
    
    # # Before running activate the window
    # cr.activate_window("Tabletop Simulator") 

    # # # take screenshot of board
    # # To save time I am saving these values 
    
    # search = capture(board)
    # cords = locate('shop.png', search)

    with open('mac_cords.json', 'r') as file:
        all_cords = json.load(file)

    shop_cords = all_cords["shop"]
    shop_img = "collected_images/shop_captures/shop_2023-11-29_11-31-03.png"
    
    ##### TO-DO
    ## have a control loop that waits for button presses to do ceratin actions 

    if not USE_PREV:
        # # go to cords and take screen shot 
        pyautogui.moveTo(shop_cords[0], shop_cords[1])
        cr.zoom()
        shop_img = capture("shop")
        pyautogui.press('space')

    ## Within shop there is 3 crew and six shipparts, 
    ## These cards will be the same everytime so we will save them for this max

    # # Locate the crew img in the shop 
    
    # crew_cords = locate_img('cards/crew_green.png',shop_img)
    # print(crew_cords)
    crew_cords = all_cords["crew"]
    
    shop_img = cv2.imread(shop_img)

  
    cropped_crew = crop_crew(shop_img,crew_cords)

    crop_crew_features(cropped_crew, all_cords["crew_features"])

    # once we store all the cords we will then use our ml model 
    # to get the text from the image by cropping specific sections

    # get all the values and save them to the shop OBJ

    # #   contracts
    # Repeat the same as above but for contracts
    
    # #  hand/shipparts
    # repeat the same but for getting player info

    return

def crop_crew(shop_img,crew_cords):
    print(crew_cords)
    cropped_crew = []
    for index,c_cords in enumerate(crew_cords):

        crew = "collected_images/cropped_imgs/crew_{}.png".format(index)
        cropped_crew.append(img_e.crop(shop_img, crew, c_cords[0],c_cords[1]))

    return cropped_crew


def crop_crew_features(crews,cords):

    for index,crew in enumerate(crews):
        crew = cv2.imread(crew)
        features = "collected_images/features/"

        name = "{}name_crew_{}.png".format(features,index)
        ability = "{}ability_crew_{}.png".format(features,index)
        cost = "{}cost_crew_{}.png".format(features,index)
        
        img_e.crop(crew, name, cords['name'][0],cords['name'][1])
        img_e.crop(crew, ability, cords["cost"][0],cords["cost"][1])
        img_e.crop(crew, cost, cords["card_ability"][0],cords["card_ability"][1])


def capture(name): 
    
    cr.activate_window("Tabletop Simulator") 

    pyautogui.moveTo(0.0)
    board = pyautogui.screenshot()
   
    filename = name +"_"+ datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
   
    folder_path = name+"_captures"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    full_path = os.path.join(folder_path, filename)
    board.save(full_path)

    return full_path

def locate_img(area, search):

    # Load images
    main_image = cv2.imread(search)
    locate = cv2.imread(area)

    ## Locate image in the img both grey scale
    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    locate_gray = cv2.cvtColor(locate, cv2.COLOR_BGR2GRAY)

    main_edges = cv2.Canny(main_gray, 50, 200)
    template_edges = cv2.Canny(locate_gray, 50, 200)

    res = cv2.matchTemplate(main_edges, template_edges, cv2.TM_CCOEFF_NORMED)

    threshold = 0.2
    locations = np.where(res >= threshold)
    scores = res[locations]
    rectangles = []

    for loc, score in zip(zip(*locations[::-1]), scores):
        rect = [int(loc[0]), int(loc[1]), int(loc[0] + locate.shape[1]), int(loc[1] + locate.shape[0])]
        rectangles.append(rect)

    rectangles = np.array(rectangles)
   
    keep = rectangles
    if len(rectangles) > 1:
        keep = non_max_suppression(rectangles, scores, 0.3)  # Adjust the threshold as needed

    coordinates = []

    for idx in keep:
        top_left = (rectangles[idx][0], rectangles[idx][1])
        bottom_right = (rectangles[idx][2], rectangles[idx][3])

        # Draw a rectangle around the matched area
        cv2.rectangle(main_image, top_left, bottom_right, (0, 255, 0), 2)

        # Calculate the center of the rectangle
        # center = [((top_left[0] + bottom_right[0]) / 2) * 0.5, ((top_left[1] + bottom_right[1]) / 2) * 0.5]
        coordinates.append([top_left,bottom_right])

    # Display the result
    cv2.imshow('Detected', main_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return coordinates

def non_max_suppression(boxes, scores, threshold):
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    areas = (x2 - x1) * (y2 - y1)
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0.0, xx2 - xx1)
        h = np.maximum(0.0, yy2 - yy1)
        overlap = (w * h) / areas[order[1:]]

        inds = np.where(overlap <= threshold)[0]
        order = order[inds + 1]

    return keep

def img_to_text(img):
    text = pytesseract.image_to_string(img, lang='eng')

    img = Image.open(img)
    gray_img = img.convert('L')

    print(pytesseract.image_to_string(gray_img, config='--psm 6'))
    print("s",text)


if __name__ == "__main__":
    main()