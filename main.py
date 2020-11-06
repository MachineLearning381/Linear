import datums as data
import test as rtest
import matplotlib.pyplot as plt

bcx = data.breast_cancer.data;
bcy = data.breast_cancer.target;




# Calculate g and g_mistakes for different T
# W Initialized by First Datapoint 5 times
# W Initialized by Linear Regression 5 times
# t(n) = T
# tm(n) = mistakes
# Blue =  W Initialized by First Datapoint
# Red = W Initialized by Linear Regression


x1=[];
x2=[];
y1=[];
y2=[];

t1,tm1,t2,tm2 = rtest.full_run(bcx,bcy,.8,100);
x1.append(t1);
y1.append(tm1);
x2.append(t2);
y2.append(tm2);

t3,tm3,t4,tm4 = rtest.full_run(bcx,bcy,.8,150);
x1.append(t3);
y1.append(tm3);
x2.append(t4);
y2.append(tm4);

t5,tm5,t6,tm6 = rtest.full_run(bcx,bcy,.8,200);
x1.append(t5);
y1.append(tm5);
x2.append(t6);
y2.append(tm6);

t7,tm7,t8,tm8 = rtest.full_run(bcx,bcy,.8,250);
x1.append(t7);
y1.append(tm7);
x2.append(t8);
y2.append(tm8);

t9,tm9,t10,tm10 = rtest.full_run(bcx,bcy,.8,300);
x1.append(t9);
y1.append(tm9);
x2.append(t10);
y2.append(tm10);
#print(x1);
#print(y1);
#print(x2);
#print(y2);
plt.plot(x1,y1,'b-');
plt.plot(x2,y2,'r-');




plt.xlabel("T");
plt.ylabel("Errors");
plt.show();






#irisx = data.iris.data;
#irisy = data.iris.target;


# rtest.test_run(irisx,irisy,.1);
# rtest.test_run(irisx,irisy,.2);
# rtest.test_run(irisx,irisy,.3);
# rtest.test_run(irisx,irisy,.4);
#rtest.test_run(irisx,irisy,.5);

# rtest.regress_run(irisx,irisy,.1);
# rtest.regress_run(irisx,irisy,.2);
# rtest.regress_run(irisx,irisy,.3);
# rtest.regress_run(irisx,irisy,.4);
#rtest.regress_run(irisx,irisy,.5);


# rtest.test_run(bcx,bcy,.1);
# rtest.test_run(bcx,bcy,.2);
# rtest.test_run(bcx,bcy,.3);
# rtest.test_run(bcx,bcy,.4);
#rtest.test_run(bcx,bcy,.5);

# rtest.regress_run(bcx,bcy,.1);
# rtest.regress_run(bcx,bcy,.2);
# rtest.regress_run(bcx,bcy,.3);
# rtest.regress_run(bcx,bcy,.4);
#rtest.regress_run(bcx,bcy,.5);


# Calculate g and g_mistakes for different T
# W Init by Linear Regression
# rt(n) = T
# rm(n) = mistakes
# Red

# rt1,rm1 = rtest.regress_run(bcx,bcy,.8, 100);
# plt.plot(rt1,rm1,'ro');

# rt2,rm2 = rtest.regress_run(bcx,bcy,.8, 150);
# plt.plot(rt2,rm2,'ro');

# rt3,rm3 = rtest.regress_run(bcx,bcy,.8, 200);
# plt.plot(rt3,rm3,'ro');

# rt4,rm4 = rtest.regress_run(bcx,bcy,.8, 250);
# plt.plot(rt4,rm4,'ro');

# rt5,rm5 = rtest.regress_run(bcx,bcy,.8, 300);
# plt.plot(rt5,rm5,'ro');