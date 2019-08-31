import cv2 as cv
#import cv
import math
from random import randint


#cv2.imwrite

#h,w
#Size = [768,1024]
#MFT = np.zeros(Size)


#Xpixels = np.arange(Size[1])
#Ypixels = np.arange(Size[0])

#Frecuency_B = np.log((Size[1]/2))/Size[1]
#Frecuency_A = 1/(Frecuency_B*Size[1])

def create_mtf(name, width, height):
	out = cv.CreateImage((width, height), 8, 1)

	b = math.log(width/2.0)/width
	a = 1.0/(b*width)

	print a,b

	x_vector = [0.5+0.5*math.sin(2*math.pi* a*math.e**(b*val) ) for val in xrange(width)]
	y_vector = [math.e**((-6.0*val)/height) for val in xrange(height)]

#	x_vector = [math.sin( .25*math.pi*val*val/width ) for val in xrange(width)]
#	x_vector = [math.sin(0.5* math.e**(val)/width ) for val in xrange(width)]

#	print x_vector
#	print y_vector#inicia [1,..., 0.018]

	for i in xrange(width):
		for j in xrange(height):
#			out[j,i] = y_vector[j]*x_vector[i]
			out[j,i] = 255.0*(x_vector[i])*y_vector[height-1 - j]
#			out[j,i] = 255*y_vector[height-1 - j]
#		print out[j,i]

	cv.ShowImage("mtf", out)
	cv.MoveWindow("mtf", 0, 0)
	cv.SaveImage("mtf.png", out)
	cv.WaitKey(0)




if __name__=="__main__":
	create_mtf("out.png", 720, 720)

