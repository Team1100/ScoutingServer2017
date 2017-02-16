from bluetooth import *
from writer import write

def getUUID(index):
    return{
        0 : "551371ae-9714-41ca-8bcc-12651809e863",
        1 : "1426babc-2df2-429e-9233-f84435154fa2",
        2 : "27bb9a0e-b772-4cde-96b9-74e7ffd1b679",
        3 : "e4283b54-0e8f-4a5f-b2c2-dafdce12b75e",
        4 : "6632b275-da16-403c-a95f-b5b9024248b1",
        5 : "1f5733c5-4511-4f87-83d4-2973cd876674"
    }.get(index,"551371ae-9714-41ca-8bcc-12651809e863")

def server(index):
    while True:
        server_sock = BluetoothSocket(RFCOMM)
        server_sock.bind(("", index+1))
        server_sock.listen(1)
        port = server_sock.getsockname()[1]

        uuid = getUUID(index)

        advertise_service(server_sock, "ScoutServer"+str(index+1),
                          service_id=uuid,
                          service_classes=[uuid, SERIAL_PORT_CLASS],
                          profiles=[SERIAL_PORT_PROFILE],
                          )
        print("Waiting for connection on RFCOMM channel %d\n" % port)

        client_sock, client_info = server_sock.accept()
        print("Accepted connection from ", client_info)
        info = ""
        try:
            while True:
                data = client_sock.recv(15000)
                if len(data) == 0:
                    break
                info+=data
        except IOError:
            pass
        print info
        write(info)
        print("disconnected")

        client_sock.close()
        server_sock.close()