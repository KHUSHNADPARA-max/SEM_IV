clc;
close all;
clear all;

# PDF TO CDF
dx=0.01;
x = -10 :dx: 10;
sig = 1;
u = 0;
for i=1:length(x)
  y = (1 / (sig * sqrt(2 * pi))) * exp(-((x - u).^2)/(2 * sig * sig));
endfor
pdf = y*dx;

for i=1:length(x)
  cdf(i) = sum(pdf(1:i));
endfor
plot(x,y);
grid on;
xlabel('x');
ylabel('y');

#PDF TO MEAN
mean=0;
for i=1:length(x)
  mean=mean+(x(i)*pdf(i));
endfor
mean

#PDF TO VAR
mean2=0;
for i=1:length(x)
  mean2=mean2+(x(i)*x(i)*pdf(i));
endfor
mean2
var = mean2-(mean^2)
