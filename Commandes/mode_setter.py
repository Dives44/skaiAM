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

while not vehicle.is_armable:
    print("Waiting for the vehicle to become armable")
    time.sleep(1)
print ("Vehicle is armable")

vehicle.mode = VehicleMode("GUIDED")

while not vehicle.mode != 'GUIDED':
    print("Waiting for the vehicle to enter guided flight mode")
    time.sleep(1)
print ("Vehicle is now in GUIDED MODE. Have fun!")

vehicle.armed = True
while vehicle.armed==False:
    print("Waiting for vehicle to become armed")
    time.sleep(1)

