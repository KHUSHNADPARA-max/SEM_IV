clc;
clear all;
close all;

n = 100;
x = rand(1,n);
y = 3 * rand(1,n);

count = 0;
x_red = [];

for i = 1:n
  if(y(i) <= (3*x(i)*x(i)))
    count = count + 1;
    #plot = [x_red x(i)]
    x_red(count) = x(i);
    #plot(x(i),y(i),"r*")
   else
    #plot(x(i),y(i),"k*")
   end
   #hold on ;
endfor

x_int = 0:0.0001:1;
for i = 1:length(x_int)
  cnt_int = length(find(x_red < x_int(i)));
  if(cnt_int < (0.95 * count))
    a = x_int(i);
    #disp(cnt_int)
  end
endfor
