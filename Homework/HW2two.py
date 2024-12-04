a = input("What was your score on Participation? ")
b = input("What was your score on Quizzes? ")
c = input("What was your score on Homework? ")
d = input("What was your score on Project 1? ")
e = input("What was your score on Project 2? ")
f = input("What was your score on Midterm Exam 1? ")
g = input("What was your score on Midterm Exam 2? ")
h = input("What was your score on Final Exam? ")
if a <= 100 and a >= 0:
    a = a
elif a >= 100:
    a = 100
else: 
    a = 0
if b <= 100 and b >= 0:
    b = b
elif b >= 100:
    b = 100
else: 
    b = 0
if c <= 100 and c >= 0:
    c = c
elif c >= 100:
    c = 100
else: 
    c = 0
if d <= 100 and d >= 0:
    e = e
elif f >= 100:
    f = 100
else: 
     f= 0
if g <= 100 and g >= 0:
    g = g
elif g >= 100:
    g = 100
else: 
    g = 0
if h <= 100 and h >= 0:
    h = h
elif h >= 100:
    h = 100
else: 
    h = 0
# Now, we don't use int() function to typecast the variables because the values in input may be in decimals that will get lost if we use int function
i = (float(a)/100) * 5
i2 = (float(a)/100) * 5
j = (float(b)/100) * 5
j2 = (float(b)/100) * 5
k = (float(c)/100) * 13
k2 = (float(c)/100) * 5
l = (float(d)/100) * 18
l2 = (float(d)/100) * 5
m = (float(e)/100) * 23
m2 = (float(e)/100) * 5
n = (float(f)/100) * 7
n2 = (float(f)/100) * 5
o = (float(g)/100) * 12
o2 = (float(g)/100) * 5
p = (float(h)/100) * 17
p2 = (float(h)/100) * 5
k = i + j + k + l + m + n + o + p
k2 = i2 + j2 + k2 + l2 + m2 + n2 + o2 + p2 
print ("In grade weighting system 1 your score is: " + k)
print ("In grade weighting system 2 your score is: " + k2)
if k >= k2:
    print("Your final grade is: " + k)
else:
    print("Your final grade is: " + k2)

print("The minimum score is 0!")
print("The minimum score is 0!")