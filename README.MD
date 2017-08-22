This repo contains my experiments for figuring out essentials of asyncio. Notes are in Polish, sorry about that :) 

# Czym jest a czym nie jest asyncio
_This module provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives._
- **jednowątkowy** - to wciąż jednowątkowy interpreter Pythona w którym działa GIL, nie zwiększamy utylizacji procesora poprzez utworzenie wielu wątków
- **concurent**, nie **parallel** - wiele "długotrwających" funkcji wykonywanych jest naprzemiennie, nie jednoczeście - więcej wyjaśnień w [What is the difference between concurrent programming and parallel programming? na Stack Overflow](http://stackoverflow.com/questions/1897993/what-is-the-difference-between-concurrent-programming-and-parallel-programming)
- przydatny dla problemów IO-bound, tj. problemem jest _czekanie na coś_, nie _obliczenie czegoś_. Gdybyśmy chcieli liczyć potrzebujemy ektra wątków lub procesów.

# Historia
* [PEP 342 -- Coroutines via Enhanced Generators](https://www.python.org/dev/peps/pep-0342) (Py 2.5)
_yay, you can send to generator!_.
* [PEP 380 -- Syntax for Delegating to a Subgenerator](https://www.python.org/dev/peps/pep-380) (Py 3.3)
_When `send`ing, `throw`ing and `close`ing generator, delegating generators gets tricky - why?_
* [PEP 492 -- Coroutines with async and await syntax](https://www.python.org/dev/peps/pep-0492/) (Py 3.5)
_We have all the tools in the language - let's make a proper syntactic sugar for those capabilities_.

## Pre PEP492
```python
import asyncio
@asyncio.coroutine
def coro(x):
    yield from asyncio.sleep(x)
```

## Post PEP492
```python
import asyncio
async def coro(x):
    await asyncio.sleep(x)
```


## Equivalents
- `yield from` = `await`
- `@asyncio.coroutine` = `async def`

# Coroutines vs. generators
- are not similar in terms of behavior description (!)
- generators (mostly) _produce_ values, coroutines (mostly) _consume_ values
- they are somewhat similar in terms of giving away control flow and being non-blocking


# Słownik

## Coroutine function
Kod - ekwiwalent funkcji.

## Coroutine
_Instancja_ `coroutine function` z przypisanymi argumentami - coś, co nadaje się do wykonania 

## Future
Encapsulates the asynchronous execution of a callable.

## Task
Schedule the execution of a coroutine: wrap it in a future. A task is a subclass of Future.

## Event loop
Pilnuje egzekucji asynchronicznego kodu.

## Linki
- [David Beazley - A Curious Course on Coroutines and Concurrency (PyCon 2009)](http://www.dabeaz.com/coroutines/Coroutines.pdf)
- [Łukasz Langa - Thinking in coroutines (PyCon 2016)](https://www.youtube.com/watch?v=l4Nn-y9ktd4)
- [Armin Ronacher - I don't understand Python's Asyncio](http://lucumr.pocoo.org/2016/10/30/i-dont-understand-asyncio/)
