from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable
from launch_ros.substitutions import FindPackageShare
import os

package_name = 'ntrip_client'

def generate_launch_description():
     
      return LaunchDescription([      
          # Declare arguments with default values
          DeclareLaunchArgument('debug',                 default_value='false'),
          DeclareLaunchArgument('config_file', default_value='params.yaml'),
          # Pass an environment variable to the node
          SetEnvironmentVariable(name='NTRIP_CLIENT_DEBUG', value=LaunchConfiguration('debug')),
          

          # ******************************************************************
          # NTRIP Client Node
          # ******************************************************************
          Node(
                name='ntrip_client_node',
                namespace='ntrip_client',
                package='ntrip_client',
                executable='ntrip_ros',
                parameters=[PathJoinSubstitution( [ FindPackageShare(package_name), 'config', LaunchConfiguration('config_file') ] )],
                # Uncomment the following section and replace "/gq7/nmea/sentence" with the topic you are sending NMEA on if it is not the one we requested
                remappings=[
                 ("/ntrip_client/nmea", "/nmea")
                ],
          )
      ])