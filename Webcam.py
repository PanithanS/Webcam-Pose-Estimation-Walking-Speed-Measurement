import cv2
from datetime import datetime

class Webcam:

    def __init__(self, add, h, w):
        
        # Initialize the Webcam
        self.address= add
        self.height = h #y
        self.width = w #x
        self.cap = cv2.VideoCapture(self.address)
        self.cap.set(3, self.width)
        self.cap.set(4, self.height)
        success_, _ = self.cap.read()
        self.started_time = ""
        self.ended_time = ""
        try:
            self.active = success_ #True if read success
        except:
            self.active = False

        self.cam_name = 'Webcam'+"-" +str(self.address)
        self.key = None

        #Mouse position x,y
        self.mouse_y = 0
        self.mouse_x = 0
        
        # drawing
        self.drawing = False
        self.draw_count = 0

        try:
            with open("SpeedCap\start_box.txt", 'r') as file:
                self.start_x1, self.start_y1, self.start_x2, self.start_y2 = map(int,(file.readlines(0))[0].split(","))
            self.draw_count = self.draw_count + 1
        except:
            #The start box (x, y), which we will draw later
            self.start_x1, self.start_y1 = 0, 0
            self.start_x2, self.start_y2 = 0, 0

        try:
            with open("SpeedCap\end_box.txt", 'r') as file:
                self.end_x1, self.end_y1, self.end_x2, self.end_y2 = map(int,(file.readlines(0))[0].split(","))
            self.draw_count = self.draw_count + 1
        except:
            #The end box (x, y), which we will draw later
            self.end_x1, self.end_y1 = 0, 0
            self.end_x2, self.end_y2 = 0, 0

    def killcam(self):
        """
        function to close the webcam window, and release the webcam
        """
        try:
            cv2.destroyWindow(self.cam_name) #In some versions of openCV, this gives an error
        except:
            self.key = 27 #Equivalent to pushing the 'ESC' button on keyboard
        self.active = False
        self.cap.release()
    
    def is_quit(self):
        """
        function to check if the user tries to close the webcam window
        """
        if self.key==27: # key =27 is the ESC key
            self.killcam() # kill this Webcam
        elif cv2.getWindowProperty(self.cam_name, cv2.WND_PROP_VISIBLE) < 1: # cv2.WND_PROP_VISIBLE = 0 when the user clicks on "X" of the Webcam window
            self.killcam() # kill this Webcam
    
    def mouse_and_keys(self, event, x, y, flags, param):
        """
        function to get a mouse event in the webcam window
        """
        
        # getmouse position
        if event == cv2.EVENT_MOUSEMOVE:
            self.mouse_y = y
            self.mouse_x = x

        elif event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.y1_draw = y 
            self.x1_draw = x

            if self.draw_count%2 == 0: #True if we are drawing the 'start point'
                self.start_y1 = self.y1_draw 
                self.start_x1 = self.x1_draw
            else: #Ortherwise, we are drawing the 'end point'
                self.end_y1 = self.y1_draw 
                self.end_x1 = self.x1_draw
                
        elif event == cv2.EVENT_LBUTTONUP: # When we finish pointer dragging
            self.y2_draw = y
            self.x2_draw = x
            
            if self.draw_count%2 == 0: #True if we are drawing the 'start point'
                self.start_y2 = self.y2_draw 
                self.start_x2 = self.x2_draw
                
                #Then save these points as "start_box.txt"
                with open("SpeedCap\start_box.txt", "w+") as file:
                    file.write( str(self.start_x1) + "," + str(self.start_y1) + "," + str(self.start_x2) + "," + str(self.start_y2))

            else: #Ortherwise, we are drawing the 'end point'
                self.end_y2 = self.y2_draw 
                self.end_x2 = self.x2_draw

                #Then save these points as "end_box.txt"
                with open("SpeedCap\end_box.txt", "w+") as file:
                    file.write( str(self.end_x1) + "," + str(self.end_y1) + "," + str(self.end_x2) + "," + str(self.end_y2))

            self.drawing = False
            self.draw_count = self.draw_count+1

    def display(self, img, delay = 10, see_clock =True):
        
        """Pop-up a window to display the program.

        Args:
        img: an image
        waittime (ms): delay time waiting for any keys press, also works as a delay between images to be displayed
        display_time: overlay clock on the top-left of the image in "%H:%M:%S" form
        
        Returns:
        The display window

        Raises:
        None

        """

        # Get current local time
        self.local_time = datetime.now()
        # Format the time in 24-hour clock format
        self.formatted_time =  self.local_time.strftime("%H:%M:%S")
        
        if see_clock:
            cv2.putText(img, str(self.formatted_time), (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 128, 128), 1)

        #display mouse position (x,y)
        cv2.putText(img, "y,x: " + str(self.mouse_x) +","+ str(self.mouse_y), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 128, 128), 1)

        #display time start/stop time detected
        cv2.putText(img, "START: " + str(self.started_time), (5, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 128, 128), 1)
        cv2.putText(img, "END: " + str(self.ended_time), (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 128, 128), 1)

        # Need to draw the estimate bounding box for starting and ending points 
        if self.drawing:
            #tempolary show the drawing box
            cv2.rectangle(img, (self.x1_draw, self.y1_draw),(self.mouse_x, self.mouse_y),(0, 0, 0), 1)
        
        if self.draw_count > 0: # already draw something

            if self.drawing == False:
                # show the start point
                cv2.rectangle(img, (self.start_x1, self.start_y1),(self.start_x2, self.start_y2),(76, 187, 23), 2)
                cv2.putText(img, str("START"), (self.start_x1, self.start_y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (76, 187, 23), 2)

                # show the end point
                cv2.rectangle(img, (self.end_x1, self.end_y1),(self.end_x2, self.end_y2),(255, 49, 49), 2)
                cv2.putText(img, str("END"), (self.end_x1, self.end_y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 49, 49), 2)

            else: # when we are drawing
                if self.draw_count%2 == 0: #True if we are drawing the 'start point'
                    # show the end box while we draw the start box 
                    cv2.rectangle(img, (self.end_x1, self.end_y1),(self.end_x2, self.end_y2),(255, 49, 49), 2)
                    cv2.putText(img, str("END"), (self.end_x1, self.end_y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 49, 49), 2)

                else: #Ortherwise, we are drawing the 'end point'
                    # show the start point while we draw the end box 
                    cv2.rectangle(img, (self.start_x1, self.start_y1),(self.start_x2, self.start_y2),(76, 187, 23), 2)
                    cv2.putText(img, str("START"), (self.start_x1, self.start_y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (76, 187, 23), 2)

        # Webcam Output 
        cv2.imshow(self.cam_name, img)
        cv2.setMouseCallback(self.cam_name, self.mouse_and_keys)
        
        self.key = cv2.waitKey(delay)
        
        self.is_quit() #if 'ESC' or 'click X' on window

        self.sbb = [self.start_x1,self.start_y1,self.start_x2,self.start_y2] #starting bounding box
        self.ebb = [self.end_x1,self.end_y1,self.end_x2,self.end_y2] #ending bounding box

        return self.sbb, self.ebb
