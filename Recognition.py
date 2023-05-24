import cv2
import numpy as np


def recog(Aksh_img,Akshtrain_img):
    # Aksh_img = cv2.imread('Image/Aksh.jpg')
    # Akshtrain_img = cv2.imread('Image/Akshtrain.jpg')

    # Convert it to grayscale
    # Aksh_img_bw = cv2.cvtColor(Aksh_img, cv2.COLOR_BGR2GRAY)
    # Akshtrain_img_bw = cv2.cvtColor(Akshtrain_img, cv2.COLOR_BGR2GRAY)

    Aksh_img_bw = Aksh_img
    Akshtrain_img_bw = Akshtrain_img

    # Initialize the ORB detector algorithm
    orb = cv2.ORB_create()

    queryKeypoints, queryDescriptors = orb.detectAndCompute(Aksh_img_bw, None)
    trainKeypoints, trainDescriptors = orb.detectAndCompute(Akshtrain_img_bw, None)

    # Initialize the Matcher for matching
    # the keypoints and then match the
    # keypoints
    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(queryDescriptors, trainDescriptors,k=2)

    good =[]

    for m, n in matches:
        if m.distance < 0.90 * n.distance:
            good.append([m])
    img3 = cv2.drawMatchesKnn(Aksh_img, queryKeypoints, Akshtrain_img, trainKeypoints, good, None, flags=2)
    print(len(good))
    #
    # img3 = cv2.drawMatchesKnn(img1,kp1,img2Croppped,kp2,good,None,flags=2)

    imgKp1 = cv2.drawKeypoints(Aksh_img,queryKeypoints,None)
    imgKp2 = cv2.drawKeypoints(Akshtrain_img,trainKeypoints,None)
    cv2.imshow("kp1", imgKp1)
    cv2.imshow("kp2", imgKp2)
    return img3



img1 = cv2.imread("Image/Aksh.jpg", 0)
img2 = cv2.imread("Image/Akshtrain.jpg", 0)
img4 = cv2.imread("Image/Aksh.jpg")

img1 = cv2.resize(img1,(1080,720))
img2 = cv2.resize(img2,(1080,720))

Height = img2.shape[0]
Width = img2.shape[1]
# img2Croppped = img2[int(Height / 2):Height - 100, int(Width - Width / 3):Width]

# print(recog(img1, img2Croppped))
# print(recog(img4, img2Croppped))


# cv2.imshow("kp1",imgKp1)
# cv2.imshow("kp2",imgKp2)
# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2Croppped)
# cv2.imshow("img3", img4)
cv2.imshow("img4", recog(img1, img2))
cv2.imshow("img5", recog(img2, img1))
# cv2.imshow("img3",img3)
cv2.waitKey(0)
