import numpy as np

def softmax(x):
    #compute softmax and return
            
scores = [3.0, 1.0, 0.2]
print(softmax(scores))
                  
# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
                                 
plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
