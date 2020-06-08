import cv2
img1="C:\\Users\\Maabul Quddus\\Documents\\Co Curricular\\Python Projects\\Spyder\\DataSets\\4.2.07.tiff"
img = cv2.imread("img1")
crop_img = img[93:93+1, 100:100+10]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)