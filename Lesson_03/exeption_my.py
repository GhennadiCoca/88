try:
    res = 10/0
    print("Res is", res)
except ZeroDivisionError:
    print("Division by zero")

print("Hi")

input_str = "avr"
input_str2 = "67"

try:
    number = int(input_str)
    print(number)
except ValueError:
    print("Only integers")

print("Hi")

def divider(a, b):
    try:
      return a / b
    except ZeroDivisionError:
      print("Division by zero")

print(divider(1, 2))
divider(1, 0)
divider(1, 0)

numbers = [1, 2, 3]
#print(numbers[3])

try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError as e:
    print(e)
    print(type(e).__name__)

def divide(a, b):
    try:
      return a / b
    except (ZeroDivisionError, TypeError) as e:
        print(e)
divide(1,"python")

try:
   data = {"name": "John", "age": 25}
   print(data["email"])
except TypeError:
    print("Key error")
except Exception:
    print("Unexpected error")

try:
    number = int("456")
except ValueError:
    print("Only integer")
else:
    print("Success, it is a number: ",number)

try:
    print("Try part")
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero")
finally:
    print("Always finished")

def type_age(age):
    try:
        age = int(age)
    except (TypeError, ValueError):
        print("Type error")
    else:
        print("Success, it is a number: ",age)
    finally:
        print("Type age")

type_age("25")
type_age("number")


