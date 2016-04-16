import numpy as np
import scipy.integrate as spIn
import matplotlib.pyplot as plt

def ode(y,t,a,b):
    y0, y1 = y
    dydt = [a*(y0 - y0*y1),b*(-y1+y0*y1)]
    return dydt

if __name__ == "__main__":

    # part 1
    # initial value for y0 and y1 and the value for a and b
    a = 1.0
    b = 0.2
    ini_y0 = 0.1
    ini_y1 = 1.0
    ini_y = [ini_y0,ini_y1]
    
    # breaking down the time from t = 0 to 5 into 100 uniform partition
    t = np.linspace(0, 5, 101)
    
    #solving the nonlinear ODE system
    sol = spIn.odeint(ode,ini_y,t,args=(a,b))

    # plotting the graph for y0 and y1 against t
    plt.plot(t, sol[:, 0], 'b', label='Prey y0 against t')
    plt.plot(t, sol[:, 1], 'g', label='Predator y1 against t')
    plt.title('Graph of y against t with initial_y0 = 0.1')
    plt.legend(loc='best')
    plt.xlabel('Year t')
    plt.ylabel('y')
    plt.grid()
    plt.savefig('Graph_of_y0_and_y1_01.jpg')
    plt.show()
    
    # plotting the graph for y1 against y0
    plt.plot(sol[:, 0],sol[:,1], 'b', label='Predator y1 against Prey y0')
    plt.title('Predator y1 against Prey y0 with initial_y0 = 0.1')
    plt.legend(loc='best')
    plt.xlabel('Prey y0')
    plt.ylabel('Predator y1')
    plt.grid()
    plt.savefig('Graph_of_y1_against_y0_01.jpg')
    plt.show()
    
    ######################################################################

    # part 2 
    # initial value for y0 and y1 and the value for a and b
    a = 1.0
    b = 0.2
    
    # different initial value for initial_y0
    ini_y0 = 0.11
    ini_y1 = 1.0
    ini_y = [ini_y0,ini_y1]
    
    # breaking down the time from t = 0 to 5 into 100 uniform partition
    t = np.linspace(0, 5, 101)
    
    #solving the nonlinear ODE system
    sol = spIn.odeint(ode,ini_y,t,args=(a,b))

    # plotting the graph for both y0 and y1 against t
    plt.plot(t, sol[:, 0], 'b', label='Prey y0 against t')
    plt.plot(t, sol[:, 1], 'r', label='Predator y1 against t')
    plt.title('y against t with initial_y0 = 0.11')
    plt.legend(loc='best')
    plt.xlabel('Year t')
    plt.ylabel('y')
    plt.grid()
    plt.savefig('Graph_of_y0_and_y1_02.jpg')
    plt.show()
    
    # plotting the graph for y1 against y0
    plt.plot(sol[:, 0],sol[:,1], 'r', label='Predator y1 against Prey y0')
    plt.title('Predator y1 against Prey y0 with initial_y0 = 0.11')
    plt.legend(loc='best')
    plt.xlabel('Prey y0')
    plt.ylabel('Predator y1')
    plt.grid()
    plt.savefig('Graph_of_y1_against_y0_02.jpg')
    plt.show()