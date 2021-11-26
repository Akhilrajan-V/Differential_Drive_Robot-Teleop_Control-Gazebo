All Folders, Files, Codes and this Readme file were created by AKhilrajan Vethirajan in collaboration with Vishaal Kanna Sivakumar
for ENPM 662 Inrtroduction to Robot Modeling - Project 1 at University of Maryland, USA.   


README


This a readme file for project 1 of ENPM 662. The project file contains 2 main folders: the Package folder and the Assembly folder. Package folder contains all the necessary files and meshes to run the Gazebo Simulation and the Assembly folder contains the CAD files (design parts). 


INSTRUCTIONS

**Even though all file paths are coded to run from model4_new directory**
**Make Sure all the paths are correct or you can change all paths to your system directory**


Step 1: Unzip the entire folder in your computer, the package folder holds a folder named model4_new. 
Move the model4_new folder into your catkin workspace source folder (catkin_ws/src).


Step 2: Build your Catkin workspace using "catkin_make" command in a terminal.


Step 3: To launch the model in an  empty Gazebo world, open a new terminal and type “roslaunch model4_new project_empty.launch ”. 
If you want to launch the model in the custom world use “roslaunch model4_new project1.launch”.


***To Control using Teleop*** 


Step 4: Make sure the teleop file is executable. Open the src folder of model4_new folder. Open a terminal in that folder and type “chmod +x teleop.py”. This will make the .py  executable. 


Step 5: Now that the model is launched into a world, open a new terminal and type “rosrun model4_new teleop.py”. 
This will run the teleoperation script and allows you to move the model using specified keys. 


***To run Publisher and Subscriber***


Step 6: Make sure you have launched the model in an empty world. Now open two new terminals and type “rosrun model4_new publisher.py” in one terminal and “rosrun model4_new subscriber.py” 
in the other terminal. This will publish commands to move the model in a straight line. ***Make sure publisher.py and subscriber.py are executable, if not use “chmod +x <file_name.py>”.



