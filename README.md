# Natural Computing Algorithms CW


## About this project
This project applies Artificial Bee Colony algorithm to solve two different problems. The first problem is to find the minimum of a objective function. Not only using the vanilla version of the algorithm, this project also adjusts the algorithm to have better performance on the minimum problem. On the other hand, the second problem is largest clique problem. This project suggests two discretization methodology to be combined with ABC algorithm to solve the largest clique problem. 

## Minimum Problem

### Objective function: 
$$
f = \frac{a^2}{4000} + \frac{b^2}{4000} + \frac{c^2}{4000} - \left(\sin\left(\frac{\pi}{2} + a\right) \cdot \sin\left(\frac{\pi}{2} + \frac{b}{\sqrt{2}}\right) \cdot \sin\left(\frac{\pi}{2} + \frac{c}{\sqrt{3}}\right)\right) + 1
$$

### Comparsion of the Vanilla and Enhanced Version. 
|  | Vanilla Version | Enhanced Version |
|----------|----------|----------|
| Employed Bee Phase | One Variable | More Variables |
| Onlooker Bee Phase | Roulette Wheel | Tournament Selection |
| Scout Bee Phase | Replaced by a random new food source | Greedy Selection |


## Largest Clique Problem
### Discretization Methodology
Method 1: The first way to generate a near-neighbour is to save the entire set of vertices and runs through the vertices that do not belong to that current food source to check whether it forms a proper clique with a current food source, and a vertex does not belong to its current food source. If a proper clique is found with a vertex and a current food source, the current food source will be replaced by that proper clique. If a proper clique is not found, the limit number will be added by 1. 

Method 2: The second way to generate a near-neighbour is by removing a random number of vertices of the targeted food source. The number of removed vertices ranges from 1 to half the targeted food source’s size, meaning at least half the vertices will remain. After removing the vertices, the unselected vertices will be chosen randomly and added to the targeted food source. This newly generated food source is the size of the current food source + 1. Then this newly generated food source will be checked to determine whether it is a proper clique. If so, the current food source will be replaced with this new food source. 


### Discretization Method used in the three phases
| ABC Phase | Discretization Methodology | 
|----------|----------|
| Employed Bee Phase | Method 1 |
| Onlooker Bee Phase | Method 1 | 
| Scout Bee Phase | Method 2 | 
