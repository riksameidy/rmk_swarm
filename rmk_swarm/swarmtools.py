import random

def genGen(a,b):
  return random.uniform(a,b)

def genIndividu(rn):
  return [ genGen(rn[i][0], rn[i][1] ) for i in range(len(rn)) ]

def genPopulasi(n_populasi,rn):
  return [ genIndividu(rn) for i in range(n_populasi) ]

def inisialisasiPopulasi(n_populasi,rn):
  return list(map(  lambda x: [x[0],x[1],[] ] , enumerate( genPopulasi(n_populasi,rn) ) ) )

def print_populasi(populasi):
  for p in populasi:
    print(p)

def f_obj(X,f):
  return f(X)

def evaluate_populasi(populasi,f):
  return list( map( lambda x: [ x[0],x[1], f_obj( x[1], f ) ] , populasi  ) )

def sort_populasi(populasi):
  populasi.sort(key = lambda x:x[2] , reverse=True)

def find_best(populasi):
  return populasi[0]
