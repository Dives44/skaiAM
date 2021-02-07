##### DEPENDENCIES ####
from dronekit import connect, VehicleMode, LocationGlobalRelative,APIException
import time
import socket
import exceptions
import math
import argparse


##### FUNCTIONS #####

def connectMyCopter():
    """
    :return: Vehicle object connected to IP adress specified in terminal
    """
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    #IP adress
    connection_string = args.connect

    if not connection_string: #if we pass no IP adress
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = sitl.connection_string()

    ###>> python connection_template.py --connect 127.0.0.1:14550
    #Use Dronekit to use Ip adress to return vehicle object
    vehicle = connect(connection_string,wait_ready=True)
    return vehicle

##### MAIN EXECUTABLE #####

vehicle = connectMyCopter()

#Version and attributes
vehicle.wait_ready('autopilot_version')
print('Autopilots set attribute from companion: %s'%vehicle.version)

#Does the firmware support the companion pc to set the attitude
print('Supports set attitude from companion: %s'%vehicle.capabilities.set_attitude_target_local_ned)

#Read the actual attitude roll, pitch, yaw
print('Attitude: %s'%vehicle.attitude)

#read the actual velocity (m/s)
print('Velocity: %s'%vehicle.velocity) #North,East,Down

#When did we receive last heartbeat
print('Last heartbeat: %s'%vehicle.last_heartbeat)

#Is the vehicle good to arm
print('Is the vehicle armable: %s'%vehicle.is_armable)

#What is total groundspeed
print('Groundspeed: %s'%vehicle.groundspeed) #This is settable

#What is the actual flight mode
print('Mode: %s'%vehicle.mode.name)

#Is the vehicle armed
print('Armed: %s'%vehicle.armed)
