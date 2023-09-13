import cv2
image = cv2.imread('data/img.png')

cv2.imshow('Image', image)


key = cv2.waitKey(0) # 키 이벤트 대기

if key == ord('s') :
    cv2.imwrite('data/save_img.png', image)
    print("저장 성공")

cv2.destroyAllWindows() #열린 모든 윈도우 제거