import scratchconnect
import time

file = open(r"video data.txt","r")
frames = file.readlines()

login = scratchconnect.ScratchConnect("USERNAME_GOES_HERE", "PASSWORD_GOES_HERE")
project = login.connect_project(1030794434, access_unshared=True)  # Connect the project

variables = project.connect_cloud_variables()
variables.get_variable_data(limit=100, offset=0)  # Returns the cloud variable data
variables.set_cloud_variable(variable_name='play?', value=0)
start = input("Press enter to start! ")
variables.set_cloud_variable(variable_name='play?', value=1)
start_time = time.perf_counter()
for frame in range(0, 6713):
    timer = round(abs((start_time -  time.perf_counter())), 1)
    current_l = int(timer * 5)
    c_frame = frames[current_l]
    s1 = slice(0, 255, 1)
    s2 = slice(256, 511, 1)
    s3 = slice(512, 767, 1)
    s4 = slice(768, 1023, 1)
    s5 = slice(1024, 1279, 1)
    s6 = slice(1280, 1400, 1)
    
    pause = 0.02
    variables.set_cloud_variable(variable_name="1", value=c_frame[s1])  # Set a Cloud Variable
    time.sleep(pause)
    variables.set_cloud_variable(variable_name='2', value=c_frame[s2])
    time.sleep(pause)
    variables.set_cloud_variable(variable_name='3', value=c_frame[s3])
    time.sleep(pause)
    variables.set_cloud_variable(variable_name='4', value=c_frame[s4])
    time.sleep(pause)
    variables.set_cloud_variable(variable_name='5', value=c_frame[s5])
    time.sleep(pause)
    variables.set_cloud_variable(variable_name='6', value=c_frame[s6])
    time.sleep(pause)

    print("timer: " + str(timer))
    print(str(current_l) + "/6713")
    #print(c_frame[s1])
    
