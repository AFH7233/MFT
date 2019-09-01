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
		print "Distance:%.3f, X:%.3f, Snap:%.3f, Alpha:%.3f, F:%.3f"%(
			user_distance, x, snap, alpha, f)

def create_mtf(name, width, height, screen, distance_user):
	out = cv.CreateImage((width, height), 8, 1)

	b = math.log(width/2.0)/width
	a = 1.0/(b*width)

	d = 0.02
	c = math.log(d)/height

	x_vector = [0.5+0.5*math.sin(2*math.pi* a*math.e**(b*val) ) for val in 
		xrange(width)]
	y_vector = [d*math.e**(-c*val) for val in xrange(height)]

	for i in xrange(width):
		for j in xrange(height):
			out[j,i] = 255.0*(x_vector[i])*y_vector[j]

	cv.ShowImage("mtf", out)
	cv.MoveWindow("mtf", 0, 0)

	cv.SetMouseCallback("mtf", user_x, [width,height,a,b,screen,distance_user])

	cv.SaveImage("mtf.png", out)
	cv.WaitKey(0)

if __name__=="__main__":
	size = 728
	screen_cm = 13.0
	distance_user_cm = 100.0
	create_mtf("out.png", size, size, screen_cm, distance_user_cm)


#1 zapato sin lentes
#Distance:30.000, X:315.000, Snap:0.018, Alpha:6.779, F:8.371
#Distance:60.000, X:250.000, Snap:0.010, Alpha:4.718, F:20.364
#Distance:100.000, X:325.000, Snap:0.019, Alpha:3.207, F:16.316

#2 zapato con lentes
#Distance:30.000, X:317.000, Snap:0.018, Alpha:6.779, F:8.236
#Distance:60.000, X:367.000, Snap:0.027, Alpha:4.718, F:7.893
#Distance:100.000, X:327.000, Snap:0.019, Alpha:3.207, F:16.054

#4
#Distance:30.000, X:245.000, Snap:0.010, Alpha:6.779, F:14.758
#Distance:60.000, X:250.000, Snap:0.010, Alpha:4.718, F:20.364
#Distance:100.000, X:245.000, Snap:0.010, Alpha:3.207, F:31.193

#3 yo sin lentes
#Distance:30.000, X:416.000, Snap:0.040, Alpha:6.779, F:3.694
#Distance:60.000, X:409.000, Snap:0.038, Alpha:4.718, F:5.617
#Distance:100.000, X:357.000, Snap:0.025, Alpha:3.207, F:12.590

#3 yo con lentes
#Distance:30.000, X:375.000, Snap:0.029, Alpha:6.779, F:5.149
#Distance:60.000, X:398.000, Snap:0.035, Alpha:4.718, F:6.140
#Distance:100.000, X:403.000, Snap:0.036, Alpha:3.207, F:8.674
