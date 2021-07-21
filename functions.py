'''
* Time information in the binary file is in TAI seconds from January 1st 2000, 00:00:00
* ECI frame of reference is J2000
* The size of a data chunk is 2068 bytes...

https://www.programcreek.com/python/example/2716/numpy.uint8
'''

import os.path
import csv
import numpy as np

def read_bin(size):
    print("inside read_bin")
    file = open("telemetry.bin", "rb")
    big_list = []

    counter = 0
    bytetext = ""
    #chunk_counter = 0
    #while chunk_counter < 3:

    byte = file.read(1)
    while byte:
        bytelist = []
        while counter < size :
            bytelist.append(byte)
            '''byteint = int(byte, 2)
            bytechar = chr(byteint)
            bytetext += bytechar'''
            byte = file.read(1)
            counter = counter + 1
        #print(bytetext)
        #print(len(bytelist))
        big_list.append(bytelist)
        counter = 0

    print("Final list of data contains {} elements. \n".format(len(big_list)))

    '''c = 0
    for e in range(len(big_list)):
        if c == 12:
            break
        else:
            print("{}".format(big_list[e]))
            c = c + 1
    '''
    file.close()
    return big_list

def read_bin2():
    with open("telemetry.bin", "rb") as binary_file:

        bytearray = np.fromfile(binary_file, dtype=np.uint8)
        print(bytearray)
        print(len(bytearray))

        cnt = 0
        chunk_list = []
        big_list = []
        for e in range(len(bytearray)):
            chunk_list.append(bytearray[e])
            cnt += 1
            if cnt == 2068:
                big_list.append(chunk_list)
                #print(chunk_list)
                chunk_list = []
                cnt = 0
    return big_list
    binary_file.close

def create_csv(bin_data, filename):
    print("inside create_csv")
    if os.path.exists(filename):         #DELETE THE NOT CLAUSE HERE
        choice = input("File already exists! \nWould you like to write data anyway? [Y/N] \n")
        if choice == 'Y':
            print("Writing data...")
            with open(filename, 'w', newline="") as file_csv:
                writer = csv.writer(file_csv)

                c = 0
                for e in range(len(bin_data)):
                    if c == 4000:
                        break
                    else:
                        # print("{}".format(bin_data[e]))
                        c = c + 1
                        writer.writerow(bin_data[e])
                print("Wrote {:} many rows into file {:}".format(c, filename))
        else:
            return 0


    else:
        print("Creating file...")
        with open(filename, 'w', newline="") as file_csv:
            writer = csv.writer(file_csv)

            c = 0
            for e in range(len(bin_data)):
                if c == 4000:
                    break
                else:
                    #print("{}".format(bin_data[e]))
                    c = c + 1
                    writer.writerow(bin_data[e])
            print(c)




