clc;
clear all;
close all;

n = input('enter the value of n : ');
nCr=zeros(1,n+1);
r= 0:n;
for i=0:n nCr(i+1)=fn_fact(n)/(fn_fact(n-i)*fn_fact(i));
  printf("\n%dC%d= %d\n",n,i,nCr(i+1));
endfor
plot(r,nCr,"r-","Markersize",15) title("r  Vs nCr","fontsize",30) xlabel("r variable","fontsize",25) ylabel("nCr","fontsize",25)

