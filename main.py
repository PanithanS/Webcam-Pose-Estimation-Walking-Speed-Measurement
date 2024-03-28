from Webcam import Webcam
from PoseModel import PoseModel
import sys
import cv2
import numpy as np 
import time
def is_in_box(box_fix, box_pred, threshold):

    # Mean Squared Error 
    MSE = np.square(np.abs(np.subtract(box_pred,box_fix))).mean()

    #threshold needs to be optimized
    return MSE, MSE < threshold

def main(vid=None, address=0, height = 720, width = 1280, threshold = 300, rotate=False):
    
    if vid == None:
        #This version only supports single webcam
        webcam_0 = Webcam(add=address, h = height, w = width) # webcam address 0, height = 720, width = 1280
        yolo = PoseModel(model_weight = 'yolo-Weights/yolov8n-pose.pt')
        
        started = False
        ended = False

        while webcam_0.active:

            #print(started, ended)

            #Images stream from Webcam_0
            _, frame = webcam_0.cap.read()

            #if the camera rotated
            if rotate:
                frame=cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            else:
                pass
            
            # YOLO model to get prediction
            results = yolo.model.predict(frame, stream=True, conf = 0.6, verbose=False) #predicted by YOLO

            img, pred_boxes = yolo.overlay_results(frame, results)

            # We pass the predicted to display on the webcam
            start_box, end_box = webcam_0.display(img, delay = 10, see_clock= True)

            if started == False:
                for pred_box in pred_boxes:

                    # If any pred box is in the start box it will return (_, True)
                    mse_start, started = is_in_box(box_fix=start_box, box_pred=pred_box, threshold = threshold)
                    print("mse start: " + str(mse_start) + str(", started: ") + str(started))
                    if started:
                        started_time = webcam_0.formatted_time
                        webcam_0.started_time = started_time

            elif started == True and ended == False: #person already pass start box
                for pred_box in pred_boxes:
                    # If any pred box is in the end box it will return (_, True)
                    mse_end, ended = is_in_box(box_fix=end_box, box_pred=pred_box, threshold = threshold)
                    print("mse start: " + str(mse_start) + str(", started: ") + str(started))
                    print("mse end: " + str(mse_end) + str(", ended: ") + str(ended))
                    if ended:
                        ended_time = webcam_0.formatted_time
                        webcam_0.ended_time = ended_time

            if started == True and ended == True:
                print("start-time, end-time" + str(started_time) +", "+ str(ended_time))
                
                #Last-Display
                start_box, end_box = webcam_0.display(img, delay = 10, see_clock= True)
                
                time.sleep(20)
                
                #input("Press Enter to continue...")
                # Then we restart the while loop
                started = False
                ended = False

        sys.exit("")

    else:
        sys.exit("This version not support video")

if __name__ == "__main__":
    main()
