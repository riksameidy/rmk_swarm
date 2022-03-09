# rmk_swarm

rmk_swarm is a python package containing tools and functions to make your implementation of Swarm Intelligence Method easier.

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install rmk_swarm like below. 
Rerun this command to check for and install  updates .
```bash
pip install rmk_swarm
```
## Usage
Features:
* swarmtools.init_pop  --> generator to genarate a swarm population consist of n individuals 
* swarmtools.eval_pop     --> function to evaluate given objective function for each individual in a population
* swarmtools.print_pop     --> function to print for each individual in a population | Format -> [ ID , X , fitness ]
* swarmtools.sort_pop     --> function to sort individual in a population based on its objective function
* swarmtools.find_best     --> function to find best individual in a population

#### Demo of some of the features:

```python
# How to Import
from rmk_swarm import swarmtools

# Domains of each x in X = {  x1,x2,x3  }
rn = [ [0,1] , [2,2] , [1,10]  ]

# Objective function Example
def f(X):
	return X[0] + X[1] + X[2]

# Parameters
n_populasi = 10    # number of individuals in Population

# Generate n number of individuals
populasi = swarmtools.init_pop(n_populasi , rn )

# Evaluate Each individuals Objective Functions
populasi = swarmtools.eval_pop(populasi,f)

# Print all individuals in population
swarmtools.print_pop(populasi)

# Sort the individuals in Population
swarmtools.sort_pop(populasi)

# Find best individuals. Note: Sort First then return best individual
swarmtools.find_best(populasi)

```

## Contributing
Please Contact me at riksameidy@gmail.com if you want to contribute to this package. Thank you :)

## License
[MIT](https://choosealicense.com/licenses/mit/)
