from matplotlib import pyplot as plt
import numpy as np
import itertools

def hamming_weight(byte):
    hw = 0
    for bit in byte:
        if bit == 1:
            hw += 1

    return hw
    
if __name__ == "__main__":
    # I think this array contains 75 plaintexts that were encrypted
    # each plaintext is 16 bytes long?
    plaintext = np.load("plaintexts.npy")
    print "plaintext array dimensions: " + str(plaintext.shape)
    # array dimensions (75, 16)

    # I think this array contains power samples for 75 AES encryptions
    power = np.load("powertraces.npy")
    # array dimensions (75, 3000)
    print "powertraces array dimensions: " + str(power.shape)

    # 16 * 8 = 128 bits
    # 3000 / 128 = 23.4 samples per bit?

    mp = np.mean(power, axis=0)

    # partition the power sample array into two parts
    #power1, power2 = np.array_split(power, 2)

    #mp1 = np.mean(power1, axis=0)
    #mp2 = np.mean(power2, axis=0)
    #delta = mp1 - mp2

    # create a lookup table of hamming weights for all possible byte values
    bytevalues = itertools.product([0, 1], repeat=8)
    ham = list()
    for value in bytevalues:
        ham.append(hamming_weight(value))
    #print ham


    


    plt.title("mean power")
    plt.plot(mp)
    plt.show()
