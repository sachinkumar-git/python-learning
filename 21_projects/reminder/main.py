import time   
from plyer import notification # importing notification from plyer module

while True:
    print("keep working hard!")  
    notification.notify(title="you can do it!", 
                        message = "You're doing great!",)
    time.sleep(60*60)  # Notify every hour