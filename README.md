# BILL_DATE_OCR
We receive a lot of bills and sometimes we forget when we received a particular bill and what bill. The BILL_DATE_OCR does the same by extracting the date from the fill but automated. The full api implementation is yet to come, but with the help of given python notebooks, util files etc it performs the task.

We were able to extract the dates from the text as the dates are always in either XX.XX.XXXX or XX.XX.XX or XX/XX/XXXX or XX/XX/XX formats.

# ORIGINAL IMAGE:
https://user-images.githubusercontent.com/26826339/68999855-9dbdff00-08ec-11ea-988a-4ba805c31a06.jpeg

The original image can be small, folded, can have low resolution etc. To handle such problems we made use of:

# 1): RESCALING
https://user-images.githubusercontent.com/26826339/68999850-9d256880-08ec-11ea-9494-0bfaf920e43d.png

After rescaling the image which is loaded in grayscale, the image is binarized and the foregroud text and background were made distinct.

# 2: THRESHOLDING AND BINARIZING:

# 2.1) IMAGE USING NORMAL BINARY_THRESHOLDING:
https://user-images.githubusercontent.com/26826339/68999852-9d256880-08ec-11ea-8361-0299266c1b2e.png

After normal binary thresholding, we extracted the text and then separated the date from it using reg exps.

# 2.2) IMAGE USING ADAPTIVE THRESHOLDING:
https://user-images.githubusercontent.com/26826339/68999853-9dbdff00-08ec-11ea-96b3-6f1946dfdaa7.png

The adaptive thresholding can give better results, as it can adapts the suitable max val for thresholding. Thus it can remove much noise. 

# 3) EXTRACTING TEXT FROM THRESHOLDED IMAGES:
https://user-images.githubusercontent.com/26826339/68999854-9dbdff00-08ec-11ea-84c1-f5790d42f47a.png


From the extracted text, we then used reg expressions to extract the date. We made use of a feature that date will always be present in either XX.XX.XXXX or XX.XX.XX or XX/XX/XXXX or XX/XX/XX.

