#linear regression new; self-learnt
"""program for implementing linear regression 
to the 'Open' and 'Last' stocks data of a particular 
company through quandl using mean square error"""


import numpy as np
import quandl
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    ss_xy = np.sum(x*y) - n*m_x*m_y
    ss_xx = np.sum(x*x) - n*(m_x*m_x)
    b_1 = ss_xy/ss_xx
    b_0 = m_y - b_1*m_x
    print("estimated coefficients b_1 and b_0=",b_1,b_0)
    return(b_0,b_1)

def plot_line(x,y,b):
    plt.scatter(x, y, color='green', s=1)
    y_pred = b[0] + b[1]*x
    plt.plot(x,y_pred,color = 'blue')
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()
def main():
    quandl.ApiConfig.api_key = "fxKHFnEiFCQ2zDqu-HCz"
    df = quandl.get('EURONEXT/MSF')
    x = np.array(df['Open'])
    y = np.array(df['Last'])
    
    b=estimate_coef(x,y)
    plot_line(x, y, b)
    
if __name__ == "__main__": 
    main()
