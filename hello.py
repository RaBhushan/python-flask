
import re  

msg = 'Hello World'
msg.strip
print(msg)

test = '1Rahul1' 

name = re.match("[a-zA-Z]+", test)

if name:
    print("name coantiane only alphabets ${test}")
else:
     print("name does not containes only alphabets ${test}")   

# import matplotlib.pyplot as plt

# import numpy as np

# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot