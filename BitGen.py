#!/usr/bin/env python
# coding: utf-8
#! python3

# In[141]:


import random as r
# Generate a certain amount of 1's and 0's
#
# Input the length of symbols required
# Output the 1's and 0's as string

print('\n')

# In[145]:


NumberInput = int(input("Input how many symbols you want to have produced: "))


# In[146]:


def bitgen(number):
    notalist = ""
    for i in range(number):
        x = r.randint(1, 10000)
        if (x % 2) == 0:
            notalist += '0'
        else:
            notalist += '1'
        
    return notalist


# In[147]:


b = bitgen(NumberInput)
bb = list(b)


# In[149]:


counter = {'Zeroes': 0, 'Ones': 0}
for number in bb:
    if number == '0':
        counter['Zeroes'] += 1
    elif number == '1':
        counter['Ones'] += 1


# In[150]:

print('\n')
print('These are your random bits: ', bitgen(NumberInput))
print('\n')


# In[152]:


PrcntOfZeroes = counter['Zeroes'] / NumberInput
zzz = int(PrcntOfZeroes * 100)

PrcntOfOnes = 100 - zzz
ooo = int(PrcntOfOnes)

print(' Percent of zeroes is:', zzz, '%', '\n', 'Percent of ones is:  ', ooo, '%')
print('\n')

input('Press ENTER to exit')
