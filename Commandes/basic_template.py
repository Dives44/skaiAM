##### DEPENDENCIES ####
from dronekit import connect, VehicleMode, LocationGlobalRelative,APIException
import time
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

def arm_and_takeoff(targetHeight):
    """
    :param targetHeight: Height to takeoff in meters
    :return: Take off drone to targetHeight with a tolerance of 0.95% then return None
    """
    #Arming the drone
    while not vehicle.is_armable:
        print("Waiting for the vehicle to become armable")
        time.sleep(1)
    print("Vehicle is armable")

    vehicle.mode = VehicleMode("GUIDED")

    while not vehicle.mode != 'GUIDED':
        print("Waiting for the vehicle to enter guided flight mode")
        time.sleep(1)
    print("Vehicle is now in GUIDED MODE. Have fun!")

    vehicle.armed = True
    while vehicle.armed == False:
        print("Waiting for vehicle to become armed")
        time.sleep(1)

    #Taking off the drone
    vehicle.simple_takeoff(targetHeight)
    while True:
        print("Current Altitude: %d"%vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt>0.95*targetHeight:
            break
        time.sleep(1)
    print("Target altitude reached.")
    return None


##### MAIN EXECUTABLE #####

vehicle = connectMyCopter()
arm_and_takeoff(10)

# set the default speed
vehicle.airspeed = 7

# go to wp1
print("go to wp1")
wp1 = LocationGlobalRelative(47.193077,-1.465763,10)
vehicle.simple_goto(wp1)

# Wait 30sec
time.sleep(30)

# Coming back
print("Coming Back")
vehicle.mode = VehicleMode("RTL")
time.sleep(20)

#Close connection
vehicle.close()


