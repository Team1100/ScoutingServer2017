from server import server
import thread



for index in range(6):
    thread.start_new_thread(server, (index,))
while True:
    raw_input()