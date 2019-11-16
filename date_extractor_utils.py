#!/usr/bin/env python
# coding: utf-8



import cv2 as cv
import numpy as np
import re
import pytesseract

def resize_incr(photo,percentage_incr):
    percentage_incr=percentage_incr+100
    photo=cv.resize(photo,(photo.shape[0]*percentage_incr//100,photo.shape[1]*percentage_incr//100))
    return photo



def predictions(image_path,resize_percentage_incr=20,starting_thresh_val=40):
    predictions_list=[]
    photo = cv.imread(image_path,0)
    photo=resize_incr(photo,resize_percentage_incr)
    pattern="([0-9]{1,2}\/[0-9]{2}\/[0-9]{2,4})|([0-9]{1,2}\.[0-9]{2}\.[0-9]{2,4})"
    
    ###FOR NORMAL BINARY THRESHING
    ###FOR NORMAL BINARY THRESHING, WE ARE KEEPING THRESHING MAX_VAL AS A HYPERPARAMETER 
    
    for i in range(starting_thresh_val,90,5):
        thresh1 = cv.threshold(photo,int(255*i)//100,255,cv.THRESH_BINARY)[1]
        text=pytesseract.image_to_string(thresh1)
        l=re.findall(pattern,text,)
  
        if isinstance(l, type(None)):
            continue
            
        date_list=[[x for x in y if len(x)!=0] for y in l]
        print("thresh_list{}".format(date_list))
        
        if len(date_list)!=0:
            for i in range(len(date_list)):
                predictions_list.append(str(date_list[i][0]))
        
              
    ###FOR ADAPTIVE GAUSSIAN THRESHING
    ### FOR ADAPTING GAUSSIAN THRESHING WE ARE KEEPING BLOCK SIZE AS A HYPERPARAMETER
    
    for i in range(11,31,4):
        th3 = cv.adaptiveThreshold(photo,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,i,10)
        text=pytesseract.image_to_string(th3)
        l=re.findall(pattern,text,)
        
        if isinstance(l, type(None)):
            continue
        
        date_list=[[x for x in y if len(x)!=0] for y in l]
        print("adaptive_thresh_list{}".format(date_list))
              
        if len(date_list)!=0:
            for i in range(len(date_list)):
                predictions_list.append(str(date_list[i][0]))
        
    
    del photo
    print("DATES: {}".format(predictions_list))
    ###RETURNING MOST OCCURED OR PREDICTED DATE
    if len(predictions_list)==0:
        return "CAN'T FIND DATE OR THE PHOTO IS NOT CLEAR"
    res=np.unique(predictions_list,return_counts=True,)
    index=np.argmax(res[1])
    res[0][index]
    return res[0][index]






