import math

#####################
# CSE 231 - Project 02
# Algorithm Overview:
# Create a program loop, requesting user input for functionality
# Different subprograms shown below:

# Speed Calculator:
## Prompt QPUs and Slope angle
## Calculate Mario's speed knowing that distance = speed and 1 QPU = 4*PU
## Because De Facto Speed = distance (PUs), calculate Mario's speed from formula
## Mario's Speed = De Facto Speed (distance) / cos(angle of slope)
## Output mario's speed

# PU Navigator:
# Prompt for Mario Speed and slope
# Calculate how many PUs traveled and final position in last PU
# Decide whether step is valid and update or not PUs traveled and position
# Output

PU_SIZE = 65535
ISLAND = 1000
SCUTTLEBUG_RADIUS = 10

running = True  # declare control variable for exiting program
while running:  # declare loop
    PROMPT = input(
        "\nSelect one of the following options:\n\
        1: Speed calculator\n\
        2: Parallel Universe navigator\n\
        3: Scuttlebug transportation\n\
        q: Exit the program\n\
        Option: ")

    if PROMPT == "q": # exit while loop and program
        running = False
        break

    elif PROMPT == "1":  # Enter Speed Calculator subprogram
        qpu = float(input("\nHow many QPUs do you want to travel? "))
        distance = qpu * 4 * PU_SIZE  # converts QPUs to PUs and then to travel distance
        slope_rad = float(input("\nWhat is the angle of the slope on which Mario is standing? "))
        mario_speed = distance / math.cos(slope_rad)  # calculate mario speed based on formula shown before
        print("\nMario needs", round(mario_speed), "speed")

    elif PROMPT == "2":  #Parallel Universe navigator
        slope_rad = float(input("\nWhat is the angle of the slope on which Mario is standing? "))
        mario_speed = float(input("\nWhat is Mario's speed? "))
        dfspeed = mario_speed * math.cos(slope_rad)  # calculate de facto speed
        Mario_pos = 0
        pu = 0
        for i in range(1, 5):  # line below checks step validity under conditions given in statement
            if 0.25 * dfspeed == PU_SIZE or abs((0.25 * dfspeed + Mario_pos) % PU_SIZE - PU_SIZE) < ISLAND:
                pu += 0.25 * dfspeed / PU_SIZE  # add PUs travelled
                if 0.25 * dfspeed == PU_SIZE:  # check if mario travelled to new PU and reset pos accordingly
                    Mario_pos = 0
                else:
                    Mario_pos = ((0.25 * dfspeed + Mario_pos) % PU_SIZE) - PU_SIZE  # adjust mario pos in the PU
            else:
                print("\nQuarter step", i, "is invalid!")  # i is the step number
                break
        if pu < 2: print("\nMario has travelled", round(pu), "PU")  # print PU if it is singular
        elif pu >= 2: print("\nMario has travelled", round(pu), "PUs")  # print PUs
        print("Mario's position in this PU:", round(Mario_pos)) # Print marios position

    elif PROMPT == "3":
        hp = int(input("\nWhat is Mario's current HP? ")) # initialize and prompt hp variable
        while hp < 1 or hp > 8: # loop until hp within range
            print("\nInvalid amount of HP!")
            hp = int(input("\nWhat is Mario's current HP? "))  # correct variable
        coin_dist = int(input("\nAt what distance is the coin placed? Enter -1 if there is no coin. "))
        distance = hp * SCUTTLEBUG_RADIUS  # since each hp moves the bug its radius' length
        if coin_dist == -1: # if there is no coin, output distance with current hp
            distance = distance # remains the same
        elif hp * SCUTTLEBUG_RADIUS > coin_dist and hp + 1 <= 8: # check if coin is within reach and acquirable
            distance = (hp + 1) * SCUTTLEBUG_RADIUS # if there is a coin, add one HP to calculation
        print("\nThe Scuttlebug can be transported", distance, "units of distance")