from darkflow.darkflow.defaults import argHandler #Import the default arguments
import os
import sys
from darkflow.darkflow.net.build import TFNet

FLAGS = argHandler()
FLAGS.setDefaults()
FLAGS.demo = sys.argv[1]

FLAGS.model = "darkflow/cfg/yolo.cfg" # tensorflow model
FLAGS.load = "darkflow/bin/yolo.weights" # tensorflow weights

FLAGS.threshold = 0.4 # threshold of decetion confidance (detection if confidance > threshold )
FLAGS.gpu = 1 #how much of tfhe GPU to use (between 0 and 1) 0 means use cpu
FLAGS.track = True # wheither to activate tracking or not
FLAGS.trackObj = ['car', 'bus']
FLAGS.saveVideo = True  #whether to save the video or not
FLAGS.BK_MOG = False # activate background substraction using cv2 MOG substraction,
                        #to help in worst case scenarion when YOLO cannor predict(able to detect mouvement, it's not ideal but well)
                        # helps only when number of detection < 3, as it is still better than no detection.
FLAGS.tracker = "sort" # wich algorithm to use for tracking deep_sort/sort (NOTE : deep_sort only trained for people detection )
FLAGS.skip = 0 # how many frames to skipp between each detection to speed up the network
FLAGS.json = True
FLAGS.csv = False #whether to write csv file or not(only when tracking is set to True)
FLAGS.display = False # display the tracking or not
FLAGS.verbalise = False

tfnet = TFNet(FLAGS)

tfnet.camera()
# exit()
# exit('Demo stopped, exit.')
