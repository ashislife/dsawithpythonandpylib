# import numpy as np
# from scipy.stats import norm
# Data = [1,2,3,4,5,6,7,8,9,10]

# #first moment mean 
# Mean=np.mean(Data)




# # Second moment mean 
# Variance =np.var(Data)

# #output /Results
# print(f"Data :(first moment) :{Mean}")
# print(f"Variance :(Second central moment) :{Variance}")




from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
#probability function 
#PDF-->Probability density function 
#CDF-->Cumulative Distribution Function
np.set_printoptions(precision=4) # Print arrays to 4 decimal places  

#make a t distribution object for t with 20 degrees of freedom 

t_dist=stats.t(20)
#plot the PDF 
t_values= np.linspace(-4,4,1000)
plt.plot (t_values ,t_dist.pdf(t_values))
plt.xlabel('t values')
plt.ylabel('Probability for t values')
plt.title('PDF for t distribution with df=20')
plt.show()

#plot the CDF
plt.plot(t_values,t_dist.cdf(t_values))
plt.xlabel('t values')
plt.ylabel('Probability for t value<=t')
plt.title('CDF for t distribution with df=20')
plt.show()

