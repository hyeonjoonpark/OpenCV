import cv2
image = cv2.imread('data/img.png')

cv2.imshow('Timed Display', image)
cv2.waitKey(3000) # 3초 동안 이미지 출력

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB',image_rgb)
cv2.waitKey(0)

# BGR 색 공간을 RGB로 변환하여 출력

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY', gray_image)
cv2.waitKey(0)

# 흑백 이미지 출력

cv2.destroyAllWindows() #열린 모든 윈도우 제거