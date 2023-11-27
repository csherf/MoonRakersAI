import pyautogui
import cv2
import numpy as np
import os
import datetime

def main():

    # take screenshot of board
    search = board_capture()
    # find key areas of board 
    locate('shop.png', search)


    #   shop
    #   contracts
    #   hand/shipparts

    return


def board_capture():
    activate_window("Tabletop Simulator")

    board = pyautogui.screenshot()
   
    filename = "board" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
   

    folder_path = "board_captures"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    full_path = os.path.join(folder_path, filename)
    board.save(full_path)

    return full_path

def locate(area, search):
 
    # Load images
    main_image = cv2.imread(search)
    locate = cv2.imread(area)


    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    locate_grey = cv2.cvtColor(locate, cv2.COLOR_BGR2GRAY)
    # Template matching
    # res = cv2.matchTemplate(main_image, locate, cv2.TM_CCOEFF)

    

    main_edges = cv2.Canny(main_gray, 50, 200)
    template_edges = cv2.Canny(locate_grey, 50, 200)


    

    res = cv2.matchTemplate(main_edges, template_edges, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    print(min_val,max_val, max_loc)

    threshold = 0.1 

    # Check if the maximum value exceeds the threshold
    if max_val < threshold:
        return
    
    # The top left of the matched area
    top_left = max_loc

    # Draw a rectangle around the matched area
    bottom_right = (top_left[0] + locate.shape[1], top_left[1] + locate.shape[0])
    cv2.rectangle(main_image, top_left, bottom_right, (0,255,0), 2)

    # Display the result
    cv2.imshow('Detected', main_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 

def activate_window(name):

    # Name of the window you want to focus on
    app_name = name

    # AppleScript command to activate the application
    script = f'''
    tell application "{app_name}"
        activate
    end tell
    '''

    # Run the AppleScript
    os.system(f"osascript -e '{script}'")


if __name__ == "__main__":
    main()