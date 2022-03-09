import random

def gen_Gen(a,b):
  return random.uniform(a,b)

def gen_Indv(rn):
  return [ gen_Gen(rn[i][0], rn[i][1] ) for i in range(len(rn)) ]

def gen_pop(n_populasi,rn):
  return [ gen_Indv(rn) for i in range(n_populasi) ]

def init_pop(n_populasi,rn):
  return list(map(  lambda x: [x[0],x[1],[] ] , enumerate( gen_pop(n_populasi,rn) ) ) )

def print_pop(populasi):
  for p in populasi:
    print(p)

def f_obj(X,f):
  return f(X)

def eval_pop(populasi,f):
  return list( map( lambda x: [ x[0],x[1], f_obj( x[1], f ) ] , populasi  ) )

def sort_pop(populasi):
  populasi.sort(key = lambda x:x[2] , reverse=True)

def find_best(populasi):
  sort_pop(populasi)
  return populasi[0]
