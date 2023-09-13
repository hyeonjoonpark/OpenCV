import cv2

cap = cv2.VideoCapture('data/video.avi')

# 비티오 캡처 객체 생성
while cap.isOpened():  # 동영상이 남아있을 때 까지
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video', frame)  # 비디오 출력

    # q 를 눌렀을 때 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
