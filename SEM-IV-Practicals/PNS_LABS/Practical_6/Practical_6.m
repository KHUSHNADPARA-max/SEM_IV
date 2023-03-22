clc;
clear all;
close all;

#x = [1 2 3 4 5 6 7];
#y = [9 8 10 12 11 13 14];

x = [1 2 3];
y = [3 2 1];

a = 0.9286;
b = 7.28;

plot(x, y, "r*")
hold on

x_plt = min(x) : 0.01 : max(x);
y_plt = (a * x_plt) + b;
plot(x_plt, y_plt)


#x is 123 and y is 123
