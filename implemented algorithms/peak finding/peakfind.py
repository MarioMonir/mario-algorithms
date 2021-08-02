#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:41:59 2019

@author: mario
"""

import numpy as np
import math  as m
def peakfind1(arr,l,r):
    
    if (r<=l):
        print(arr[l:])
        print ("case 1 last recurse")
        return arr[r]
    
    elif(r-l==1):
        print ("size of  arr =  " , r-1+1 )
        print ("case 2 : found in index " , l)
        return max(arr[l],arr[l+1])
    
    else:
        mid = m.floor( ( (r+l)/2)   ) 
        print("mid index = " , mid , "with value = " , arr[mid] )
        
        if(arr[mid]>=arr[mid-1] and  arr[mid]>=arr[mid+1]):
            print ("case 3  found " , arr[mid] ,">=",arr[mid-1]," , ", arr[mid],">=",arr[mid+1])
            return arr[mid]
        
        else:
            # go right    # go left
            l = mid+1     #r = mid -1 
            print ("case 4 recurse  now array start from index = ", l , " value is " ,arr[l] )
            return peakfind1(arr,l,r)
        


def cloumnMax1(arr,n,clm):
    mx   = 0
    for i in range(1,n):
        if(arr[i][clm]>arr[mx][clm]):
            mx = i
    return mx        

        

def peakfind2D1(arr,l,r):
    
    n = len(arr[0])
    mid = m.floor((r+l)/2)
    i = cloumnMax1(arr,n,mid)
    
    if(r<= l):
        print ("case 1 last recurse  peak at index",i,",",mid)
        return arr[i][mid]
    elif(r-l==1):
        print ("case 2 just 2 column peak at index",i,",",mid)
        return max(arr[i][mid],arr[i+1][mid] )
    else:
        p = arr[i][mid]
        if ( p >= arr[i][mid-1]  and p >= arr[i][mid+1] ):
            print ("case 3  found " , p ,">=",arr[i][mid-1]," , "
                   , p ,">=",arr[i][mid+1] ," peak at index",i,",",mid )
            return p
        
        else:
            l = mid+1
            return peakfind2D1(arr,l,r)
        

arr = np.random.randint(25, size=11)
#arr = [12,109]

#print (arr)
#print(peakfind(arr,0,len(arr)-1))


arr2d = np.random.randint(25, size=(3,3))
print (arr2d)

print(peakfind2D1(arr2d,0,len(arr2d)-1))







        
    
def peakfind(arr,l,r):
    if (r<=l):
        return arr[r]
    elif(r-l==1):
        return max(arr[l],arr[l+1])
    else:
        mid = m.floor( ( (r+l)/2)   ) 
        if(arr[mid]>=arr[mid-1] and  arr[mid]>=arr[mid+1]):
            return arr[mid]
        else:
            l = mid+1
            return peakfind(arr,l,r)    
    
    
def cloumnMax(arr,n,clm):
    mx   = 0
    for i in range(1,n):
        if(arr[i][clm]>arr[mx][clm]):
            mx = i
    return mx        
    
def peakfind2D(arr,l,r):
    
    n = len(arr[0])
    mid = m.floor((r+l)/2)
    i = cloumnMax(arr,n,mid)
    
    if(r<= l):
        return arr[i][mid]
    elif(r-l==1):
        return max(arr[i][mid],arr[i+1][mid] )
    else:
        p = arr[i][mid]
        if ( p >= arr[i][mid-1]  and p >= arr[i][mid+1] ):
            return p
        
        else:
            l = mid+1
            return peakfind2D(arr,l,r)
            
    