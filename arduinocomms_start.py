import serial
import cv2
import numpy as np
import math
import time

def startComms(coord_list):

    PORT = '/dev/ttyACM0'
    SPEED = 9600
    def send_command(val):
        connection = serial.Serial( PORT, 
                                    SPEED,
                                    timeout=0,
                                    stopbits=serial.STOPBITS_TWO
                                    )
        connection.write(val)
        time.sleep(2)
        connection.flushInput()
        #connection.flushOutput()
        connection.close()

    def receive_command():
        connection = serial.Serial( PORT, 
                                    SPEED,
                                    timeout=5,
                                    stopbits=serial.STOPBITS_TWO
                                    )
        go = True
        tdata = ''
        while(go):
            #time.sleep(2)
            tdata = connection.readline()
            print(tdata)
            time.sleep(1)
            #data_left = connection.inWaiting()
            #print(data_left)
            #tdata += connection.read(data_left)
            if tdata == '!':    
                go = False
        connection.close()
        return tdata

    def button(x):
        s = cv2.getTrackbarPos(switch,'video')
        if(s==0):
            send_command('2')
        if(s==1):
            send_command('1131111111111131111111111111113')

    def classify_direc(move_x,move_y):
        if move_x == 0 and move_y == 0:
            direc = 0
        elif move_x == 0 and move_y > 0:
            direc = 1
        elif move_x > 0 and move_y > 0:
            direc = 2
        elif move_x > 0 and move_y == 0:
            direc = 3
        elif move_x > 0 and move_y < 0:
            direc = 4
        elif move_x == 0 and move_y < 0:
            direc = 5
        elif move_x < 0 and move_y < 0:
            direc = 6
        elif move_x < 0 and move_y == 0:
            direc = 7
        elif move_x < 0 and move_y > 0:
            direc = 8
        return direc

    def transmit_instructions(img2,instruction_list):
        loc = (1,1)
        direcs = {'0': (0,0), '1': (0,1), '2': (1,1), '3': (1,0), '4': (1,-1), '5': (0,-1), '6': (-1,-1), '7': (-1,0), '8': (-1,1)}
        for i in instruction_list:
            #if i == '080000000000200020' or receive_command() == '!':
            #send_command(i[0:18])
            wt = ((float(i[18:22])/1000) + .057)/2
            prin = int(i[0])
            xdel = int(i[2:6])
            ydel = int(i[6:10])
            dur = direcs[i[1]]
            loc = ((loc[0]+(dur[0]*xdel)),((loc[1]+(dur[1]*ydel))))
            #if prin == 1:
            cv2.circle(img2,loc,2,(0,0,255),-1)
            #time.sleep(wt)
            #print(wt)
            print ('plotted command: ' + i)
        cv2.imshow('print-preview',img2)

    def sign_extend(unextended):
        if len(unextended) == 1:
            return '000' + unextended
        elif len(unextended) == 2:
            return '00' + unextended
        elif len(unextended) == 3:
            return '0' + unextended
        elif len(unextended) == 4:
            return unextended

    def compute_instruction(coord_list):
        instruction_list = []
        for i in range(0, len(coord_list)):
            for j in range(0, len(coord_list[i])):
                if i == 0 and j == 0:
                    printgo = 0
                    move_x = coord_list[i][j][0]
                    move_y = coord_list[i][j][1]
                    instruction_list.append('0800000000002000200000')
                elif len(coord_list[i]) > 1:
                    printgo = 1
                    move_x = coord_list[i][j][0] - coord_list[i][j-1][0]
                    move_y = coord_list[i][j][1] - coord_list[i][j-1][1]
                    if move_x > 0 or move_x < 0:
                        R_x = abs(move_y/move_x)
                    else:
                        R_x = abs(move_y)
                    if move_y > 0 or move_y < 0:
                        R_y = abs(move_x/move_y)
                    else:
                        R_y = abs(move_x)
                    if R_x > 1:
                        R_y = 20
                    elif R_y > 1:
                        R_x = 20
                    #########################
                    delta_x = str(abs(move_x))
                    delta_y = str(abs(move_y))
                    delay_x = str(R_x)
                    delay_y = str(R_y)
                    #########################
                    direc = classify_direc(move_x,move_y)
                    #########################
                    # if len(delta_x) == 1:
                    delta_x = sign_extend(delta_x)
                    delta_y = sign_extend(delta_y)
                    delay_x = sign_extend(delay_x)
                    delay_y = sign_extend(delay_y)
                    ##########################
                    timing = '0000'
                    if R_x == 20:
                        timing = sign_extend(str(abs((R_x*move_x))))
                    if R_y == 20:
                        timing = sign_extend(str(abs((R_y*move_y))))

                    command = str(printgo) + str(direc) + delta_x + delta_y + delay_x + delay_y + timing
                    instruction_list.append(command)
                elif len(coord_list[i]) == 1:
                    move_x = coord_list[i][j][0] - coord_list[i-1][len(coord_list[i-1])-1][0]
                    move_y = coord_list[i][j][1] - coord_list[i-1][len(coord_list[i-1])-1][1]
                    delta_x = str(abs(move_x))
                    delta_y = str(abs(move_y))
                    delta_x = sign_extend(delta_x)
                    delta_y = sign_extend(delta_y)
                    delay_x = '0020'
                    delay_y = '0020'
                    direc_x = classify_direc(move_x,0)
                    direc_y = classify_direc(0,move_y)
                    printgo = 0
                    timing = sign_extend(str(abs(20))) #could multiply by move_x
                    command1 = str(printgo) + str(direc_x) + delta_x + '0000' + delay_x + '0000' + timing
                    timing2 = sign_extend(str(abs(20))) #could multiply by move_y
                    command2 = str(printgo) + str(direc_y) + '0000' + delta_y + '0000' + delay_y + timing2
                    printgo = 1
                    #timing3 = sign_extend('2000')
                    command3 = str(printgo) + '0' + '0000' + '0000' + '0000' + '0000' + '2000'
                    instruction_list.append(command1)
                    instruction_list.append(command2)
                    instruction_list.append(command3)
        print(instruction_list)
        return instruction_list
    cv2.namedWindow('video')
    cv2.namedWindow('print-preview')
    #switch = '0 : OFF \n1 : ON'
    #cv2.createTrackbar(switch, 'video',0,1,button)
    img = cv2.imread('handimage.png')
    img2 = cv2.imread('template.png')
    cv2.imshow('video',img)
    coord_list[0] = [(1,1)]
    printgo = 0
    print('Computing... Please Wait')
    final_instructions = compute_instruction(coord_list)
    print('Finished. Press the "G" key to being printing')
    while(True):
        # Capture frame-by-frame
        if cv2.waitKey(1) & 0xFF == ord('g'):
            transmit_instructions(img2,final_instructions)   
            cv2.imshow('print-preview',img2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # k = cv2.waitKey(1) & 0xFF
        # if k == ord('w'):
        #     send_command('1')
        # elif k == ord('a'):
        #     send_command('2')
        # elif k == ord('s'):
        #     send_command('3')
        # elif k == ord('d'):
        #     send_command('4')
        # elif k == ord('t'):
        #     send_command('5')
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()