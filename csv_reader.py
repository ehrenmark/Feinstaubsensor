# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:37:20 2022

@author: Marcus
"""
import os
import csv

class CSV_import:
    def __init__(self, directorys:[str]):
        self.cwd = os.getcwd()
        self.file_directorys = directorys
        print(self.cwd)
    
    def read_files(self):
        data = {}
        for directory in self.file_directorys:
            files = os.listdir(self.cwd + os.sep + directory)
            file_data = []
            for file in files:
                #print(self.cwd + os.sep + directory + os.sep + file)
                #with open("path", "r") as file: # reading files here
                    # do your part
                with open(self.cwd + os.sep + directory + os.sep + file) as csv_file:
                    #print(csv_file.readline())
                    line = csv_file.readline()
                    while line:
                        line = line[:-1]
                        file_data2 = line.split(";")
                        line = csv_file.readline()
                        try:
                            if(directory == "csv_sds011"):
                            #sensor_id, location, lon, lat, p1, dur_p1, ratio_p1, p2, dur_p2, ratio_p2, messzeitpunkt
                                file_data.append(
                                (
                                    file_data2[0],  # sensor_id
                                    file_data2[2],  # location
                                    file_data2[3],  # lon
                                    file_data2[4],  # lat
                                    file_data2[6],  # p1
                                    file_data2[7],  # dur_p1
                                    file_data2[8],  # ratio_p1
                                    file_data2[9],  # p2
                                    file_data2[10],  # dur_p2
                                    file_data2[11],  # ratio_p2
                                    file_data2[5]  # Messzeitpunkt
                                )
                                )
                            elif(directory == "csv_dht22"):
                                file_data.append(
                                    (
                                    #sensor_id, location, lon, lat, humidity, temperature, messzeitpunkt
                                    file_data2[0],
                                    file_data2[2],
                                    file_data2[4],
                                    file_data2[3],
                                    file_data2[7],
                                    file_data2[6],
                                    file_data2[5]
                                )
                                )
                            else:
                        # Tupel ()
                                file_data.append(tuple(file_data2))
                        except Exception:
                            return
            data[directory] = file_data
        return data