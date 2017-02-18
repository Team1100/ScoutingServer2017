from server import *
import thread

for index in range(6):
    thread.start_new_thread(server, (index,))
thread.start_new_thread(pitServer())
while True:
    raw_input()