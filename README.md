# Point cloud recording and labelling for terrain data from Gazebo simulation
This repo is for automatically labelling point cloud data from Gazebo simulation, specifically to test rover perception systems


## Environment and Dependencies: 
Everything runs on Ubuntu 18.04 LTS

* Install ROS Melodic: http://wiki.ros.org/melodic/Installation/Ubuntu
* Install catkin: `$ sudo apt-get install ros-melodic-catkin`
* Create a catkin workspace: http://wiki.ros.org/catkin/Tutorials/create_a_workspace
* Clone this repo to src folder of your catkin workspace. 
* If the ROS installation didn't install gazebo then follow: http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install
* Install Gazebo_ros_pkgs:
  * `$ sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control`
  * `$ sudo apt-get install ros-melodic-hector-gazebo-plugins`
  * `$ sudo apt-get install ros-melodic-rqt-robot-steering` - pkg for steering rover via a gui
* Depends on messages defined in common repo https://github.com/novarover/common, please clone into same workspace.
* Depends on the Gazebo simulation at https://github.com/novarover/gazebo, please clone into same workspace and change to the feature/ground_label branch
  
 ## Git Usage:
 * Clone this repository into a subdirectory of the catkin workspace src folder.
 * To develop a feature: branch from `develop` and make a pull request into `develop` when finished with changes.

 ## Compiling:
* Use `$ catkin build` anywhere within workspace to build your packages. If you've previously used `catkin_make` then you may need to delete build and devel folders from your workspace.
* For ROS to see your packages you must use command `$ source ~/catkin_ws/devel/setup.bash` where `catkin_ws` is the path of your workspace folder. This can be done automatically with each new terminal by adding to .bashrc: `$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc`
* Gazebo searches for models using env variable `GAZEBO_MODEL_PATH`. Therefore, you need to add the full path of the models folder to the variable.
`$ echo "export GAZEBO_MODEL_PATH=/path/to/models/:$GAZEBO_MODEL_PATH" >> ~/.bashrc`

## Use:
* Go to the workspace directory and start the Gazebo simulation `$ roslaunch autonomous_sim rough_terrain.launch` 
* Start the Skid Steer Drive Controller graphical tool `$ rosrun rqt_robot_steering rqt_robot_steering`
* Can visualize the point cloud output by using `$ rviz` and adding a PointCloud2 visualization on the /camera/depth/points topic. May need to change the Global Fixed Frame setting to one of the drop down options as well
* Start recording the point cloud stream `$ rosrun record_pointcloud record.py`
* Quit the node to stop recording. The raw point cloud data will be stored under `./data/gazebo_pointcloud.npy` and the labelled dataset will be stored under `./data/gazebo_pc_dataset.pickle`