#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator
# 
# https://mercer-health.com/services/weight-management-center/bmi-calculator#:~:text=Body%20Mass%20Index%2C%20or%20BMI,inches%20x%20height%20in%20inches

# In[88]:


name = input("Enter your name: ")

weightKG = int(input("Enter your weight in kilogram (kg): "))

heightCM = int(input("Enter your height in centimeters (cm): "))

heightM = int(heightCM) * 0.01

BMI = (weightKG) / (heightM * heightM)

print(BMI)

if BMI > 0:
    if (BMI < 18.5):
        print(name+", you are Underweight!")
    elif (BMI <= 24.9):
        print(name+", you are Normal Weight!")
    elif (BMI <= 29.9):
        print(name+", you are overweight!")
    elif (BMI <= 34.9):
        print(name+", you are Obese!")
    elif (BMI <= 39.9):
        print(name+", you are Severely Obese!")
    else:
        print(name+", you are Morbidly Obese!")
else:
    print("Enter valid input")
        



# In[ ]:





# In[19]:





# In[ ]:





# In[ ]:


#BMI = (weight in pounds x 703) / (height in inches x height in inches).


# In[ ]:


print(weight)


# In[ ]:


Under 18.5	Underweight	Minimal
18.5 - 24.9	Normal Weight	Minimal
25 - 29.9	Overweight	Increased
30 - 34.9	Obese	High
35 - 39.9	Severely Obese	Very High
40 and over	Morbidly Obese	Extremely High


# In[85]:


if BMI > 0:
    if (BMI < 18.5):
        print("Your BMI is", BMI, name+", you are Underweight!")
    elif (BMI <= 24.9):
        print("Your BMI is", BMI, name+", you are Normal Weight!")
    elif (BMI <= 29.9):
        print("Your BMI is", BMI, name+", you are overweight!")
    elif (BMI <= 34.9):
        print("Your BMI is", BMI, name+", you are Obese!")
    elif (BMI <= 39.9):
        print("Your BMI is", BMI, name+", you are Severely Obese!")
    else:
        print("Your BMI is", BMI, name+", you are Morbidly Obese!")
else:
    print("Enter valid input")
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




