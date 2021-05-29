seconds = 1
minutes = 1
hours = 12
import time

while True:
     print(str(hours)+":"+str(minutes) + ":" + str(seconds))
     seconds = seconds + 1
     time.sleep(1)
     if seconds == 60:
          seconds = 0
          minutes = minutes +1
          if minutes == 60:
               minutes = 0
               hours = hours +1
     

          
     
     
