import h5py
import numpy as np
# This is simple program to read the Advanced Microwave Scanning Radiometer 2 (AMSR2)  satellite data containing the Brightness Temperature.
# Then, you can use the GMT to plot data in map easily.

# Data was downloaded from https://gportal.jaxa.jp/gpr/
# Author: Lei  Yang, FIO, China
# leiyang@fio.org.cn

with h5py.File('GW1AM2_201912110435_218A_L1SGBTBR_2220220.h5', "r") as f:
    for key in f.keys():
        print(key)  # f[key] means a dataset or a group object. f[key].value visits dataset' value,except group object
    dset = f['Brightness Temperature (89.0GHz-B,V)']
    dseth = f['Brightness Temperature (89.0GHz-A,H)']
    blat = f['Latitude of Observation Point for 89B']
    blon = f['Longitude of Observation Point for 89B']

    # print(blon.shape)
    # print(blon.name)
    # print(blon.dtype)

    a = np.ones(blon.shape)
    b = np.ones(blon.shape)
    c = np.ones(blon.shape)
    d = np.ones(blon.shape)

    blat.read_direct(a)
    outlat = a.reshape(2041 * 486)

    dset.read_direct(b)
    outdset = b.reshape(2041*486)

    dseth.read_direct(d)
    outseth = d.reshape(2041*486)

    blon.read_direct(c)
    outlon = c.reshape(2041 * 486)

    print('==========================================================================================')
    print(outlon[1:100])
    print(outdset[1:100])
    print(outlat[1:100])
    print('==========================================================================================')

    outdata = np.column_stack((outdset, outseth, outlat, outlon))
    print(type(outdata), outdata.shape, outdata[1, 0:4])

np.savetxt("output.npy", outdata, fmt="%10.1f", delimiter=",")

f.close()

