from datetime import datetime

def printtime(start=True):
    startmsg = "Starttijd: "
    endmsg = "Eindtijd: "
    if start:
        message = startmsg
    else:
        message = endmsg

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("X" * 40)
    line = " " + message + current_time + " "
    print("X{:X^38}X".format(line))
    print("X" * 40)