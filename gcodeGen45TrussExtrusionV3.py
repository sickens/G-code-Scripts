#path optimized
len = int(input('Input side length of triangle(mm): '))
##tri = int(input('Input number of base triangles: '))
ext = int(input('Input amount of extrusion(mm): '))
layers = int(input('Input number of layers: '))
z_gap = float(input('Input Z gap(mm): '))
speed = input('Input speed(mm/min): ')

j = 0

for i in range(int(layers)):
    print('G1   X' + str(0)         + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len+ext)   + ' Y' + str(len+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(-ext)    + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2+ext) + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(len+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3+ext) + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(-ext)    + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*4+ext) + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*4)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    j+=1
    print('G1   X' + str(len*4)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3-ext) + ' Y' + str(len+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(-ext)    + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2-ext) + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(len+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len-ext)   + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(-ext)    + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)      + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)         + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    j+=1
    print('G1   X' + str(0)         + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len+ext)   + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(len+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2+ext) + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(-ext)    + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3+ext) + ' Y' + str(len+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(-ext)    + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*4+ext) + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*4)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    j+=1
    print('G1   X' + str(len*4)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3-ext) + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(len+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*3)     + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2-ext) + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(-ext)    + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len*2)     + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len-ext)   + ' Y' + str(len+ext) + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(len)     + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(-ext)    + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(len)       + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(-ext)      + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    print('G1   X' + str(0)         + ' Y' + str(0)       + ' Z' + str(j*z_gap) + ' F' + speed)
    j+=1
input("Press enter to exit")