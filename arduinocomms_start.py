import serial
import cv2
import numpy as np
import math

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
        connection.close()

    def receive_command():
        connection = serial.Serial( PORT, 
                                    SPEED,
                                    timeout=0,
                                    stopbits=serial.STOPBITS_TWO
                                    )
        command = connection.read(3)
        connection.flushOutput()
        connection.close()
        return command

    def button(x):
        s = cv2.getTrackbarPos(switch,'video')
        if(s==0):
            send_command('2')
        if(s==1):
            send_command('1131111111111131111111111111113')

    def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
        """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
        """
        
        output_range = output_interval_start - output_interval_end
        input_range = input_interval_end - input_interval_start
        relative_val = val - input_interval_end
        return (float(output_range)/input_range)*relative_val+output_interval_start

    def transmit_instructions(instruction_list):
            for i in instruction_list:
                if receive_command() == '111':
                    send_command(i)
                else:
                    while(receive_command() != '111'):
                        print(waiting)

    def compute_instruction(coord_list):
        instruction_list = []
        for i in range(0, len(coord_list)):
            for j in range(0, len(coord_list[i])):
                if i == 0 and j == 0:
                    printgo = 0
                    move_x = coord_list[i][j][0]
                    move_y = coord_list[i][j][1]
                    instruction_list.append('08000000000000')
                if len(coord_list[i][j]) > 1:
                    printgo = 1
                    move_x = coord_list[i][j][0] - coord_list[i][j-1][0]
                    move_y = coord_list[i][j][1] - coord_list[i][j-1][1]
                    R_x = (move_x/move_y) + 24
                    R_y = (move_x/move_y) + 24
                    #########################
                    delta_x = str(move_x)
                    delta_y = str(move_y)
                    delay_x = str(R_x)
                    delay_y = str(R_y)
                    #########################
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
                    #########################
                    if len(delta_x) == 1:
                        delta_x = '00' + delta_x
                    elif len(delta_x) == 2:
                        delta_x = '0' + delta_x
                    if len(delta_y) == 1:
                        delta_y = '00' + delta_y
                    elif len(delta_y) == 2:
                        delta_y = '0' + delta_y
                    if len(delay_x) == 2:
                        delay_x = '0' + delay_x
                    if len(delay_y) == 2:
                        delay_y = '0' + delay_y
                    ##########################
                    command = str(printgo) + str(direc) + delay_x + delay_y + delay_x + delay_y 
                    instruction_list.append(command)
                    # for u in range(1, abs(move_x)):
                    #     if move_x >= 0:
                    #         send_command('4')
                    #     if move_x < 0:
                    #         send_command('2')
                    # for v in range(1, abs(move_y)):
                    #     if move_y >= 0:
                    #         send_command('1')
                    #     if move_y < 0:
                    #         send_command('3')
                    
                if len(coord_list[i][j]) == 1:
                    move_x = coord_list[i][j][0] - coord_list[i-1][end][0]
                    move_y = coord_list[i][j][1] - coord_list[i-1][end][1]
                    printgo = False
                    send_command('0123456789')
                    # for u in range(1, abs(move_x)):
                    #     if move_x >= 0:
                    #         send_command('4')
                    #     if move_x < 0:
                    #         send_command('2')
                    # for v in range(1, abs(move_y)):
                    #     if move_y >= 0:
                    #         send_command('1')
                    #     if move_y < 0:
                    #         send_command('3')

        # Our operations on the frame come here
        # Display the resulting frame

    cv2.namedWindow('video')
    #switch = '0 : OFF \n1 : ON'
    #cv2.createTrackbar(switch, 'video',0,1,button)
    img = cv2.imread('handimage.png')
    cv2.imshow('video',img)
    coord_list[0] = [(1,1)]
    printgo = 0;
    while(True):
        # Capture frame-by-frame
        if cv2.waitKey(1) & 0xFF == ord('g'):
            
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        k = cv2.waitKey(1) & 0xFF
        if k == ord('w'):
            send_command('1')
        elif k == ord('a'):
            send_command('2')
        elif k == ord('s'):
            send_command('3')
        elif k == ord('d'):
            send_command('4')
        elif k == ord('t'):
            send_command('5')
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()