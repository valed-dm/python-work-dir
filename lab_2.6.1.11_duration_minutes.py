hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

print(str((hour + dura // 60 + (mins + dura % 60) // 60) %
      24) + " : " + str((mins + dura % 60) % 60))
