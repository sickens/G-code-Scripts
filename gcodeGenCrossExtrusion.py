width = int(input('Input width(mm):'))
ext = int(input('Input amount of extrusion(mm): '))
layers = int(input('Input number of layers: '))
z_gap = float(input('Input Z gap(mm): '))
speed = input('Input speed(mm/min): ')

j = 0

for i in range(int(layers)):
    print('G1   X' + str(0)           + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*1+ext) + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*1)     + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*1)     + ' Y' + str(width*7+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*1)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*2+ext) + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*2)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*2)     + ' Y' + str(-ext)        + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*2)     + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*3+ext) + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*3)     + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*3)     + ' Y' + str(width*7+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*3)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*4+ext) + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*4)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*4)     + ' Y' + str(-ext)        + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*4)     + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*5+ext) + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*5)     + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*5)     + ' Y' + str(width*7+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*5)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*6+ext) + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*6)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*6)     + ' Y' + str(-ext)        + ' Z' + str(j*z_gap) + ' F' + speed)
    j += 1
    print('G1   X' + str(width*6)     + ' Y' + str(-ext)        + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*6)     + ' Y' + str(width*7+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*6)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*5-ext) + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*5)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*5)     + ' Y' + str(-ext)        + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*5)     + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*4-ext) + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*4)     + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*4)     + ' Y' + str(width*7+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*4)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*3-ext) + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*3)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*3)     + ' Y' + str(-ext)        + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*3)     + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*2-ext) + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*2)     + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*2)     + ' Y' + str(width*7+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*2)     + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width-ext)   + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width)       + ' Y' + str(width*7)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width)       + ' Y' + str(-ext)        + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width)       + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)        + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    j += 1
    print('G1   X' + str(0)           + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*1+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*1)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7+ext) + ' Y' + str(width*1)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*1)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*2+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*2)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)        + ' Y' + str(width*2)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*2)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*3+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*3)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7+ext) + ' Y' + str(width*3)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*3)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*4+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*4)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)        + ' Y' + str(width*4)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*4)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*5+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*5)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7+ext) + ' Y' + str(width*5)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*5)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*6+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*6)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)        + ' Y' + str(width*6)     + ' Z' + str(j*z_gap) + ' F' + speed)
    j += 1
    print('G1   X' + str(-ext)        + ' Y' + str(width*6)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7+ext) + ' Y' + str(width*6)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*6)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*5-ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*5)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)        + ' Y' + str(width*5)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*5)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*4-ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*4)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7+ext) + ' Y' + str(width*4)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*4)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*3-ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*3)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)        + ' Y' + str(width*3)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*3)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*2-ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width*2)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7+ext) + ' Y' + str(width*2)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width*2)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width-ext)   + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(width*7)     + ' Y' + str(width)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)        + ' Y' + str(width)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(width)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(-ext)        + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)           + ' Y' + str(0)           + ' Z' + str(j*z_gap) + ' F' + speed)
    j += 1
input("Press enter to exit") 
    