clc;
clear all;
close all;

A = xlsread('test.xlsx', 'Sheet1');
x = A(:,1);
y = A(:,2);

#x=[1 2 3 4 5 6 7];
#y=[9 8 10 12 11 13];

n=length(x);

a = ((n*sum(x.*y))-(sum(x)*sum(y))) / ((n*sum(x.*x))-(sum(x)*sum(x)));
b=mean(y)-(a*mean(x));

a
b
#printf(" a = %d\n", (a));
#printf(" b = %d\n", (b));

x_plt = min(x):0.01:max(x);
y_plt = (a*x_plt) + b;

plot(x_plt, y_plt)

hold on
plot(x, y, "r*")
