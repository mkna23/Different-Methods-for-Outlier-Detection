#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:42:02 2020
Program: Outlier Detection

Input: the number of terms for data series 
    
Computation:
    a.)to generate a function to detect outliers in given data series using mean 
    and standard deviation
    Function: getOutliersMeanStd(data)
      Calculated the mean and standard deviation og given data series 
      using the condition that if any data point is less than
      Mean-2*Stdv and greater than Mean+2*Stdv is appended to list of outliers
      the outliers list returned to main
      
      
    b.) generate a function to detect outliers in given data series based on z-score
    Function: getOutliersZscore
    calculated z score for each point and any value that is >3 or <-3 is outlier 
    the list of outlier is returned
    
    c.) generate a recursive function to generate a series of numbers
    Function: genOddsSeq(nterms)
    input is no of terms
    this function using the odds function to create the list of data series of odd numbers for 
    the given no of terms.
    returns the list of data series of odd numbers  
    
Output:
    generate data series of odd numbers
    The outliers based on mean and deviation
    outliers based on z-score
    Outliers based on mean, standard deviation and trimming the data series

"""



# this function return the odd term for the number using the arthimetic formula a=a(n-1)+2
def odds(n):
    if n==1:
       a=3
       return a
    else:
        a=3
        a=a+2
        return odds(n-1)+2
  # using recursive function      

#this function returns the sequence of odd terms 
def genOddsSeq(nTerms):
    Seq_Oddterms=[]
    for i in range(1,nTerms+1):# uses the function odds to get odd terms for the terms
         Oddval= odds(i)
         Seq_Oddterms.append(Oddval)
    return Seq_Oddterms
    


def getOutliersMeanStd(data,trim=0):
    import statistics
    import math
    Outlier=[]
    Sum =0
    for i in data:
        Sum+=i
    Mean= Sum/len(data) #mean calculation
    Variance = statistics.variance(data)
    Stdv = math.sqrt(Variance)#standard dev calculation
    Cond_low = Mean-2*Stdv
    Cond_high = Mean+2*Stdv
    for i in data:
          if i<Cond_low or i>Cond_high:
              Outlier.append(i)
    return Outlier
#returns the lost of outliers
    
    
def getOutliersMeanStd2(data,trim=0.1):
    import statistics
    import math
    Outlier=[]
    Sum =0
    for i in data:
        Sum+=i
    Mean= Sum/len(data)
    Variance = statistics.variance(data)
    Stdv = math.sqrt(Variance)
    Cond_low = Mean-2*1.49*Stdv# conditions changed as data is trimmed
    Cond_high = Mean+2*1.49*Stdv
    for i in data:
        if i<Cond_low or i>Cond_high:
            Outlier.append(i)
    return Outlier

      
        
def getOutliersZscore(data):
    Outlier={}
    Z_Score=[]
    import statistics
    import math
    Sum =0
    for i in data:
        Sum+=i
    Mean= Sum/len(data)
    Variance = statistics.variance(data)
    Stdv = math.sqrt(Variance)
    # calculation of z score using mean and stdv
    for Term in data:
        z= (Term-Mean)/Stdv
        Z_Score.append(z)
    # for loop used to put outliers in dic as key from z score list and data list
    for z,i in zip(data,Z_Score):
          if i>3 or i<-3:
             Outlier[z]=i
    return list(Outlier.keys())
#returns the list of outliers as in form of list of keys of dic
        
#main function    
def main():
  valid =0 
  while(valid==0):
    try:
        data = int(input('Enter the number of terms for data series:'))
        valid = 1
    except ValueError:
          print("Error, Please input numbers only !")
# geting only integer values
  Terms=[]
  Outlier1=[]
  Outlier2=[]
  Outlier3=[]
  #calling function genOddsSeq and assigning series of data series to list name Terms
  Terms = genOddsSeq(data)
  #extending the list Terms 
  Items=[100,200,500,900]
  Terms.extend(Items)
  
   #printing the list of data series(Terms)
  print('-'*21,':')
  print('Series of odd numbers :')
  print('-'*21,':')
  print(Terms)
  
  # printing the outliers bsed on mean and stdv
  print('-'*38 ,':')
  print('Outlier detection based on mean and std :')
  print('-'*38,':')
  Outlier1 = getOutliersMeanStd(Terms,trim=0)
  for i in Outlier1:
      print('Outlier :%3d'%i)
      
  print('-'*49,':')
  # calling the function getOutliersMeanStd2
   # printing the outliers bsed on mean and std with trim 0.1
  print('Outlier detection based on mean and std with trim 0.1')
  print('-'*49,':')
  Outlier2= getOutliersMeanStd2(Terms,trim=0.1)
  for i in Outlier2:
     print('Outlier :%3d'%i)
     
  print('-'*35,':')
  #printing the outliers based on z score
  print('Outlier detection based on z score :')
  print('-'*35,':')
  Outlier3= getOutliersZscore(Terms)
  for i in Outlier3:
      print('Outlier : %3d'%i)
main()

