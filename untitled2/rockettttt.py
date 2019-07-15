position = 100
velocity = 0
gravity = -10
fuel = 100
thruster = 0        # thruster = 0~20

print (" P: {0} , V: {1}, F: {2}". format(position, velocity, fuel))

while 1:
    input_temp = input("Input thrusters : ")

    if (input_temp < 0):
        print("Thruster can't be less than 0 ")
        thruster = 0
    elif (input_temp >= 20):
        print("Thruster can't be bigger than 20 ")
        thruster = 20
    else:
        thruster = input_temp

    #if input_temp > fuel, show the fuel by thruster. And calc the last fuel
    if (input_temp > fuel):
        print ("Out of fuel! Thrusters at {}".format(fuel))

        thruster = fuel
        #add count the val by fuel
        count = fuel
        fuel = 0

        while 1:
            if(count == 0):
                break
            elif(count == 1):
                #DO NOT USED THE THRSTER VALUE
                #DO NOT CALC THE FUEL

                acceleration = gravity
                position = position + velocity + acceleration * 0.5
                velocity = velocity + acceleration
                if velocity >= -3:
                    print("Landing successful!")
                    exit()
                else:
                    print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))
                    print ("Rocket crashed! Velocity was {} m/s".format(velocity))
                    exit()
            elif(count == 4):
                # DO NOT CALC THE FUEL

                # calc acceleration
                acceleration = gravity + thruster
                # calc position
                position = position + velocity + acceleration * 0.5
                # calc velocity
                velocity = velocity + acceleration
                print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))
                print("No fuel -- rockeet is in free-fall!")
                count = count - 1
            else:
                # DO NOT USED THE THURSTER VALUE
                # DO NOT CALC THE FUEL

                # calc acceleration
                acceleration = gravity
                # calc position
                position = position + velocity + acceleration * 0.5
                # calc velocity
                velocity = velocity + acceleration
                print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))
                print("No fuel -- rockeet is in free-fall!")
                count = count - 1

    # calc acceleration
    acceleration = gravity + thruster
    # calc position
    position = position + velocity + acceleration * 0.5
    # calc fuel
    fuel = fuel - thruster
    # calc velocity
    velocity = velocity + acceleration

    if position < 0:
        position = 0
        print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))
        print("Landing successful!")
        exit()
    else:
        print ('P: {0} V: {1} F: {2}'.format(position, velocity, fuel))
        