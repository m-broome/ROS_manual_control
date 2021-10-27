from setuptools import setup

package_name = 'manual_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='michael',
    maintainer_email='broomey2014@outlook.com',
    description='Publish JSON commands on keyboard input for robot control',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'manual_control = manual_control.manual_control:main',
        ],
    },
)
