from pynput.keyboard import Key, Listener
import subprocess

settings = 1
detect = 0
def show(key):
	global settings
	global detect
	
	settings = settings - 0.2
	

	if settings <= 0 and detect == 0:
		settings = 1
		detect = 1
		
	if settings <= 0 and detect == 1:
		detect = 0
		settings = 0
	 
	if str(key) == "<0>":
		popen = subprocess.Popen("xrandr --verbose --output DP1 --brightness {}".format(settings), stdout = subprocess.PIPE, shell = True, encoding = 'utf8')
  
	if key == Key.delete:
        # Stop listener
		return False
  
# Collect all event until released
with Listener(on_press = show) as listener:   
    listener.join()
