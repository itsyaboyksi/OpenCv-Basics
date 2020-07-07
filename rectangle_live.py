import cv2
import numpy as np

drawing = False # true if mouse is pressed
mode = False # if True, draw rectangle.
pt1 = (0,0)
pt2 = (0,0)
# mouse callback function
def draw_circle(event,x,y,flags,param):
  global pt1, pt2, drawing, mode

  if event == cv2.EVENT_LBUTTONDOWN:
      drawing = False
      pt2 = x,y
      pt1 = x,y
  elif event == cv2.EVENT_MOUSEMOVE:
      if drawing == False:
          if mode == True:
              a=x
              b=y
              if a != x | b != y:
                  pt2 = (x,y)
                
  elif event == cv2.EVENT_LBUTTONUP:
      drawing = True
      mode = True
      pt2 = x,y

#img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # Based on the Global Variables Draw the Frame
    # Draw a Circle on the Frame
    if mode == True:
        cv2.rectangle(frame,pt1,pt2,(0,255,0),3) #setting thickness to -1 will make a filled circle
    
    # Show the Frame
    cv2.imshow('image', frame)
    
    # 27 == esc button. You can use any other button like ord('q')
    # If you try to close the window pressing the x you'll get in trouble (^_^)
    if cv2.waitKey(15) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()   
