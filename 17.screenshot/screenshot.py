import time
import pyautogui

def take_screenshot():
    """
    Takes a screenshot of the current screen after a delay.

    The screenshot is saved with a filename based on the current timestamp.
    The file is saved in PNG format and then displayed.
    """
    # Delay before taking the screenshot to allow for screen setup
    time.sleep(5)

    # Generating a unique filename using the current timestamp
    timestamp = int(round(time.time() * 1000))
    filename = f'{timestamp}.png'

    # Taking the screenshot
    screenshot_image = pyautogui.screenshot(filename)

    # Displaying the screenshot
    screenshot_image.show()

take_screenshot()
