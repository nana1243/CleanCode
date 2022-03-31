
## Using Generators

the goal of this chapter
- to create generators that improve the performances
- to study how iterators are embedded in Python
- to understand how generators work   as the basis for coroutines and asynchronous programming
- To explore the syntactic support for coroutines—yield from, await, and async def



### Technical requirements

### Creating Generators
- 제네레이터 주요 목적은 메모리 절약이다.

### A first look at generators
- a generatorr object is an iterable which means that it can work with for loops


### Generator expressions
- Generator save a lot of memory
- Generator expressions can also be passed directly to functions that work with iterables, such as sum(), and, max():

### Iterating idiomatically

### Idioms for iteration
- 