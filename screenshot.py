from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll
import cv2 as cv
import numpy
from time import time
from PIL import Image
import os

def findWindowId(windowName):
    windowId = None

    print('searching window id')

    windowList = CGWindowListCopyWindowInfo(
        kCGWindowListOptionAll, kCGNullWindowID)

    for window in windowList:
        print(window.get('kCGWindowName', ''))
        if(windowName.lower() in window.get('kCGWindowName', '').lower()):
            windowId = window['kCGWindowNumber']
            print('found window id %s' % windowId)
            return windowId

    print('unable to find window id')
    return None


def takeScreenshotAndSave(windowName, repoPath):
    windowId = findWindowId(windowName)

    if windowId is None:
        return None

    imageFileName = 'test-img.png'
    # -x mutes sound and -l specifies windowId
    os.system('screencapture -x -l %s %s' % (windowId, imageFileName))
    img = Image.open(imageFileName)
    img = numpy.array(img)
    os.remove(imageFileName)

    # Save the image with a unique name in the specified repo path
    timestamp = int(time())
    savePath = os.path.join(repoPath, f'{windowName}_{timestamp}.png')
    cv.imwrite(savePath, img)

    print(f"Image saved at: {savePath}")  # Print the path of the saved image

    return savePath


loopTime = time()

# while(True):
#     screenshot = takeScreenshotAndSave('Roblox')

#     if screenshot is not None:
#         img = cv.imread(screenshot)
#         cv.imshow('cv', img)

#     # measure frames per second
#     print('FPS {}'.format(1 / (time() - loopTime)))
#     loopTime = time()

#     if cv.waitKey(1) == ord('q'):  # quit script when pressing 'q' key
#         cv.destroyAllWindows()
#         break

takeScreenshotAndSave('Roblox', './screenshots')

print('Done.')
