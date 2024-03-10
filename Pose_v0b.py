from ultralytics import YOLO
import cv2
import math 
import time

# start Webcam
#image_size 1920 × 1080 (FullHD)
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

model = YOLO('yolo-Weights/yolov8n-pose.pt')  # load a pretrained YOLOv8n pose model

#color for the key-points
KEYPOINT_EDGE_INDS_TO_COLOR = {
    (0, 1): (147, 20, 255),
    (0, 2): (255, 255, 0),
    (1, 3): (147, 20, 255),
    (2, 4): (255, 255, 0),
    (0, 5): (147, 20, 255),
    (0, 6): (255, 255, 0),
    (5, 7): (147, 20, 255),
    (7, 9): (147, 20, 255),
    (6, 8): (255, 255, 0),
    (8, 10): (255, 255, 0),
    (5, 6): (0, 255, 255),
    (5, 11): (147, 20, 255),
    (6, 12): (255, 255, 0),
    (11, 12): (0, 255, 255),
    (11, 13): (147, 20, 255),
    (13, 15): (147, 20, 255),
    (12, 14): (255, 255, 0),
    (14, 16): (255, 255, 0)
}


################ main ################
while True:
    # Webcam display
    success, img = cap.read()

    #Predicted by YOLO
    results = model.predict(img, stream=True, conf = 0.6, verbose=False) #predicted by YOLO


    for result in results:
        boxes = result.boxes
        keypoints = result.keypoints

        # Pose estimation display
        for kpt in keypoints.xy[0]:
            x, y = int(kpt[0]), int(kpt[1])
            
            if 0 in (x,y):
                pass
            else:
                cv2.circle(img, (x, y), radius=6, color=(0, 255, 0), thickness=-1)
                
        for edge, color in KEYPOINT_EDGE_INDS_TO_COLOR.items():
            point1_index, point2_index = edge
            try:
                x1, y1, = keypoints.xy[0][point1_index]
                x2, y2, = keypoints.xy[0][point2_index]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Draw the line on the image
                if 0 in (x1, y1, x2, y2):
                    pass
                else:
                    cv2.line(img, (x1, y1), (x2, y2), color, 2)
            except:
                pass
        

        # bounding box display
        for box in boxes:
            
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (0, 0, 255) #letters color
            thickness = 1
            cv2.putText(img, str(confidence), org, font, fontScale, color, thickness)

    # Time display
    local_time = time.ctime(time.time())
    cv2.putText(img, str(local_time), (5, 15), font, 0.5, (255, 255, 255), 1)

    #Output display
    cv2.imshow('Webcam', img)

    # break this while
    k = cv2.waitKey(33)
    if k==27:  # Esc key to stop
        break
    elif cv2.getWindowProperty('Webcam', cv2.WND_PROP_VISIBLE) < 1: #if click on "X"
        break

cap.release()
cv2.destroyAllWindows()
