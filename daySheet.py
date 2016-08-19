#!/usr/bin/python
import glob
from PIL import Image
from PIL import ImageStat
from PIL import ImageChops
from PIL import ImageFont
from PIL import ImageDraw
from PIL.ExifTags import TAGS, GPSTAGS
import string, sys, traceback, datetime, time, calendar
import os, shutil
from PIL import *
import math





def daySheet(namePath,xstep,ystep,orientation,backGround,paperSize,thumbSize,quality,inputDir,outputDir,cameraInterval):

	'Creates a daysheet from a list of JPGs and prints a log: filename format = TARONGA_2014_09_29-11_56_58.jpg'
	'Each list must be constituted by a single days images to avoid over pasting'

	cellInfo = []
	today = os.path.basename(namePath[0])
	
	location = today[0:7]
	today = today[8:18]
	
	print '\ntoday ', today
	print ' '


	#create new Proof.tiff file
	Proofimg = Image.new('RGB', paperSize, backGround)


	#process all thumbs from day
	for name in namePath:

	
		#resize
		img = Image.open(name).resize(thumbSize)
		name = os.path.basename(name)
		#parse cellInfo
		nameInfo = cellNumbers(name,cameraInterval,xstep,ystep,orientation) # call to cellNUmbers function that delivers info for each image in proof set 
		cellInfo.append(nameInfo) #list of cellInfo for each cell

   		Proofimg.paste(img,(nameInfo[12][0],nameInfo[12][1]))





   	#Proofimg.save(outputDir+'/'+nameInfo[2] +'_'+ today +'_'+'PROOF_'+'.tif','tiff', quality=quality)#tiff
   	Proofimg.save(outputDir+'/'+nameInfo[2] +'_'+ today +'_'+'PROOF_'+'.jpeg','jpeg', quality=95)#jpeg
	

	print 'cellInfo ',cellInfo

	

	logWriter(cellInfo, inputDir, outputDir)


