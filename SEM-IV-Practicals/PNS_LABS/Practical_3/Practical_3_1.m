clc;
clear all;
close all;

dx = 0.1;
x=-20:dx:20;
s=3;
m=0;

for i=1:length(x)
  y(i) = (1/sqrt(2*pi*s*s))*exp(-(x(i)-m)^2/(2*s*s));
endfor
pdf = y * dx;

for i = 1:length(x)
    cdf(i) = sum(pdf(1:i));
endfor

subplot(2,1,1);
plot(x,pdf)
subplot(2,1,2);
plot(x,cdf)

mean = 0

for i=1:length(x)
  mean=mean+(x(i)*pdf(i));
endfor

mean

x2m;
var=x2m-(mean*2);

