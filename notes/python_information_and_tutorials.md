# Python Information and Tutorials: Practical Summary

**Course:** University of Washington, Computational Neuroscience (Coursera)
**Recorded:** September 13, 2026
**Source:** The course reading "Python Information and Tutorials" shared in this session, plus the practical study explanation.
**Status:** Reference notes, not evidence of completed exercises or an optional Python quiz attempt.

The pasted reading contained missing code blocks and several Python 2-era links. The examples below are reconstructed for Python 3, not a verbatim transcript of those missing blocks.

## What You Need for This Course

Python is the tool for representing neural data, running numerical calculations, and plotting signals or model outputs.

| Tool | Practical role |
|---|---|
| Python 3 | The programming language and runtime. |
| NumPy | Arrays, matrices, numerical calculations, and vectorized operations. |
| Matplotlib | Plotting data and model results. |
| VS Code, Spyder, or another editor | The place where you write and run code; it does not change the mathematics. |

You can continue using VS Code. Anaconda and Spyder are optional, not course requirements. A working environment with NumPy and Matplotlib is sufficient for the material shared so far.

## Console, Scripts, and Packages

- **Console/interpreter:** Run individual commands and inspect results immediately.
- **Script:** Save a sequence of commands in a `.py` file and run it again later.
- **Module:** A Python file whose functions or other definitions can be imported.
- **Package:** Organized functionality you import and reuse, such as NumPy.
- **Environment:** The Python installation and packages used for a particular project. Select the intended interpreter in your editor.

Anaconda bundles a Python environment with scientific tools. Miniconda provides a smaller starting environment to which you add packages. The download sizes and Spyder menu instructions in the reading are historical, not current installation specifications.

The relevant Python foundations are variables and arithmetic, `if` statements, `for` and `while` loops, functions, lists and dictionaries, and imports. Given your Python background, focus on numerical array behavior rather than restarting with basic syntax.

## The Basic Scientific Python Workflow

Import libraries, create or load data, calculate, then plot:

```python
import numpy as np
import matplotlib.pyplot as plt

values = np.array([1, -1, 2, -2, 3])
doubled = values * 2

print(doubled)
print(values.mean())

plt.plot(values)
plt.xlabel("Sample index")
plt.ylabel("Value")
plt.show()
```

The printed results are `[2, -2, 4, -4, 6]` as a NumPy array and a mean of `0.6`. Without explicit x-values, `plt.plot(values)` uses sample indices starting at zero.

`np` and `plt` are conventional aliases for `numpy` and `matplotlib.pyplot`. They let you call functions such as `np.array`, `np.mean`, and `plt.plot`.

**Important:** Multiplying a Python list by 2 repeats its contents. Multiplying a NumPy array by 2 doubles every value. Use arrays for the numerical operations in this course.

## MATLAB to NumPy: The Differences That Matter

These examples assume numerical NumPy arrays, not Python lists or the legacy `np.matrix` class.

| Task | MATLAB | Python / NumPy |
|---|---|---|
| First element of a vector | `values(1)` | `values[0]` |
| All rows, columns 2 and 3 | `matrix(:,2:3)` | `matrix[:, 1:3]` |
| All rows, columns 1, 3, and 5 | `matrix(:,1:2:5)` | `matrix[:, 0:5:2]` |
| Element-wise multiplication | `left .* right` | `left * right` |
| Matrix multiplication | `left * right` | `left @ right` |
| Element-wise square | `values .^ 2` | `values ** 2` |
| Two-by-three zero matrix | `zeros(2,3)` | `np.zeros((2, 3))` |
| Four-by-one vector of fives | `ones(4,1) * 5` | `np.full((4, 1), 5)` |
| Transpose without conjugation | `matrix.'` | `matrix.T` |
| Replace negative entries | `values(values < 0) = 0` | `values[values < 0] = 0` |

**Indexing:** Python starts at 0 and uses square brackets. Python slices exclude the stop index: `1:3` selects indices 1 and 2, which are the second and third entries. Slice order is `start:stop:step`, unlike MATLAB's `start:step:stop`.

**Shapes:** A NumPy array can be one-dimensional rather than a row or column matrix:

