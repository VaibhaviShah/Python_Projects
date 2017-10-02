import time
import webbrowser

total_breaks = 3
break_count = 0

print("Study time started at: " + str(time.ctime()))
while (break_count <= total_breaks):
    time.sleep(2)
    webbrowser.open("www.gmail.com")
    print("")
    break_count += 1

