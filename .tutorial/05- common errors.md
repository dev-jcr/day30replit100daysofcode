# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

👉 What's wrong with this code:

```python
for i in range(1, 31):
  print("Day {i} of 100")
```

<details> <summary> 👀 Answer </summary>

We missed the `f` before the string OR we need to add `.format`

```python
for i in range(1, 31):
  print(f"Day {i} of 100")
```
OR

```python
for i in range(1, 31):
  print("Day {count} of 100".format(count=i))
```

</details>

f-strings must have `f` before them or `.format` after  them or they will not work.