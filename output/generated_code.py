 Here's a simple Python script that calculates the factorial of a given number, specifically 10 in this case:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 10
result = factorial(number)

print(f"The factorial of {number} is {result}")
```

Save this script as `factorial.py` and run it in your terminal or Python environment to get the factorial of 10.