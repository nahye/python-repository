Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> t.shape("turtle")
>>> from turtle import *
>>> color('yellow', 'pink')
>>> begin_fill()
>>> while True:
	forward(250)
	left(220)
	if abs(pos()) < 1:
		break

	
>>> end_fill()
>>> done()
