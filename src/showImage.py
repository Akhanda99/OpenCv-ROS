#!/usr/bin/env python3
  
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

cap= cv2.VideoCapture(0)  
bridge=CvBridge()

def callback(imageData):
      
    
    rospy.loginfo("Image Data recieved")
    img=bridge.imgmsg_to_cv2(imageData,"bgr8")
    

    cv2.imshow('frame', img)
    cv2.waitKey(3)
  
def main():

    rospy.init_node('OpenCV_Image_Subscriber', anonymous=True)
    rospy.Subscriber("/camera1/image_raw", Image, callback)
    rospy.spin()
  
if __name__ == '__main__':
      
    # you could name this function
    try:
        main()
    except rospy.ROSInterruptException:
        pass