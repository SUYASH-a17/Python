import cv2, pandas
from datetime import datetime
first_frame = None
status_list = [None,None]
time_list = []
df = pandas.DataFrame(columns=['Start', 'End'])


video = cv2.VideoCapture(0)     # video capture object, will capture the video

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 'contours' holds the list of contours found in your image

    for contour in contours:
        if cv2.contourArea(contour) < 20000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0:
        time_list.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        time_list.append(datetime.now())

    cv2.imshow('Capture', gray)
    cv2.imshow('delta frame', delta_frame)
    cv2.imshow('Threshold Frame', thresh_frame)
    cv2.imshow('Color Frame', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            time_list.append(datetime.now())
        break
print(status_list)
print(time_list)

for i in range(0, len(time_list), 2):
    new_row = pandas.DataFrame({'Start': [time_list[i]], 'End': [time_list[i+1]]})
df = pandas.concat([df, new_row], ignore_index=True)
df.to_excel('txt_fl/Times.xlsx')

video.release()
cv2.destroyAllWindows