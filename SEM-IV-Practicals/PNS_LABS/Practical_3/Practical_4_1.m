clc;
clear all;
close all;

x1 = audioread('Khush.wav');
y = x1(7000:10000);
z = length(x1) - length(y) + 1;
r = [];

for i=1:z
  d = sum(x1(i:i+length(y)-1).*y);
  r=[r d];
endfor

index=find(r==max(r));


plot(x1)
figure
plot(y)
figure
plot(r)
