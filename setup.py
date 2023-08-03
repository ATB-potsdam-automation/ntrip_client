from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ntrip_client'

setup(
    name=package_name,
    version='1.3.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Rob Fisher',
    author_email='rob.fisher@parker.com',
    maintainer='Rob Fisher',
    maintainer_email='rob.fisher@parker.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='NTRIP client that will publish RTCM corrections to a ROS topic, and optionally subscribe to NMEA messages to send to an NTRIP server',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ntrip_ros = ntrip_client.ntrip_ros:main'
        ],
    },
)