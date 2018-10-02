# Built-in imports
from platform import system as plat
import subprocess as sp

# Our imports
from config import SharedCfg, PingCfg

# Get system type and setup the ping command
if plat().lower() == "windows":
    pingCommand = ""  # TODO
else:
    pingCommand = "ping -c " + str(PingCfg.PING_ATTEMPTS) + " "  # Follow this with the ip/hostname

for ip in PingCfg.PING_TARGETS:
    if SharedCfg.DEBUG_MODE:
        print(pingCommand + ip)  # Print the command
    proc = sp.Popen([pingCommand + ip], stdout=sp.PIPE, shell=True)  # Run the command and...
    (out, err) = proc.communicate()  # ...get the output
    outStr = out.decode()

    pre_percent = "packets received, "
    post_percent = "% packet loss"
    startLocationOfPercent = outStr.find(pre_percent) + len(pre_percent)
    endLocationOfPercent = outStr.find(post_percent)
    percentStr = outStr[startLocationOfPercent:endLocationOfPercent]

    percentLost = round(float(percentStr))
    percent = 100 - percentLost

    if percent > PingCfg.PERCENT_SUCCESS_FOR_UP:
        print('Host "', ip, '" is UP. It responded to ', percent, '% of pings.', sep='')
    else:
        print('Host "', ip, '" is DOWN. It responded to ', percent, '% of pings.', sep='')
