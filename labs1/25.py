time = int(input())
day = time/(24*3600)
hour = (time % (24*3600))/3600
minutes = ((time % (24*3600)) % 3600)/60
seconds = ((time % (24*3600)) % 3600) % 60
print("d:h:m:s-> %d:%02d:%02d:%02d" % (day, hour, minutes, seconds))
