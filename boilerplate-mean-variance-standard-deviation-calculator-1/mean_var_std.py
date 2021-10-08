import numpy as np

def calculate(list):
  if(len(list)!= 9):
    raise ValueError ("List must contain nine numbers.")
  calculations = {}
  print(mean(list))
  calculations["mean"] = mean(list)
  calculations["variance"] = variance(list)
  calculations["standard deviation"] = standard_deviation(list)
  calculations["max"] = max(list)
  calculations["min"] = min(list)
  calculations["sum"] = sum(list)
  print("calc",calculations)
  return calculations


def mean(list):
  arr = np.array(list).reshape(3,3)
  print("mean",np.mean(arr,axis = 0) , np.mean(arr,axis=1), np.mean(arr))
  return [[*np.mean(arr,axis = 0)] , [*np.mean(arr,axis=1)], np.mean(arr)]
    
def variance(list):
  arr = np.array(list).reshape(3,3)
  return [[*np.var(arr,axis = 0)] , [*np.var(arr,axis=1)], np.var(arr)]
    

def standard_deviation(list):
  arr = np.array(list).reshape(3,3)
  return [[*np.std(arr,axis = 0)] , [*np.std(arr,axis=1)], np.std(arr)]


def max(list):
  arr = np.array(list).reshape(3,3)
  return [[*np.max(arr,axis = 0)] , [*np.max(arr,axis=1)], np.max(arr)]


def min(list):
  arr = np.array(list).reshape(3,3)
  return [[*np.min(arr,axis = 0)] , [*np.min(arr,axis=1)], np.min(arr)]


def sum(list):
  arr = np.array(list).reshape(3,3)
  return [[*np.sum(arr,axis = 0)] , [*np.sum(arr,axis=1)], np.sum(arr)]

