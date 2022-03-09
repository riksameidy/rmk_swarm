# RMK SWARM

RMK Swarm is a python package containing tools and functions to make your implementation of Swarm Intelligence Method easier.

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install RMK Swarm like below. 
Rerun this command to check for and install  updates .
```bash
pip install git+https://github.com/riksameidy/rmk_swarm
```

## Usage
Features:
* swarmtools.inisialisasiPopulasi  --> generator to genarate a swarm population consist of n individuals 
* swarmtools.evaluate_populasi     --> function to evaluate given objective function for each individual in a population

#### Demo of some of the features:

```python
import rmk_swarm
from rmk_swarm import swarmtools

# The domain
rn = [ [0,1] , [2,2] , [1,10]  ]

# Objective function
def f(X):
	return X[0] + X[1] + X[2]

# Parameters
n_populasi = 10    # number of individuals in Population

populasi = swarmtools.inisialisasiPopulasi(n_populasi , rn )
populasi = swarmtools.evaluate_populasi(populasi,f)

print( populasi )

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)