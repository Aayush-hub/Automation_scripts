import keyboard                          # pip install keyboard
from PIL import Image, ImageGrab         # pip install pillow
import time

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(250, 300):
        for j in range(250, 360):
            if data[i, j] < 100:
                keyboard.press("down")
                return
    # Draw the rectangle for cactus
    for i in range(330, 430):
        for j in range(400, 470):
            if data[i, j] < 100:
                keyboard.press("up")
                return
    return

if __name__ == "__main__":
    print("Dino game about to start in 2 seconds")
    time.sleep(2) 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
        
        '''
        Code for testing co-ordinates
        
        # Draw the rectangle for cactus
        for i in range(200, 300):
            for j in range(390, 450):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 150

        image.show()
        break
        '''
