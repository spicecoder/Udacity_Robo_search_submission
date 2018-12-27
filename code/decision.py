import numpy as np
import time

def stop(Rover):
    if Rover.vel > 0.2:
        Rover.throttle = 0
        Rover.brake = Rover.brake_set
        Rover.steer = 0
    elif Rover.vel < 0.2:
        Rover.mode = 'stop'
            
def find_and_go(Rover):
    if Rover.near_sample and Rover.vel == 0 and not Rover.picking_up:
        Rover.send_pickup = True
    else:
        if len(Rover.nav_angles) < Rover.go_forward:
            Rover.throttle = 0
            Rover.brake = 0
            Rover.steer = -15
            #print("decesion find n go1")
        if len(Rover.nav_angles) >= Rover.go_forward:
            Rover.throttle = Rover.throttle_set
            Rover.brake = 0
            Rover.mode = 'forward'
            #print("decesion find n go2")
        if  Rover.vel == 0 :
            #Rover.steer = Rover.p_steer  - 180
            Rover.brake = 0
            Rover.steer = 15
            Rover.throttle = Rover.throttle_set
            #print("find steer back ")    
        
def move(Rover):
    Rover.o_pos = Rover.pos
    if Rover.near_sample:
        Rover.mode = 'tostop'
        #print("decesion move 1")
    if  Rover.vel == 0 :
        #Rover.brake = Rover.brake_set
        steer_away = np.random.randint(-15, high=15, dtype='int')
        Rover.steer = Rover.steer + steer_away
        Rover.throttle = Rover.throttle_set
        print("stuck ! decesion steer from",":",Rover.steer)
          
    
    elif len(Rover.nav_angles) >= Rover.stop_forward:
        if Rover.vel < Rover.max_vel:
            Rover.throttle = Rover.throttle_set
            #print("decesion move 2")
        else:
            Rover.throttle = 0
            #print("decesion move 3")
        Rover.brake = 0
        Rover.p_steer = Rover.steer             
        Rover.steer = np.max((Rover.nav_angles) * 180 / np.pi) - 30 # minus wall offset
    else:
        Rover.mode = 'tostop'
        Rover.steer = -15
        #print("decesion move 4")
def initial_setup(Rover):
    if 90 < Rover.yaw < 95:
        Rover.throttle = Rover.throttle_set
        Rover.brake = 0
        Rover.steer = 0
        if len(Rover.nav_angles) < Rover.go_forward:
            Rover.mode = 'stop'
           # print("decesion01")
    else:
        Rover.brake = 0
        Rover.throttle = 0
        if 90 > Rover.yaw or Rover.yaw >= 270:            
            Rover.steer = 10 
           # print("decesion02")
        else:
            Rover.steer = -10
            #print("decesion03")
def decision_step(Rover): 
    if Rover.o_pos == None:
        Rover.o_pos = Rover.pos
       # print("decesion1")
    else:
        if  Rover.o_pos != Rover.pos:
            Rover.stop_time = Rover.total_time
           # print("decesion2") 
        else :
             Rover.steer = np.clip(np.mean((Rover.nav_angles+60) * 180 / np.pi), -15, 15) - 30
                   
    if Rover.total_time - Rover.stop_time > Rover.max_time:
        Rover.throttle = 0
        Rover.brake = 0
        Rover.steer = Rover.p_steer -60
        time.sleep(1) 
        #print("decesion3")
        
    if Rover.nav_angles is not None:
        if Rover.mode == 'forward':
            move(Rover) 
           # print("decesion6")
        if Rover.mode == 'start':
            initial_setup(Rover)  
            #print("decesion4")            
        if Rover.mode == 'sample':
            recover_sample(Rover, nearest_sample)
           # print("decesion5")
      
        if Rover.mode == 'tostop':
            stop(Rover) 
           # print("decesion7")
        if Rover.mode == 'stop':
            find_and_go(Rover) 
    return Rover
