import cv2
vidcap = cv2.VideoCapture('20190312_180601.mp4')
success,image = vidcap.read()
count = 0
#outPath ="C:\\Users\\Maabul Quddus\\Documents\\Co Curricular\\Python Projects\\Spyder\\Out"
while success:
  cv2.imwrite("frame%d.jpg" % count, image,0)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1