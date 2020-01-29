# Pythonic Objects
Repository dedicated to study a course created by Luciano Ramalho and presented by Renzo Nuccitelli in python.pro.br

**Content:**  
1. Difference between `globals()` and `locals()`
2. Function as object: Attributes and properties  
    a. `function.__name__`  
    b. `function.__code__.co_code`  
3. Anonymous function: `func_double = lambda x: x*2`
4. Function as argument:
```
def execute(f, n=1):
    for _ in range(n):
        f()
```
5. Using `map()` and `filter()`:  
    a. Both functions receive a function as first argument  
    b. `filter()` receives a boolean function  
    c. `map()` receives a transformation function