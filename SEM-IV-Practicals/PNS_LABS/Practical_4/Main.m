clc;
clear all;
close all;

#x=[0 , -2 , -1 , 3 , -4 , -2 , -1 , 2 ];
#y=[-1 , 3 , -4];

#a = legnt(x)/legnth(y):
a=audioread('1.wav');
b=audioread('2.wav');
c=audioread('3.wav');
d=audioread('4.wav');
e=audioread('5.wav');
f=audioread('6.wav');
g=audioread('7.wav');
h=audioread('7.wav');
i=audioread('8.wav');
j=audioread('9.wav');
k=audioread('0.wav');

x=[j;d;b;j;d;c;d;b;k;a];
y=j;
for i=1:length(x)-length(y)+1
  #r(i)=x(i)*y(1)+x(i+1)*y(2)+x(i+2)*y(3);
  r(i)=sum(y.*x(i:i+length(y)-1));
end

#r
ind=find(r==max(r));
ind

subplot(3,1,1)
plot(x)
subplot(3,1,2)
plot(y)
subplot(3,1,3)
plot(r)
