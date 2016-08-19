#!/usr/bin/python

def dayCoords(name):
	"""
	Calculates the coordinate offset values for each day of the month

	1  2  3  4  5  6  7  8  9  10  11  12
	13 14 15 16 17 18 19 20 21 22  23  24
	25 26 27 28 29 30 31
        
	"""
	location = str(name[0:7])
	year = int(name[8:12])
	month = int(name[13:15])
	day = int(name[16:18])
	hour = int(name[19:21])
	minute = int(name[22:24])
	second = int(name[25:27])
	date = str(name[8:18])

	origin_DATE_X = oDX = 130
	origin_DATE_Y = oDY = 100
	DATE_step_X = dsx = 140
	DATE_step_Y = dsy = 300

	xstep = 10
	ystep = 10
	pasteCoords = []
	cameraInterval = 300

	secs_since_midnight = (int(second) + int(minute*60) + int(hour*3600))

	if secs_since_midnight == 86400:
		gridNum = 287
	else:
		gridNum = int(secs_since_midnight/cameraInterval)

	#coordinates for each day's upper left corner

	if day == 1:
		daycoords = (oDX            , oDY)
	if day == 2:
		daycoords = (oDX + dsx      , oDY)
	if day == 3:
		daycoords = (oDX + (2*dsx)  , oDY)
	if day == 4:
		daycoords = (oDX + (3*dsx)  , oDY)
	if day == 5:
		daycoords = (oDX + (4*dsx)  , oDY)
	if day == 6:
		daycoords = (oDX + (5*dsx)  , oDY)
	if day == 7:
		daycoords = (oDX + (6*dsx)  , oDY)
	if day == 8:
		daycoords = (oDX + (7*dsx)  , oDY)
	if day == 9:
		daycoords = (oDX + (8*dsx)  , oDY)
	if day == 10:
		daycoords = (oDX + (9*dsx)  , oDY)
	if day == 11:
		daycoords = (oDX + (10*dsx) , oDY)
	if day == 12:
		daycoords = (oDX + (11*dsx) , oDY)
	if day == 13:
		daycoords = (oDX            , (oDY+dsy))
	if day == 14:
		daycoords = (oDX + dsx      , (oDY+dsy))
	if day == 15:
		daycoords = (oDX + (2*dsx)  , (oDY+dsy))
	if day == 16:
		daycoords = (oDX + (3*dsx)  , (oDY+dsy))
	if day == 17:
		daycoords = (oDX + (4*dsx)  , (oDY+dsy))
	if day == 18:
		daycoords = (oDX + (5*dsx)  , (oDY+dsy))
	if day == 19:
		daycoords = (oDX + (6*dsx)  , (oDY+dsy))
	if day == 20:
		daycoords = (oDX + (7*dsx)  , (oDY+dsy))
	if day == 21:
		daycoords = (oDX + (8*dsx)  , (oDY+dsy))
	if day == 22:
		daycoords = (oDX + (9*dsx)  , (oDY+dsy))
	if day == 23:
		daycoords = (oDX + (10*dsx) , (oDY+dsy))
	if day == 24:
		daycoords = (oDX + (11*dsx) , (oDY+dsy))
	if day == 25:
		daycoords = (oDX            , (oDY+(2*dsy)))
	if day == 26:
		daycoords = (oDX + dsx      , (oDY+(2*dsy)))
	if day == 27:
		daycoords = (oDX + (2*dsx)  , (oDY+(2*dsy)))
	if day == 28:
		daycoords = (oDX + (3*dsx)  , (oDY+(2*dsy)))
	if day == 29:
		daycoords = (oDX + (4*dsx)  , (oDY+(2*dsy)))
	if day == 30:
		daycoords = (oDX + (5*dsx)  , (oDY+(2*dsy)))
	if day == 31:
		daycoords = (oDX + (6*dsx)  , (oDY+(2*dsy)))


	#Grid number within each day. Format =  24 rows x 12 columns:		
	#row 1

	if gridNum == 0:
		cellCoordinates = (1*xstep, 1*ystep)
	if gridNum == 1:
		cellCoordinates = (2*xstep, 1*ystep)
	if gridNum == 2:
		cellCoordinates = (3*xstep, 1*ystep)
	if gridNum == 3:
		cellCoordinates = (4*xstep, 1*ystep)
	if gridNum == 4:
		cellCoordinates = (5*xstep, 1*ystep)
	if gridNum == 5:
		cellCoordinates = (6*xstep, 1*ystep)
	if gridNum == 6:
		cellCoordinates = (7*xstep, 1*ystep)
	if gridNum == 7:
		cellCoordinates = (8*xstep, 1*ystep)
	if gridNum == 8:   
		cellCoordinates = (9*xstep, 1*ystep)
	if gridNum == 9:
		cellCoordinates = (10*xstep,1*ystep)
	if gridNum == 10:
		cellCoordinates = (11*xstep,1*ystep)
	if gridNum == 11:
		cellCoordinates = (12*xstep,1*ystep)
	#row 2
	if gridNum == 12:
		cellCoordinates = (1*xstep, 2*ystep)
	if gridNum == 13:
		cellCoordinates = (2*xstep, 2*ystep)
	if gridNum == 14:
		cellCoordinates = (3*xstep, 2*ystep)
	if gridNum == 15:
		cellCoordinates = (4*xstep, 2*ystep)
	if gridNum == 16:
		cellCoordinates = (5*xstep, 2*ystep)
	if gridNum == 17:
		cellCoordinates = (6*xstep, 2*ystep)
	if gridNum == 18:
		cellCoordinates = (7*xstep, 2*ystep)
	if gridNum == 19:
		cellCoordinates = (8*xstep, 2*ystep)
	if gridNum == 20:
		cellCoordinates = (9*xstep, 2*ystep)
	if gridNum == 21:
		cellCoordinates = (10*xstep,2*ystep)
	if gridNum == 22:
		cellCoordinates = (11*xstep,2*ystep)
	if gridNum == 23:
		cellCoordinates = (12*xstep,2*ystep)
	#row 3
	if gridNum == 24:
		cellCoordinates = (1*xstep, 3*ystep)
	if gridNum == 25:
		cellCoordinates = (2*xstep, 3*ystep)
	if gridNum == 26:
		cellCoordinates = (3*xstep, 3*ystep)
	if gridNum == 27:
		cellCoordinates = (4*xstep, 3*ystep)
	if gridNum == 28:
		cellCoordinates = (5*xstep, 3*ystep)
	if gridNum == 29:
		cellCoordinates = (6*xstep, 3*ystep)
	if gridNum == 30:
		cellCoordinates = (7*xstep, 3*ystep)
	if gridNum == 31:
		cellCoordinates = (8*xstep, 3*ystep)
	if gridNum == 32:
		cellCoordinates = (9*xstep, 3*ystep)
	if gridNum == 33:
		cellCoordinates = (10*xstep,3*ystep)
	if gridNum == 34:
		cellCoordinates = (11*xstep,3*ystep)
	if gridNum == 35:
		cellCoordinates = (12*xstep,3*ystep)
	#row 4
	if gridNum == 36:
		cellCoordinates = (1*xstep, 4*ystep)
	if gridNum == 37:
		cellCoordinates = (2*xstep, 4*ystep)
	if gridNum == 38:
		cellCoordinates = (3*xstep, 4*ystep)
	if gridNum == 39:
		cellCoordinates = (4*xstep, 4*ystep)
	if gridNum == 40:
		cellCoordinates = (5*xstep, 4*ystep)
	if gridNum == 41:
		cellCoordinates = (6*xstep, 4*ystep)
	if gridNum == 42:
		cellCoordinates = (7*xstep, 4*ystep)
	if gridNum == 43:
		cellCoordinates = (8*xstep, 4*ystep)
	if gridNum == 44:
		cellCoordinates = (9*xstep, 4*ystep)
	if gridNum == 45:
		cellCoordinates = (10*xstep,4*ystep)
	if gridNum == 46:
		cellCoordinates = (11*xstep,4*ystep)
	if gridNum == 47:
		cellCoordinates = (12*xstep,4*ystep)
	#row 5
	if gridNum == 48:
		cellCoordinates = (1*xstep, 5*ystep)
	if gridNum == 49:
		cellCoordinates = (2*xstep, 5*ystep)
	if gridNum == 50:
		cellCoordinates = (3*xstep, 5*ystep)
	if gridNum == 51:
		cellCoordinates = (4*xstep, 5*ystep)
	if gridNum == 52:
		cellCoordinates = (5*xstep, 5*ystep)
	if gridNum == 53:
		cellCoordinates = (6*xstep, 5*ystep)
	if gridNum == 54:
		cellCoordinates = (7*xstep, 5*ystep)
	if gridNum == 55:
		cellCoordinates = (8*xstep, 5*ystep)
	if gridNum == 56:
		cellCoordinates = (9*xstep, 5*ystep)
	if gridNum == 57:
		cellCoordinates = (10*xstep,5*ystep)
	if gridNum == 58:
		cellCoordinates = (11*xstep,5*ystep)
	if gridNum == 59:
		cellCoordinates = (12*xstep,5*ystep)
	#row 6
	if gridNum == 60:
		cellCoordinates = (1*xstep, 6*ystep)
	if gridNum == 61:
		cellCoordinates = (2*xstep, 6*ystep)
	if gridNum == 62:
		cellCoordinates = (3*xstep, 6*ystep)
	if gridNum == 63:
		cellCoordinates = (4*xstep, 6*ystep)
	if gridNum == 64:
		cellCoordinates = (5*xstep, 6*ystep)
	if gridNum == 65:
		cellCoordinates = (6*xstep, 6*ystep)
	if gridNum == 66:
		cellCoordinates = (7*xstep, 6*ystep)
	if gridNum == 67:
		cellCoordinates = (8*xstep, 6*ystep)
	if gridNum == 68:
		cellCoordinates = (9*xstep, 6*ystep)
	if gridNum == 69:
		cellCoordinates = (10*xstep,6*ystep)
	if gridNum == 70:
		cellCoordinates = (11*xstep,6*ystep)
	if gridNum == 71:
		cellCoordinates = (12*xstep,6*ystep)
	#row 7
	if gridNum == 72:
		cellCoordinates = (1*xstep, 7*ystep)
	if gridNum == 73:
		cellCoordinates = (2*xstep, 7*ystep)
	if gridNum == 74:
		cellCoordinates = (3*xstep, 7*ystep)
	if gridNum == 75:
		cellCoordinates = (4*xstep, 7*ystep)
	if gridNum == 76:
		cellCoordinates = (5*xstep, 7*ystep)
	if gridNum == 77:
		cellCoordinates = (6*xstep, 7*ystep)
	if gridNum == 78:
		cellCoordinates = (7*xstep, 7*ystep)
	if gridNum == 79:
		cellCoordinates = (8*xstep, 7*ystep)
	if gridNum == 80:
		cellCoordinates = (9*xstep, 7*ystep)
	if gridNum == 81:
		cellCoordinates = (10*xstep,7*ystep)
	if gridNum == 82:
		cellCoordinates = (11*xstep,7*ystep)
	if gridNum == 83:
		cellCoordinates = (12*xstep,7*ystep)
	#row 8
	if gridNum == 84:
		cellCoordinates = (1*xstep, 8*ystep)
	if gridNum == 85:
		cellCoordinates = (2*xstep, 8*ystep)
	if gridNum == 86:
		cellCoordinates = (3*xstep, 8*ystep)
	if gridNum == 87:
		cellCoordinates = (4*xstep, 8*ystep)
	if gridNum == 88:
		cellCoordinates = (5*xstep, 8*ystep)
	if gridNum == 89:
		cellCoordinates = (6*xstep, 8*ystep)
	if gridNum == 90:
		cellCoordinates = (7*xstep, 8*ystep)
	if gridNum == 91:
		cellCoordinates = (8*xstep, 8*ystep)
	if gridNum == 92:
		cellCoordinates = (9*xstep, 8*ystep)
	if gridNum == 93:
		cellCoordinates = (10*xstep,8*ystep)
	if gridNum == 94:
		cellCoordinates = (11*xstep,8*ystep)
	if gridNum == 95:
		cellCoordinates = (12*xstep,8*ystep)
	#row 9
	if gridNum == 96:
		cellCoordinates = (1*xstep, 9*ystep)
	if gridNum == 97:
		cellCoordinates = (2*xstep, 9*ystep)
	if gridNum == 98:
		cellCoordinates = (3*xstep, 9*ystep)
	if gridNum == 99:
		cellCoordinates = (4*xstep, 9*ystep)
	if gridNum == 100:
		cellCoordinates = (5*xstep, 9*ystep)
	if gridNum == 101:
		cellCoordinates = (6*xstep, 9*ystep)
	if gridNum == 102:
		cellCoordinates = (7*xstep, 9*ystep)
	if gridNum == 103:
		cellCoordinates = (8*xstep, 9*ystep)
	if gridNum == 104:
		cellCoordinates = (9*xstep, 9*ystep)
	if gridNum == 105:
		cellCoordinates = (10*xstep,9*ystep)
	if gridNum == 106:
		cellCoordinates = (11*xstep,9*ystep)
	if gridNum == 107:
		cellCoordinates = (12*xstep,9*ystep)
	#row 10
	if gridNum == 108:
		cellCoordinates = (1*xstep, 10*ystep)
	if gridNum == 109:
		cellCoordinates = (2*xstep, 10*ystep)
	if gridNum == 110:
		cellCoordinates = (3*xstep, 10*ystep)
	if gridNum == 111:
		cellCoordinates = (4*xstep, 10*ystep)
	if gridNum == 112:
		cellCoordinates = (5*xstep, 10*ystep)
	if gridNum == 113:
		cellCoordinates = (6*xstep, 10*ystep)
	if gridNum == 114:
		cellCoordinates = (7*xstep, 10*ystep)
	if gridNum == 115:
		cellCoordinates = (8*xstep, 10*ystep)
	if gridNum == 116:
		cellCoordinates = (9*xstep, 10*ystep)
	if gridNum == 117:
		cellCoordinates = (10*xstep,10*ystep)
	if gridNum == 118:
		cellCoordinates = (11*xstep,10*ystep)
	if gridNum == 119:
		cellCoordinates = (12*xstep,10*ystep)
	#row 11
	if gridNum == 120:
		cellCoordinates = (1*xstep, 11*ystep)
	if gridNum == 121:
		cellCoordinates = (2*xstep, 11*ystep)
	if gridNum == 122:
		cellCoordinates = (3*xstep, 11*ystep)
	if gridNum == 123:
		cellCoordinates = (4*xstep, 11*ystep)
	if gridNum == 124:
		cellCoordinates = (5*xstep, 11*ystep)
	if gridNum == 125:
		cellCoordinates = (6*xstep, 11*ystep)
	if gridNum == 126:
		cellCoordinates = (7*xstep, 11*ystep)
	if gridNum == 127:
		cellCoordinates = (8*xstep, 11*ystep)
	if gridNum == 128:
		cellCoordinates = (9*xstep, 11*ystep)
	if gridNum == 129:
		cellCoordinates = (10*xstep,11*ystep)
	if gridNum == 130:
		cellCoordinates = (11*xstep,11*ystep)
	if gridNum == 131:
		cellCoordinates = (12*xstep,11*ystep)
	#row 12
	if gridNum == 132:
		cellCoordinates = (1*xstep, 12*ystep)
	if gridNum == 133:
		cellCoordinates = (2*xstep, 12*ystep)
	if gridNum == 134:
		cellCoordinates = (3*xstep, 12*ystep)
	if gridNum == 135:
		cellCoordinates = (4*xstep, 12*ystep)
	if gridNum == 136:
		cellCoordinates = (5*xstep, 12*ystep)
	if gridNum == 137:
		cellCoordinates = (6*xstep, 12*ystep)
	if gridNum == 138:
		cellCoordinates = (7*xstep, 12*ystep)
	if gridNum == 139:
		cellCoordinates = (8*xstep, 12*ystep)
	if gridNum == 140:
		cellCoordinates = (9*xstep, 12*ystep)
	if gridNum == 141:
		cellCoordinates = (10*xstep,12*ystep)
	if gridNum == 142:
		cellCoordinates = (11*xstep,12*ystep)
	if gridNum == 143:
		cellCoordinates = (12*xstep,12*ystep)
	#row 13
	if gridNum == 144:
		cellCoordinates = (1*xstep, 13*ystep)
	if gridNum == 145:
		cellCoordinates = (2*xstep, 13*ystep)
	if gridNum == 146:
		cellCoordinates = (3*xstep, 13*ystep)
	if gridNum == 147:
		cellCoordinates = (4*xstep, 13*ystep)
	if gridNum == 148:
		cellCoordinates = (5*xstep, 13*ystep)
	if gridNum == 149:
		cellCoordinates = (6*xstep, 13*ystep)
	if gridNum == 150:
		cellCoordinates = (7*xstep, 13*ystep)
	if gridNum == 151:
		cellCoordinates = (8*xstep, 13*ystep)
	if gridNum == 152:
		cellCoordinates = (9*xstep, 13*ystep)
	if gridNum == 153:
		cellCoordinates = (10*xstep,13*ystep)
	if gridNum == 154:
		cellCoordinates = (11*xstep,13*ystep)
	if gridNum == 155:
		cellCoordinates = (12*xstep,13*ystep)
	#row 14
	if gridNum == 156:
		cellCoordinates = (1*xstep, 14*ystep)
	if gridNum == 157:
		cellCoordinates = (2*xstep, 14*ystep)
	if gridNum == 158:
		cellCoordinates = (3*xstep, 14*ystep)
	if gridNum == 159:
		cellCoordinates = (4*xstep, 14*ystep)
	if gridNum == 160:
		cellCoordinates = (5*xstep, 14*ystep)
	if gridNum == 161:
		cellCoordinates = (6*xstep, 14*ystep)
	if gridNum == 162:
		cellCoordinates = (7*xstep, 14*ystep)
	if gridNum == 163:
		cellCoordinates = (8*xstep, 14*ystep)
	if gridNum == 164:
		cellCoordinates = (9*xstep, 14*ystep)
	if gridNum == 165:
		cellCoordinates = (10*xstep,14*ystep)
	if gridNum == 166:
		cellCoordinates = (11*xstep,14*ystep)
	if gridNum == 167:
		cellCoordinates = (12*xstep,14*ystep)
	#row 15
	if gridNum == 168:
		cellCoordinates = (1*xstep, 15*ystep)
	if gridNum == 169:
		cellCoordinates = (2*xstep, 15*ystep)
	if gridNum == 170:
		cellCoordinates = (3*xstep, 15*ystep)
	if gridNum == 171:
		cellCoordinates = (4*xstep, 15*ystep)
	if gridNum == 172:
		cellCoordinates = (5*xstep, 15*ystep)
	if gridNum == 173:
		cellCoordinates = (6*xstep, 15*ystep)
	if gridNum == 174:
		cellCoordinates = (7*xstep, 15*ystep)
	if gridNum == 175:
		cellCoordinates = (8*xstep, 15*ystep)
	if gridNum == 176:
		cellCoordinates = (9*xstep, 15*ystep)
	if gridNum == 177:
		cellCoordinates = (10*xstep,15*ystep)
	if gridNum == 178:
		cellCoordinates = (11*xstep,15*ystep)
	if gridNum == 179:
		cellCoordinates = (12*xstep,15*ystep)
	#row 16
	if gridNum == 180:
		cellCoordinates = (1*xstep, 16*ystep)
	if gridNum == 181:
		cellCoordinates = (2*xstep, 16*ystep)
	if gridNum == 182:
		cellCoordinates = (3*xstep, 16*ystep)
	if gridNum == 183:
		cellCoordinates = (4*xstep, 16*ystep)
	if gridNum == 184:
		cellCoordinates = (5*xstep, 16*ystep)
	if gridNum == 185:
		cellCoordinates = (6*xstep, 16*ystep)
	if gridNum == 186:
		cellCoordinates = (7*xstep, 16*ystep)
	if gridNum == 187:
		cellCoordinates = (8*xstep, 16*ystep)
	if gridNum == 188:
		cellCoordinates = (9*xstep, 16*ystep)
	if gridNum == 189:
		cellCoordinates = (10*xstep,16*ystep)
	if gridNum == 190:
		cellCoordinates = (11*xstep,16*ystep)
	if gridNum == 191:
		cellCoordinates = (12*xstep,16*ystep)
	#row 17
	if gridNum == 192:
		cellCoordinates = (1*xstep, 17*ystep)
	if gridNum == 193:
		cellCoordinates = (2*xstep, 17*ystep)
	if gridNum == 194:
		cellCoordinates = (3*xstep, 17*ystep)
	if gridNum == 195:
		cellCoordinates = (4*xstep, 17*ystep)
	if gridNum == 196:
		cellCoordinates = (5*xstep, 17*ystep)
	if gridNum == 197:
		cellCoordinates = (6*xstep, 17*ystep)
	if gridNum == 198:
		cellCoordinates = (7*xstep, 17*ystep)
	if gridNum == 199:
		cellCoordinates = (8*xstep, 17*ystep)
	if gridNum == 200:
		cellCoordinates = (9*xstep, 17*ystep)
	if gridNum == 201:
		cellCoordinates = (10*xstep,17*ystep)
	if gridNum == 202:
		cellCoordinates = (11*xstep,17*ystep)
	if gridNum == 203:
		cellCoordinates = (12*xstep,17*ystep)
	#row 18	
	if gridNum == 204:
		cellCoordinates = (1*xstep, 18*ystep)
	if gridNum == 205:
		cellCoordinates = (2*xstep, 18*ystep)
	if gridNum == 206:
		cellCoordinates = (3*xstep, 18*ystep)
	if gridNum == 207:
		cellCoordinates = (4*xstep, 18*ystep)
	if gridNum == 208:
		cellCoordinates = (5*xstep, 18*ystep)
	if gridNum == 209:
		cellCoordinates = (6*xstep, 18*ystep)
	if gridNum == 210:
		cellCoordinates = (7*xstep, 18*ystep)
	if gridNum == 211:
		cellCoordinates = (8*xstep, 18*ystep)
	if gridNum == 212:
		cellCoordinates = (9*xstep, 18*ystep)
	if gridNum == 213:
		cellCoordinates = (10*xstep,18*ystep)
	if gridNum == 214:
		cellCoordinates = (11*xstep,18*ystep)
	if gridNum == 215:
		cellCoordinates = (12*xstep,18*ystep)
	#row 19
	if gridNum == 216:
		cellCoordinates = (1*xstep, 19*ystep)
	if gridNum == 217:
		cellCoordinates = (2*xstep, 19*ystep)
	if gridNum == 218:
		cellCoordinates = (3*xstep, 19*ystep)
	if gridNum == 219:
		cellCoordinates = (4*xstep, 19*ystep)
	if gridNum == 220:
		cellCoordinates = (5*xstep, 19*ystep)
	if gridNum == 221:
		cellCoordinates = (6*xstep, 19*ystep)
	if gridNum == 222:
		cellCoordinates = (7*xstep, 19*ystep)
	if gridNum == 223:
		cellCoordinates = (8*xstep, 19*ystep)
	if gridNum == 224:
		cellCoordinates = (9*xstep, 19*ystep)
	if gridNum == 225:
		cellCoordinates = (10*xstep,19*ystep)
	if gridNum == 226:
		cellCoordinates = (11*xstep,19*ystep)
	if gridNum == 227:
		cellCoordinates = (12*xstep,19*ystep)
	#row 20
	if gridNum == 228:
		cellCoordinates = (1*xstep, 20*ystep)
	if gridNum == 229:
		cellCoordinates = (2*xstep, 20*ystep)
	if gridNum == 230:
		cellCoordinates = (3*xstep, 20*ystep)
	if gridNum == 231:
		cellCoordinates = (4*xstep, 20*ystep)
	if gridNum == 232:
		cellCoordinates = (5*xstep, 20*ystep)
	if gridNum == 233:
		cellCoordinates = (6*xstep, 20*ystep)
	if gridNum == 234:
		cellCoordinates = (7*xstep, 20*ystep)
	if gridNum == 235:
		cellCoordinates = (8*xstep, 20*ystep)
	if gridNum == 236:
		cellCoordinates = (9*xstep, 20*ystep)
	if gridNum == 237:
		cellCoordinates = (10*xstep,20*ystep)
	if gridNum == 238:
		cellCoordinates = (11*xstep,20*ystep)
	if gridNum == 239:
		cellCoordinates = (12*xstep,20*ystep)
	#row 21
	if gridNum == 240:
		cellCoordinates = (1*xstep, 21*ystep)
	if gridNum == 241:
		cellCoordinates = (2*xstep, 21*ystep)
	if gridNum == 242:
		cellCoordinates = (3*xstep, 21*ystep)
	if gridNum == 243:
		cellCoordinates = (4*xstep, 21*ystep)
	if gridNum == 244:
		cellCoordinates = (5*xstep, 21*ystep)
	if gridNum == 245:
		cellCoordinates = (6*xstep, 21*ystep)
	if gridNum == 246:
		cellCoordinates = (7*xstep, 21*ystep)
	if gridNum == 247:
		cellCoordinates = (8*xstep, 21*ystep)
	if gridNum == 248:
		cellCoordinates = (9*xstep, 21*ystep)
	if gridNum == 249:
		cellCoordinates = (10*xstep,21*ystep)
	if gridNum == 250:
		cellCoordinates = (11*xstep,21*ystep)
	if gridNum == 251:
		cellCoordinates = (12*xstep,21*ystep)
	#row 22	
	if gridNum == 252:
		cellCoordinates = (1*xstep, 22*ystep)
	if gridNum == 253:
		cellCoordinates = (2*xstep, 22*ystep)
	if gridNum == 254:
		cellCoordinates = (3*xstep, 22*ystep)
	if gridNum == 255:
		cellCoordinates = (4*xstep, 22*ystep)
	if gridNum == 256:
		cellCoordinates = (5*xstep, 22*ystep)
	if gridNum == 257:
		cellCoordinates = (6*xstep, 22*ystep)
	if gridNum == 258:
		cellCoordinates = (7*xstep, 22*ystep)
	if gridNum == 259:
		cellCoordinates = (8*xstep, 22*ystep)
	if gridNum == 260:
		cellCoordinates = (9*xstep, 22*ystep)
	if gridNum == 261:
		cellCoordinates = (10*xstep,22*ystep)
	if gridNum == 262:
		cellCoordinates = (11*xstep,22*ystep)
	if gridNum == 263:
		cellCoordinates = (12*xstep,22*ystep)
	#row 23
	if gridNum == 264:
		cellCoordinates = (1*xstep, 23*ystep)
	if gridNum == 265:
		cellCoordinates = (2*xstep, 23*ystep)
	if gridNum == 266:
		cellCoordinates = (3*xstep, 23*ystep)
	if gridNum == 267:
		cellCoordinates = (4*xstep, 23*ystep)
	if gridNum == 268:
		cellCoordinates = (5*xstep, 23*ystep)
	if gridNum == 269:
		cellCoordinates = (6*xstep, 23*ystep)
	if gridNum == 270:
		cellCoordinates = (7*xstep, 23*ystep)
	if gridNum == 271:
		cellCoordinates = (8*xstep, 23*ystep)
	if gridNum == 272:
		cellCoordinates = (9*xstep, 23*ystep)
	if gridNum == 273:
		cellCoordinates = (10*xstep,23*ystep)
	if gridNum == 274:
		cellCoordinates = (11*xstep,23*ystep)
	if gridNum == 275:
		cellCoordinates = (12*xstep,23*ystep)
	#row 24	
	if gridNum == 276:
		cellCoordinates = (1*xstep, 24*ystep)
	if gridNum == 277:
		cellCoordinates = (2*xstep, 24*ystep)
	if gridNum == 278:
		cellCoordinates = (3*xstep, 24*ystep)
	if gridNum == 279:
		cellCoordinates = (4*xstep, 24*ystep)
	if gridNum == 280:
		cellCoordinates = (5*xstep, 24*ystep)
	if gridNum == 281:
		cellCoordinates = (6*xstep, 24*ystep)
	if gridNum == 282:
		cellCoordinates = (7*xstep, 24*ystep)
	if gridNum == 283:
		cellCoordinates = (8*xstep, 24*ystep)
	if gridNum == 284:
		cellCoordinates = (9*xstep, 24*ystep)
	if gridNum == 285:
		cellCoordinates = (10*xstep,24*ystep)
	if gridNum == 286:
		cellCoordinates = (11*xstep,24*ystep)
	if gridNum == 287:
		cellCoordinates = (12*xstep,24*ystep)


	pasteUpperleft =  (  (daycoords[0]+cellCoordinates[0]-xstep)+2    ,  (daycoords[1]+cellCoordinates[1] - ystep)+2,  gridNum)
	#pasteUpperright = ( (daycoords[0]+cellCoordinates[0]+xstep)  ,  daycoords[1]+cellCoordinates[1])
	#pasteLowerleft =  (  daycoords[0]+cellCoordinates[0]         , (daycoords[1]+cellCoordinates[1]+ystep))
	#pasteLowerright = ( (daycoords[0]+cellCoordinates[0]+xstep)  ,  daycoords[1]+cellCoordinates[1]+ystep)

	return  pasteUpperleft













