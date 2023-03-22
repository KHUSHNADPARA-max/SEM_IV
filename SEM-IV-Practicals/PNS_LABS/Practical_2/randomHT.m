clc;
clear all;
close all;

n = input("Enter the number of timmes you want to toss coin : ");

a = randi(2,1,n);
a
for i = 1:n
  if(a(i) == 2)
    outcome(i) = 'H';
   else
    outcome(i) = 'T';
  end
endfor

outcome

#-------------------------------------------------

nh = 0;
nt = 0;

for i = 1:n
    nh = nh+(outcome(i) == 'H');
    nt = nt+(outcome(i) == 'T');
endfor

disp(sprintf("Prob. Of Head :: %3.2f", nh/n));
disp(sprintf("Prob. Of Tail :: %3.2f", nt/n));
