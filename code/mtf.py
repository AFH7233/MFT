import cv
import math
from random import randint


def user_x(event,x,y,flags,param):
	if event == cv.CV_EVENT_LBUTTONDOWN:
		param = map(float, param)
		n_pixels = param[0]
		a = param[2]
		b = param[3]
		screen_size = param[4]
		user_distance = param[5]

		snap = a*b*math.e**(b*x)
		d = n_pixels/screen_size
		alpha = math.atan(d/user_distance)*2.0*math.pi
		f = 1.0/(snap*alpha)
#		print x,y, param, snap, 1.0/(snap*alpha)
		print "Distance:%.3f, X:%.3f, Snap:%.3f, Alpha:%.3f, F:%.3f"%(user_distance, x, snap, alpha, f)



def create_mtf(name, width, height, screen, distance_user):
	out = cv.CreateImage((width, height), 8, 1)

	b = math.log(width/2.0)/width
	a = 1.0/(b*width)
#	print a,b

	x_vector = [1.0+math.sin(2*math.pi* a*math.e**(b*val) ) for val in xrange(width)]
	y_vector = [math.e**((-8.0*val)/height) for val in xrange(height)]

	for i in xrange(width):
		for j in xrange(height):
			out[j,i] = 255.0*(x_vector[i])*y_vector[height-1 - j]

	cv.ShowImage("mtf", out)
	cv.MoveWindow("mtf", 0, 0)

	cv.SetMouseCallback("mtf", user_x, [width,height,a,b,screen,distance_user])

	cv.SaveImage("mtf.png", out)
	cv.WaitKey(0)


if __name__=="__main__":
	size = 728
	screen_cm = 13.0
	distance_user_cm = 70.0
	create_mtf("out.png", size, size, screen_cm, distance_user_cm)

