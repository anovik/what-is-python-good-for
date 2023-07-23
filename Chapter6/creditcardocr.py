from imutils import contours
import numpy as np
import imutils
import cv2

def getCountours(image):
	countours = cv2.findContours(image, cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
	countours = imutils.grab_contours(countours)
	countours = contours.sort_contours(countours, method="left-to-right")[0]
	return countours

# Step 1. Image preparation

image = cv2.imread("fake-credit-card.jpeg")
image = imutils.resize(image, width=300)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray.png',gray)

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

cv2.imwrite('tophat.png',tophat)

gradX = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0,
	ksize=-1)
gradX = np.absolute(gradX)
(minVal, maxVal) = (np.min(gradX), np.max(gradX))
gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
gradX = gradX.astype("uint8")

cv2.imwrite('gradX.png',gradX)

gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
thresh = cv2.threshold(gradX, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

squareKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, squareKernel)

cv2.imwrite('thresh.png',thresh)

# Step 2. Getting locations of digit groups

cnts = getCountours(thresh.copy())
locs = []

for (i, c) in enumerate(cnts):
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)
	if ar > 2.5 and ar < 4.0:	
		if (w > 40 and w < 55) and (h > 10 and h < 20):			
			locs.append((x, y, w, h))


locs = sorted(locs, key=lambda x:x[0])

# Step 3. Preparing OCR-A template digits for future comparison            
            
ocrA = cv2.imread("OCR-A_digits.jpg")
ocrA = cv2.cvtColor(ocrA, cv2.COLOR_BGR2GRAY)
ocrA = cv2.threshold(ocrA, 10, 255, cv2.THRESH_BINARY_INV)[1]

cv2.imwrite('ocrA.png',ocrA)

templateCountours = getCountours(ocrA.copy())

digits = {}

for (i, c) in enumerate(templateCountours):
	(x, y, w, h) = cv2.boundingRect(c)
	roi = ocrA[y:y + h, x:x + w]
	roi = cv2.resize(roi, (57, 88))
	digits[i] = roi

# Step 4. Match our countour locations with digit templates

output = []
for (i, (gX, gY, gW, gH)) in enumerate(locs):	
	groupOutput = []	
	group = gray[gY - 5 : gY + gH + 5, gX - 5 : gX + gW + 5 ]
	group = cv2.threshold(group, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]	
	digitCountours = getCountours(group.copy())
	
	for c in digitCountours:	
		(x, y, w, h) = cv2.boundingRect(c)
		roi = group[y:y + h, x:x + w]
		roi = cv2.resize(roi, (57, 88))	
		scores = []
		for (digit, digitROI) in digits.items():		
			result = cv2.matchTemplate(roi, digitROI,
				cv2.TM_CCOEFF)
			(_, score, _, _) = cv2.minMaxLoc(result)
			scores.append(score)		
		groupOutput.append(str(np.argmax(scores)))
		
	cv2.rectangle(image, (gX - 5, gY - 5), (gX + gW + 5, gY + gH + 5), (0, 0, 255), 2)
	cv2.putText(image, "".join(groupOutput), (gX, gY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)             
	
	output.extend(groupOutput)


print("Credit Card #: {}".format("".join(output)))
cv2.imshow("Image", image)
cv2.waitKey(0)