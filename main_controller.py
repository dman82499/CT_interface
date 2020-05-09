"""main_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


# create the Robot instance.
def initialize():
    print("Initializing robot")
    robot = Robot()

    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    a = robot.getDistanceSensor("ds_right")
    motor1 = robot.getMotor("wheel1")
    motor2 = robot.getMotor("wheel2")
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getMotor('motorname')
    #  ds = robot.getDistanceSensor('dsname')
    #  ds.enable(timestep)

    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    print("entering loop")
    while robot.step(timestep) != -1:

        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()

        # Process sensor data here.

        # Enter here functions to send actuator commands, like:
        # motor.setPosition(10.0)
        pass
    print("sucessfully stopped program")
# Enter here exit cleanup code.
def getinput(inputs):
    for x in inputs:
        inputs_out = inputs[x]
    return(inputs_out)
initialize()