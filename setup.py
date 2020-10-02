from glob import glob
from setuptools import setup

package_name = 'q_ros_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*')),
        ('share/' + package_name + '/urdf', glob('urdf/*.urdf.xacro')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tygoto',
    maintainer_email='tygoto@me.com',
    description='ros kyushu ug tutorial',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = q_ros_tutorial.publisher:main',
        ],
    },
)
