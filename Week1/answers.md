--> Define: node, topic, package, workspace. Provide one sentence each.
Node: A node is a single executable process in ROS 2 that performs a specific task, such as reading sensor data or controlling a motor.
Topic: A topic is a named communication channel used by ROS 2 nodes to send and receive messages asynchronously.
Package: A package is an organized folder that contains ROS 2 code, dependencies, configuration files, and build instructions.
Workspace: A workspace is a directory that contains one or more ROS 2 packages along with the build, install, and log folders used to develop and run them.

--> Explain why sourcing is required. What happens if you do not source a workspace?
Sourcing is required because it sets up environment variables that allow ROS 2 to locate installed packages, executables, and dependencies. When a workspace is sourced, the terminal knows where the built packages are located.
If a workspace is not sourced, ROS 2 will not recognize the packages inside the workspace. Commands like ros2 pkg list or ros2 run will fail to find the package or executable.

--> What is the purpose of colcon build? What folders does it generate?
The command colcon build compiles and builds all ROS 2 packages inside the workspace. It processes package dependencies, installs executables, and prepares the packages so they can be run using ROS 2 commands.
After running colcon build, the following folders are generated:
src/ : your packages (source code)
build/ – contains intermediate build files.
install/ – contains installed packages and executable scripts.
log/ – contains logs generated during the build process.

--> In your own words, explain what the entry_points console script does in setup.py.
The entry_points console script in setup.py registers a Python function as a runnable ROS 2 command. It tells ROS 2 which Python file and function should be executed when the user runs ros2 run <package> <executable>.

--> Draw (by hand or ASCII) a diagram showing one publisher and one subscriber connected
by a topic.
+--------------+
|   Publisher  |
+--------------+
       |
       | Publishes
       | message
       v
+------------------+
|  Message Broker  |
|      Topic       |
+------------------+
       ^
       | subscribe
       | & notify
       v
+--------------+
|  Subscriber  |
+--------------+
       |
       |
       v
+--------------+
|    Process   |
+--------------+
