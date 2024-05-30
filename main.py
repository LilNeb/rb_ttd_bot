import ocr
import screenshot

windowName = 'Roblox'
repoPath = '/Users/nicolasm./Documents/GitHub/rb_ttd_bot/screenshots'
screenshot.takeScreenshotAndSave(windowName, repoPath)

#process image and crop it to only show the text
#here

file_path = '/Users/nicolasm./Documents/GitHub/rb_ttd_bot/screenshots/text.png'
text = ocr.ocr_file(file_path)
print(text)