import cv2
import numpy as np

# فتح الكاميرا الأساسية للكمبيوتر
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # تحويل الصورة إلى تدرج اللون HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # تحديد نطاق اللون الأزرق
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)

    # استخراج اللون من الصورة الأصلية
    result = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # عرض النافذة
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Color Recognition (Blue)", result)

    # الخروج عند الضغط على زر 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()