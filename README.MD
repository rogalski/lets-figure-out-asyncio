This repo contains my experiments for figuring out essentials of asyncio. Notes are in Polish, sorry about that :) 

# Czym jest a czym nie jest asyncio
_This module provides infrastructure for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets and other resources, running network clients and servers, and other related primitives._
- **jednowątkowy** - to wciąż jednowątkowy interpreter Pythona w którym działa GIL, nie zwiększamy utylizacji procesora poprzez utworzenie wielu wątków
- **concurent**, nie **parallel** - wiele "długotrwających" funkcji wykonywanych jest naprzemiennie, nie jednoczeście - więcej wyjaśnień w [What is the difference between concurrent programming and parallel programming? na Stack Overflow](http://stackoverflow.com/questions/1897993/what-is-the-difference-between-concurrent-programming-and-parallel-programming)
- przydatny dla problemów IO-bound, tj. problemem jest _czekanie na coś_, nie _obliczenie czegoś_. Gdybyśmy chcieli liczyć potrzebujemy ektra wątków lub procesów.

# Słownik

## Event loop
Pilnuje egzekucji asynchronicznego kodu.

## Task
Jaka jest różnica między nimi?

## Future
Jaka jest różnica między nimi?

## Transport
Obiekt reprezentujący kanał komunikacyjny

## Protkół (Protocol)
Obiekt kodujący i dekodujący dane przesyłane przez transport

# `async with` 
?