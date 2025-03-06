# ros2_workshop

<!-- GETTING STARTED -->
## Getting Started

To prepare your PC you need:
* Install Ubuntu 22.04 on PC or in Virtual Machine
Download the ISO [Ubuntu 22.04](https://ubuntu.com/download/desktop) for your PC
* Install [ROS 2 Humble](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) on your Ubuntu 22.04
* Install ROS 2 missing libraries. Some libraries that are used in this project are not in the standard ROS package. Install them with:
```sh
sudo apt-get update && sudo apt-get install -y \
     ros-humble-joint-state-publisher-gui \
     ros-humble-xacro \
     ros-humble-ros2-control \
     ros-humble-moveit* \
     ros-humble-ros2-controllers \
     ros-humble-ros-gz-* \
     ros-humble-*-ros2-control
```
* Install VS Code on your PC
* Install Python and C++ additional libraries
```sh
sudo apt-get update && sudo apt-get install -y \
     libserial-dev \
     python3-pip
```

```sh
pip install pyserial
```

```sh
sudo apt-get install ros-humble-urdf-tutorial
```


### Installation

1. Clone the repo
```sh
git clone https://github.com/MooKol/ros2_workshop.git
```
2. Build the ROS 2 workspace
```sh
cd ~/ros2_workshop
```
```sh
colcon build
```
3. Source the project
```sh
. install/setup.bash
```

<!-- USAGE EXAMPLES -->
## Usage

To launch the ROS 2 **Simulated robot**
```sh
. install/setup.bash
```
```sh
ros2 launch arduinobot_description gazebo.launch.py
```
```sh
. install/setup.bash
```
```sh
ros2 launch arduinobot_controller controller.launch.py 
```
```sh
. install/setup.bash
```
```sh
ros2 launch arduinobot_moveit moveit.launch.py 


