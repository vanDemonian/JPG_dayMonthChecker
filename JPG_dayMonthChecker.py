#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------------------------------
Filename:           JPG_dayMonthChecker.py
Author:             Martin Walch
Release Date:       2016-05-21
Description:        1920 x 1080 symbolic map of files
                    Each landscape tiff consists of
                    31 cells (one for each possible day of the month) made of
                    288 subcells (one for each 5 minute section of a day)
                    
            ****    
                    
                    Iterates through a directory tree of JPG's renamed by JPG_reNamer.py.

                    TARONGA_2014_09_29-11_56_58.jpg

                    Creates a new sheet for each month and places each pixel patch (R, G or B) according to
                    the time of day it was taken.

                    blank = no image
                    Green = 1 image
                    Red = 2 or more images
                    

Required Modules:   logWriter.py
                    cellData.py
                    proofSheet.py
                    EXIF.py
                    dirwalk.py
---------------------------------------------------------------------------------------------------
"""






import glob
from PIL import Image
from PIL import ImageStat
from PIL import ImageChops
from PIL.ExifTags import TAGS, GPSTAGS
import string, sys, traceback, datetime, time, calendar
import os, shutil
from PIL import *
import math
from checkSheet import *


red = (200, 50, 50)
green = (50, 200, 50)
blue = (50, 50, 200)

white = (255,255,255)
backGround = white

#baseImage = "dayMonth_base.tif"


P_1080        = (1920, 1080)
P_1080_check  = (6, 6)

#change these values according to size of output required
paperSize = P_1080
checkSize = P_1080_check




inputDir    = '/Volumes/3TB_DP/RAW_DATA/KINGWIL'   #root directory that will be parsed (includes subdirectories)
outputDir   = '/Users/pyDev/Documents/JPG_dayMonthChecker/checker_outputs' #output directory (must be created before script is run)
fileExt     = '.jpg'
cameraInterval = 300 #this is the number of seconds between each capture:   5mins = 300 secs


allnames = []
allnamePaths = []
dateList = []

monthList = []


cellInfo = []


DateChangeList =[]
MonthChangeList = []

DAYS = []
MONTHS = []



count = 0



def Timer(start, end):
    """
    Calculates the time it takes to run a process, based on start and finish times
    ---------------------------------------------------------------------------------------------
    Inputs:       in seconds 
    start:        Start time of process
    end:          End time of process
    ---------------------------------------------------------------------------------------------
    """
    elapsed = end - start
    # Convert process time, if needed
    if elapsed <= 59:
        time = str(round(elapsed,2)) + " seconds\n"
    if elapsed >= 60 and elapsed <= 3590:
        min = elapsed / 60
        time = str(round(min,2)) + " minutes\n"
    if elapsed >= 3600:
        hour = elapsed / 3600
        time = str(round(hour,2)) + " hours\n"
    return time


##### RUN #####

if __name__ == '__main__':
    #start = time.clock()
    start = time.time()

    print '   '
    print 'JPG_dayMonthChecker.py   '
    print '   '

    # loop to create list of all names and  their paths
    for root, dirs, files in os.walk(inputDir):
        for name in files:
            
            if name.endswith(fileExt):

                allnames.append(name)           #list of filenames - basename only
                allnamePaths.append(os.path.join(root,name))    #list of all names with directory paths appended

                count = count + 1

    #---------------------------------------------------------------
    #print allnamePaths - debug

    #set date of first name as 'today' and appends it to the empty 'dateList'
    firstdate = allnames[0][8:18]
    todaysdate =  firstdate
    dateList.append(todaysdate)
    #print dateList - debug

    #   loop to create list of days by checking if the date changes
    #   and adding the date to the list of dates if it does.
    for name in allnames:

        if name[8:18] != todaysdate:
            #create new day and append name
            dateList.append(name[8:18])



            #create a new month object







            #create a new day object







            #make the new date = 'today'
            todaysdate = name[8:18]



    numberofDays = len(dateList)
    print 'Number of Days = ', numberofDays



    #---------------------------------------------------------------

    #set month of first name as todaysMonth and appends it to the start of 'monthList'
    todaysMonth = allnames[0][8:15]
    monthList.append(todaysMonth)

    #   loop to create list of months by checking if the month changes
    #   and adding the month to the list of months if it does.
    for name in allnames:

        if name[8:15] != todaysMonth:
            #create new month and append name
            monthList.append(name[8:15])
            #make the new date = 'today'
            todaysMonth = name[8:15]



    numberofMonths = len(monthList)
    print 'Number of Months = ', numberofMonths

    #---------------------------------------------------------------


    today = 0

    for i in range(0,len(allnamePaths)):
        date = os.path.basename(allnamePaths[i])
        date = date[8:18]
        

        if date != today:
            today = date
            DateChangeList.append(i)
        
        print ' ', i,'   ',date

    DateChangeList.append(len(allnamePaths)-1)
    print 'Date Change List  ', DateChangeList


    #---------------------------------------------------------------



    d = 0

    for x in range(len(DateChangeList)-1):
        #print x,' ', len(allnamePaths)
        v = DateChangeList[d]
        
        v1 =DateChangeList[(d+1)]
        print 'v ',v,'v1 ',v1
        proofPath = allnamePaths[v:v1]
        DAYS.append(proofPath)


        d+=1

    print ' '
    print ' '
    print ' '


    print ' ****************************************************** '

    thismonth = 0

    for i in range(0,len(allnamePaths)):
        month = os.path.basename(allnamePaths[i])
        month = month[8:15]
        

        if month != thismonth:
            thismonth = month
            MonthChangeList.append(i)
        
        print ' ', i,'   ',month

    MonthChangeList.append(len(allnamePaths)-1)
    print 'Month Change List  ', MonthChangeList


    #---------------------------------------------------------------
    dd = 0

    for x in range(len(MonthChangeList)-1):
        #print x,' ', len(allnamePaths)
        v  = MonthChangeList[dd]
        
        v1 = MonthChangeList[(dd+1)]
        print 'v ',v,'v1 ',v1
        monthPath = allnamePaths[v:v1]
        MONTHS.append(monthPath)

        dd+=1





    for monthPath in MONTHS:
        #print '    '
        #print monthPath
        #print '****'
        checkSheet(monthPath, inputDir, outputDir, cameraInterval)


    finish = time.time()





    #print 'List of dates in data ', dateList
    print 'Total Number of dates = ', len(dateList)
    print
    print 'List of months in data ', monthList
    print
    print 'Total Number of months = ', len(monthList)
    print
    print 'Total Number of Images processed: ', str(count)
    print
    print 'Processing done in ', Timer(start, finish), '\n'



