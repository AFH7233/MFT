import cv
import math

def user_x(event,x,y,flags,param):
	if event == cv.CV_EVENT_LBUTTONDOWN:
		param = map(float, param)
		n_pixels = param[0]
		a = param[2]
		b = param[3]
		screen_size = param[4]
		user_distance = param[5]

		snap = a*b*math.e**(b*x)
		d = screen_size/n_pixels
		alpha = math.atan(d/user_distance)*(180.0/math.pi)
		f = snap/alpha
		print "Distance:%.3f, X:%.3f, Snap:%.3f, Alpha:%.3f, F:%.3f"%(
			user_distance, x, snap, alpha, f)

def create_mtf(name, width, height, screen, distance_user):
	out = cv.CreateImage((width, height), 8, 1)

	b = math.log(width/2.0)/width
	a = 1.0/(b*width)

	d = 0.01
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



#Distance:30.000, X:513.000, Snap:0.088, Alpha:0.034, F:2.569
#Distance:60.000, X:430.000, Snap:0.045, Alpha:0.017, F:2.623
#Distance:100.000, X:359.000, Snap:0.025, Alpha:0.010, F:2.460

#Distance:30.000, X:627.000, Snap:0.221, Alpha:0.034, F:6.469
#Distance:60.000, X:541.000, Snap:0.110, Alpha:0.017, F:6.446
#Distance:100.000, X:475.000, Snap:0.064, Alpha:0.010, F:6.295

#Distance:30.000, X:498.000, Snap:0.078, Alpha:0.034, F:2.275
#Distance:60.000, X:418.000, Snap:0.041, Alpha:0.017, F:2.380
#Distance:100.000, X:358.000, Snap:0.025, Alpha:0.010, F:2.440

