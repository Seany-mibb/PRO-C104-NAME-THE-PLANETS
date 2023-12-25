import cv2
img = cv2.imread("solar-system.jpg")
#Sun
cv2.putText(img,
            "Sun",
            (20, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

#Mercury
cv2.putText(img,
            "Mercury",
            (110, 230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

#Venus
cv2.putText(img,
            "Venus",
            (190, 230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

#Earth
cv2.putText(img,
            "Earth",
            (288, 230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

#Mars
cv2.putText(img,
            "Mars",
            (388, 230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

#Jupiter
cv2.putText(img,
            "Jupiter",
            (500, 230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 0)
            )

#Saturn
cv2.putText(img,
            "Saturn",
            (775, 230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 0)
            )

#Uranus
cv2.putText(img,
            "Uranus",
            (960, 230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 0, 0)
            )

#Neptune
cv2.putText(img,
            "Neptune",
            (1110, 230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.imshow("output", img)
cv2.waitKey(4000)