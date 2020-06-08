# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:21:18 2019

@author: Maabul Quddus
"""
import os
import cv2
import numpy as np


def main():
#    img=np.zeros((512,512,3),np.uint8)
#    cv2.line(img,(0,99),(200,0),(255,0,0),2)
#    cv2.rectangle(img,(440,60),(80,70),(0,255,0),2)
#    cv2.circle(img,(100,100),30,(0,255,0),-1)
#    cv2.ellipse(img,(300,300),(50,20),0,0,360,(0,255,0),-1)
#    
#    points=np.array([[80,2],[125,40],[179,19],[230,5],[30,50]],np.int32)
#    points=points.reshape(-1,1,2)
#    cv2.polylines(img,[points],True,(0,255,255))
#    Text1='Test Text'
#    cv2.putText(img,Text1,(100,300),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,0))
    imgpath="C:\\Users\\Maabul Quddus\\Documents\\Co Curricular\\Python Projects\\Spyder\\DataSets\\4.2.07.tiff"
    
    img=cv2.imread(imgpath,0)
    print(img)
    print(img.dtype)
    print(img.shape)
    print(img.ndim)
    print(img.size)
#    
#    cv2.namedWindow('Black',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Vegies',img)
    cv2.waitKey(0)
    cv2.destroyWindow('Vegies')
    

if __name__=="__main__":
    main()    