```python
vector = np.array([1, 2, 3])
column = vector.reshape(3, 1)
row = vector.reshape(1, 3)

print(vector.shape)
print(column.shape)
print(row.shape)
```

The shapes are `(3,)`, `(3, 1)`, and `(1, 3)`, respectively. Applying `.T` to the one-dimensional `vector` does not turn it into a column vector.

For two-dimensional arrays, `(rows, inner) @ (inner, columns)` produces `(rows, columns)`. NumPy may also broadcast element-wise operations across compatible shapes. When an operation surprises you, inspect `.shape` first.

## Connect This to the MATLAB Plot Quiz

The MATLAB expression `sin(x.^2)` becomes `np.sin(sample_points ** 2)`:

```python
import numpy as np
import matplotlib.pyplot as plt

sample_points = np.linspace(0, 5, 101)
signal = np.sin(sample_points ** 2)

plt.plot(sample_points, signal)
plt.xlabel("x")
plt.ylabel("sin(x squared)")
plt.show()
```

`np.linspace(0, 5, 101)` includes both endpoints and generates the same intended 0.05 spacing as MATLAB's `0:0.05:5`. The curve starts at zero and oscillates increasingly quickly. It corresponds to Question 7 in the [MATLAB quiz](../quizzes/matlab_programming_quiz.md#question-7-recognize-a-plot).

## Division: Use Python 3 Rules

```python
print(3 / 5)
print(3 // 5)
print(-3 // 5)
```

The results are `0.6`, `0`, and `-1`.

- `/` performs ordinary division and returns a floating-point result for integer operands.
- `//` performs floor division: it rounds the quotient down toward negative infinity, not to the nearest integer.
- `from __future__ import division` was useful for Python 2. It is unnecessary in Python 3.

Use Python 3 documentation, rather than the Python 2 documentation linked in the original reading.

## Loading and Saving Pickle Data

Some course datasets may be distributed as pickle files. `pickle` is part of Python's standard library, so it does not require a separate package installation.

To load a trusted dataset:

```python
import pickle

with open("course_data.pkl", "rb") as data_file:
    data = pickle.load(data_file)
```

To save the `data` object to a new output file:

```python
with open("course_data_copy.pkl", "wb") as data_file:
    pickle.dump(data, data_file)
```

`rb` means read binary, `wb` means write binary, and `with` closes the file when the block ends. Writing with `wb` overwrites an existing file of the same name, so choose the output name deliberately.

**Security:** Only unpickle files from a trusted source. Loading a pickle can execute code. Do not use it to inspect arbitrary unknown downloads.

If a trusted legacy Python 2 dataset fails with a text-decoding compatibility error, the course data may require this loading variant:

```python
with open("course_data.pkl", "rb") as data_file:
    data = pickle.load(data_file, encoding="latin1")
```

Use that compatibility option when needed, not as a replacement for checking the file's source or diagnosing unrelated errors.

## Practice Checklist

These items remain unchecked until demonstrated; reading this summary is not a mastery check.

- [ ] Create an array and explain its `.shape`.
- [ ] Distinguish a one-dimensional array, row matrix, and column matrix.
- [ ] Select rows and columns using zero-based indexing and exclusive-stop slices.
- [ ] Explain the difference between `*` and `@` for NumPy arrays.
- [ ] Replace negative entries using a logical mask.
- [ ] Generate sample points and plot a numerical signal.
- [ ] Explain `/` versus `//` in Python 3.
- [ ] Load a trusted pickle file and explain why untrusted pickles are unsafe.
- [ ] Write a short function and use a loop without relying on a guided exercise.

The reading also mentions an optional Python programming quiz. Its 14 questions were shared on September 14, 2026 and are now saved with [answers and explanations](../quizzes/python_programming_quiz.md). Submission and score are not confirmed. The earlier [MATLAB quiz](../quizzes/matlab_programming_quiz.md) is documented separately.

## Reference Links

- [Python 3 tutorial](https://docs.python.org/3/tutorial/): focus on sections 3 (Introduction), 4 (Control Flow), 5 (Data Structures), and 6 (Modules).
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
- [Matplotlib pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Python 3 pickle documentation](https://docs.python.org/3/library/pickle.html)
- [MATLAB quiz answers and explanations](../quizzes/matlab_programming_quiz.md)