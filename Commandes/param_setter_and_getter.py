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

vehicle.parameters['GPS_TYPE'] = 3
gps_type = vehicle.parameters['GPS_TYPE']
print("GPS_TYPE param value is %s"%str(gps_type))