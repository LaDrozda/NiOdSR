from setuptools import find_packages, setup

package_name = 'camera_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='damianh',
    maintainer_email='kacper.pvs@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
       'circle_motion = camera_subscriber.circle_motion:main',
            'camera_node = camera_subscriber.camera_node:main',
        ],
    },
)