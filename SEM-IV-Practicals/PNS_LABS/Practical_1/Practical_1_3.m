clc;
clear all;
close all;
n = input('enter the value of n : ');
nPr=zeros(1,n+1);
r= 0:n;
for i=0:n nPr(i+1)=fn_fact(n)/fn_fact(n-i);
  printf("\n%dp%d= %d\n",n,i,nPr(i+1));
endfor
plot(r,nPr,"r*","Markersize",15) title("r  Vs nPr","fontsize",30) xlabel("r variable","fontsize",25) ylabel("nPr","fontsize",25)
