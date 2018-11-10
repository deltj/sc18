import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    power = np.load("powertraces.npy")
    plaintext = np.load("plaintexts.npy")
    
    print "powertraces array dimensions: " + str(power.shape)
    print "plaintext array dimensions: " + str(plaintext.shape)

    meanpower = np.mean(power, axis=0)

    #print plaintext

    plt.title("mean power")
    plt.plot(meanpower)
    plt.show()
