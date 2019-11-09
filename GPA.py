#!/usr/bin/env python3

# pip install matplotlib
import matplotlib.pyplot as plt 
import numpy as np 


#calculating any semester 1.0 F17 GPA
#cg=3.11; # Current Cum GPA
#bc=6; #Current Semester Credits
#cc=101; #Current Cum Credits Taken
cg=3.445
bc=16
cc=86

m=bc/(bc+cc)
b=cc*cg/(bc+cc)
#x=0:0.01:4
x = np.linspace(0,4,1000)
y= x*m+b
D=x*0+cg

plt.plot(x,y)
plt.plot(cg,cg)
plt.plot(x,D)

plt.xlabel('Semester GPA')
plt.ylabel('Resulting Cumulative GPA')
plt.title('Spring 19 GPA')
#plt.legend('Projection','Current','Money')
#plt.xlim([3.5,4])
#plt.ylim([3.6,3.8])
plt.grid(True)



plt.show()

# x = np.linspace(0, 6 * np.pi, 1000)
# y = np.sin(x)
# plt.plot(x, np.sin(x))
# plt.show()

# def update(hello):
#     pass

# calculating any semester 1.0 F17 GPA
# clear,clc,clf
# cg=2.98; % Current Cum GPA
# bc=12; %Current Semester Credits
# cc=80; %Current Cum Credits Taken
# m=bc/(bc+cc);
# b=cc*cg/(bc+cc);
# x=0:0.01:4;
# y=@(x) x*m+b;
# D=@(x) x*0+3; 
# plot(x,y(x),'linewidth',2),hold on
# plot(cg,cg,'o','linewidth',2)
# plot(x,D(x),'g')
# xlabel('Semester'),ylabel('Resulting Cummulative')
# legend('Projection','Current','Money'),title('Fall 17 GPA')
# xlim([2,4]),grid on



# sarah spring 2019 term gpa calculation
ss19=((2*3.67)+(4*4))/6
print('real',ss19)
print('hello')