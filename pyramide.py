blocks = int(input("Enter the number of blocks: "))
used_blocks = 0
height = 0

#i = 0
#for i in range(blocks):
#    if (blocks - used_blocks) >= (height + 1):
#        used_blocks += (i + 1)
#        height += 1
#    else:
#        break

while (blocks - used_blocks) >= (height  + 1):
    height += 1
    used_blocks += height

print("The height of the pyramid: " + str(height) + ".")
print("blocks used: " + str(used_blocks) + ".")
