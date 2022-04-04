
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
- a generator object is an iterable which means that it can work with for loops
- 제너레이터 객체는 이터러블이며, 이터러블을 사용하면 for 루프의 다형성을 보장하는 강력한 추상화가 가능하다.


### Generator expressions
- Generator save a lot of memory
- Generator expressions can also be passed directly to functions that work with iterables, such as sum(), and, max():

### Iterating idiomatically

### Idioms for iteration
- 
### The next() function
- 다음 원소가 없다면 `StopIteration` 이라는 에러가 발생한다.
- 만약 default값을 설정하고 싶다면 next(word, "default value") 라고 설정 해주면 된다.

### Using a generator
- Generator objects are iterators.

### Itertools


### Simplifying code through iterators
- 동시에 한번에 여러개의 iterator을 만들어야 한다.

Nested loops
- 중첩된 for문을 돌을떄, 용이하게 사용할 수 있다.


### Coroutines
- Here, we will explore how generators evolved into coroutines to support the basis of asynchronous programming
- the basic methods 
  - .close()
  - .throw()
  - .send()


- streamer.throw(CustomException)이 발생한 경우 제너레이터는 INFO 레벨의 메시지를 기록하고 다음 yield 구문으로 이동한다.
- except Exception as e 구문이 없다면 streamer.throw(RuntimeError)이 발생한 경우 제너레이터가 중지된 행에서 예외가 호출자에게 전파되고, 제너레이터는 중지된다.