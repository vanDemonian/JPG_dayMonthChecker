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
from dayCoords import *



def checkSheet(MONTH,inputDir,outputDir,cameraInterval):

	'Creates a visual checksheet from a list of JPGs'
	'one cell for each day of the  month'
	'288 possible image samples within each cell'

	paperSize = (1920, 1080)
	checkSize = (6,6)
	green = (50,200,50)
	red = (200, 50, 50)

	inputDir = inputDir
	outputDir = outputDir
	cameraInterval = cameraInterval

	cellInfo = []
	today = os.path.basename(MONTH[0])
	
	location = today[0:7]
	thismonthyear = today[8:15]
	
	print '\nthismonthyear ', thismonthyear
	print ' '

	Checkimg = Image.open('dayMonth_base.tif')
	greenImg = Image.open('dayMonth_green.tif')
	
	fnt = ImageFont.truetype('TrueTypeFonts/arial.ttf', 30)

	#process all dates in the month
	yy = -100

	for name in MONTH:

		name = os.path.basename(name)
		var = dayCoords(name)
		print "var ", var
		print var[0]
		print var[1]
		print var[2]

		xx =  var[2]	


		pixels = (var[0], var[1], (var[0]+6), (var[1]+6))
		
		if xx == yy:
			Checkimg.paste(red, pixels)
		else:
			Checkimg.paste(green, pixels)

			
   		yy = xx


	draw = ImageDraw.Draw(Checkimg)
   	draw.text((130, 1000), location, font=fnt, fill=(0,0,0,128))
	draw.text((1500, 1000), thismonthyear, font=fnt, fill=(0,0,0,128))

   	Checkimg.save(outputDir+'/'+location +'_CHECK*PROOF_' + thismonthyear +'_'+ '.jpeg','jpeg', quality=100)#jpeg
	



	



