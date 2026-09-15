# Python Programming Quiz: Answers and Explanations

**Course:** University of Washington, Computational Neuroscience (Coursera)
**Recorded:** September 14, 2026
**Source:** The 14 Python Programming practice questions shared as screenshots in this session.
**Status:** Study answer key, not an official course answer key. Submission, score, and independent mastery have not been confirmed.

**Executed companion:** [Python quiz notebook](python_programming_quiz.ipynb), with runnable examples, saved outputs, assertions, and the Question 10 plot. All 14 examples completed their checks on September 14, 2026; the Question 14 breakpoint is disabled during unattended execution.

Options are numbered from top to bottom in the screenshots. Plot and matrix choices are described in text; screenshots are not embedded. Some incorrect choices are paraphrased for readability. Examples assume Python 3 and `import numpy as np` unless the question concerns that import itself.

## Quick Answer Key

| Question | Correct option(s) | Answer |
|---|---|---|
| 1 | 2 | Four rows: `[[1,2,3], [2,3,4], [3,4,5], [4,5,6]]` |
| 2 | 1 | `B = A[[0, 2], 1:]` |
| 3 | 3 | Put `import numpy as np` at the start, before using `np`. |
| 4 | 2, 3, 5, 6, 7 | `np.ones(5,)`, `a[4:]`, `a[:5]`, `np.ones((5,5))`, and `a[:2]` |
| 5 | 2 | `x = np.random.rand(100)` |
| 6 | 4 | `x[x > 0.5] = 1` |
| 7 | 4 | `(x > 1).nonzero()[0][:3]` |
| 8 | 1 | Open in binary read mode, then `data = pickle.load(f)`. |
| 9 | 1 | `data['b'] = 100` |
| 10 | 3 | Starts at zero, stays between -1 and 1, and oscillates increasingly quickly. |
| 11 | 2 | `y = x**3` |
| 12 | 2 | `[[4,9], [9,0], [0,0]]` |
| 13 | 1, 2, 4 | All three versions using membership: `x in [2, 5, 9]`. |
| 14 | 1 | Interrupt execution and temporarily give interactive debugger control to the user. |

## Question 1: Interpret a Nested Array

Which matrix corresponds to this code?

```python
A = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
```

**Correct answer:** Option 2.

```text
[[1 2 3]
 [2 3 4]
 [3 4 5]
 [4 5 6]]
```

Each inner list becomes a row. There are four inner lists with three entries each, so `A.shape` is `(4, 3)`.

**Other choices:** A single column and a single row would require reshaping or flattening; the 3-by-4 matrix in option 4 exchanges rows and columns and is not produced by this constructor.

## Question 2: Select Rows and Columns

Given:

```python
A = np.array([[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6]])
```

Which expression produces `B = [[2, 3, 4], [4, 5, 6]]`?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `B = A[[0, 2], 1:]` | Yes | Selects first and third rows, then columns from index 1 to the end. |
| 2 | `B = A[[1, 3], 2:]` | No | Row index 3 is out of bounds for an array with three rows. |
| 3 | `B = A[:, :]` | No | Selects the whole array. |
| 4 | `B = A[[0, 2], 2:]` | No | Selects the correct rows but only the final two columns. |

**Correct answer:** Option 1.

**Rule:** NumPy uses `array[rows, columns]` with zero-based indices. The list `[0, 2]` selects particular rows; `1:` selects everything starting with the second column.

## Question 3: Fix an Undefined Alias

The script contains `A = np.array([1, 2, 3])` and raises `NameError: name 'np' is not defined`. How do you correct it?

**Correct answer:** Option 3, insert this at the start of the script:

```python
import numpy as np

A = np.array([1, 2, 3])
```

`np` is not built into Python. The import binds that name to the NumPy module before the array expression runs.

**Other choices:** `from numpy import *` does not establish the `np` alias. Putting the correct import at the end is too late: execution already failed at the earlier use of `np`.

## Question 4: Which Commands Avoid Errors?

Given `a = np.array([1, 2, 3, 4])`, which commands do not raise an error? Select all that apply.

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `b = np.ones(5, 5)` | No | The second positional argument is a data type, not a second dimension. Integer `5` is not a valid dtype here. |
| 2 | `b = np.ones(5,)` | Yes | Calls `np.ones` with the single shape argument `5`. The trailing comma does not add an argument. Result shape: `(5,)`. |
| 3 | `b = a[4:]` | Yes | A slice starting at the end returns an empty array. Result shape: `(0,)`. |
| 4 | `b = a[4]` | No | Direct indexing at 4 is out of bounds; valid indices are 0 through 3. |
| 5 | `b = a[:5]` | Yes | Slicing clips the stop to the available data, returning `[1, 2, 3, 4]`. |
| 6 | `b = np.ones((5, 5))` | Yes | A tuple supplies both dimensions. Result shape: `(5, 5)`. |
| 7 | `b = a[:2]` | Yes | Returns the first two elements: `[1, 2]`. |

**Correct answer:** Options 2, 3, 5, 6, and 7.

**Rule:** Out-of-range scalar indexing raises an error, but out-of-range slice boundaries can produce clipped or empty results. A NumPy shape tuple is one argument: `np.ones((rows, columns))`.

## Question 5: Generate Uniform Random Numbers

Which code generates an array of 100 random numbers between 0 and 1?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `x = random(100)` | No | No callable named `random` has been defined by importing NumPy as `np`. |
| 2 | `x = np.random.rand(100)` | Yes | Returns a one-dimensional array of 100 uniform random samples in `[0, 1)`. |
| 3 | `x = np.random(100)` | No | `np.random` is a module, not a callable function. |

**Correct answer:** Option 2.

The upper endpoint 1 is excluded. For new code, a modern equivalent is `np.random.default_rng().random(100)`, but it is not one of the quiz choices. A seed can make a sequence reproducible; it is not required to answer this question.

## Question 6: Replace Selected Values

Suppose `x` contains 100 random numbers between 0 and 1. Which code sets every element greater than 0.5 to 1?

**Correct answer:** Option 4.

```python
x[x > 0.5] = 1
```

`x > 0.5` creates a Boolean mask. The bracketed selection updates only the entries where the mask is true. Values equal to 0.5 remain unchanged because the comparison is strictly greater than.

Example: `[0.2, 0.5, 0.8]` becomes `[0.2, 0.5, 1.0]`.

**Other choices:** Assigning to the comparison itself is invalid syntax; an index missing the left side of the comparison is also invalid. `if x > 0.5: x = 1` does not perform element-wise updates and raises an ambiguous-truth-value error for this multi-element array.

## Question 7: Find the First Three Matching Indices

Which expression returns the numerical indices of the first three elements of a one-dimensional `x` that are greater than 1?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `x[:3] > 1` | No | Returns a Boolean mask for the first three positions, not matching indices from the full array. |
| 2 | `(x > 1)[:3]` | No | Also returns only the first three entries of a Boolean mask. |
| 3 | `x[x > 1][:3]` | No | Returns the matching values, not their original indices. |
| 4 | `(x > 1).nonzero()[0][:3]` | Yes | Gets indices of true entries, extracts the index array, then keeps the first three. |

**Correct answer:** Option 4.

For `x = np.array([0, 4, 1, 6, 7, 0, 8])`:

1. `x > 1` gives `[False, True, False, True, True, False, True]`.
2. `.nonzero()` returns a tuple containing the index array `[1, 3, 4, 6]`.
3. `[0]` selects that array from the tuple.
4. `[:3]` returns `[1, 3, 4]`.

If fewer than three elements match, the expression returns the available indices without an error. A concise alternative for a one-dimensional array is `np.flatnonzero(x > 1)[:3]`.

## Question 8: Load a Pickled Dictionary

Which code loads the dictionary stored in the accessible file `data.pickle` into the variable `data`?

**Correct answer:** Option 1.

```python
import pickle

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
```

`open(..., 'rb')` opens a binary stream. `pickle.load(f)` deserializes the saved object, which is a dictionary according to the question. The `with` block closes the stream afterwards.

**Other choices:** `f.open()` is not the loading method of an open file; `data = f` assigns a file object rather than the dictionary; and `pickle.open(...)` is not a pickle API.

**Security:** Only load trusted pickle files. Deserialization can execute code. The file name alone says nothing about whether a file is safe.

## Question 9: Update a Dictionary Entry

Given `data = {'a': 3, 'c': 9, 'b': 5}`, how do you set the value for key `'b'` to 100?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `data['b'] = 100` | Yes | Assigns to the dictionary entry whose key is the string `'b'`. |
| 2 | `data.b = 100` | No | Attribute notation does not update a standard dictionary key. |
| 3 | `set(data, b, 100)` | No | `set` constructs a set; it is not a dictionary assignment function. |
| 4 | `data('b') = 100` | No | A function call is not a valid assignment target. |

**Correct answer:** Option 1.

The resulting dictionary has the same other entries, with `'b': 100`. Dictionary keys use square brackets, and string keys need quotes.

## Question 10: Identify the Sine Plot

Which plot results from this script?

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, step=0.05)
y = np.sin(x**2)
plt.plot(x, y)
plt.show()
```

**Correct answer:** Option 3, the densely sampled curve starting at zero with values between -1 and 1.

| Option | Plot description | Correct? |
|---|---|---|
| 1 | Starts at 1 and oscillates increasingly quickly. | No |
| 2 | Starts at zero but reaches approximately 2 and -2. | No |
| 3 | Starts at zero, stays between -1 and 1, and oscillates increasingly quickly. | Yes |
| 4 | The visibly coarse, jagged version. | No |

**Explanation:** The function is $y = \sin(x^2)$, not $\cos(x^2)$, $2\sin(x^2)$, or $\sin^2(x)$.

- At `x = 0`, `y = 0`.
- The sine amplitude is 1.
- The phase derivative is $2x$, so oscillations become more frequent as x increases.
- `np.arange(0, 5, step=0.05)` produces 100 points from 0 through 4.95; the stop value 5 is excluded.
- The first peak is near $x = \sqrt{\pi/2} \approx 1.253$.

Unlike the earlier MATLAB quiz's `0:0.05:5`, this exact Python expression does not include 5. The [Python one-pager](../notes/python_one_pager.html) uses `np.linspace(0, 5, 101)` to include both endpoints in its MATLAB translation.

## Question 11: Cube Every Element

Given `x = np.array([1, 2, 3, 4, 5])`, which expression creates an array containing the cube of every element?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `y = x.^3` | No | MATLAB-style syntax, not valid Python. |
| 2 | `y = x**3` | Yes | NumPy applies exponentiation element-wise. |
| 3 | `y = x*3` | No | Multiplies each value by 3 rather than cubing it. |

**Correct answer:** Option 2.

The result is `[1, 8, 27, 64, 125]`. In Python, `**` means exponentiation; `^` means bitwise XOR and is not a substitute.

## Question 12: Trace Scaling, Masking, and Transposition

What is the mathematical representation of `x` after this sequence?

```python
x = np.array([[1, 2, 3], [2, 3, 4]])
x *= 5
x -= 1
x[x > 10] = 0
x = x.T
```

**Correct answer:** Option 2.

```text
[[4 9]
 [9 0]
 [0 0]]
```

Trace the array in order:

| Step | Array |
|---|---|
| Initial | `[[1, 2, 3], [2, 3, 4]]` |
| Multiply by 5 | `[[5, 10, 15], [10, 15, 20]]` |
| Subtract 1 | `[[4, 9, 14], [9, 14, 19]]` |
| Replace entries greater than 10 with zero | `[[4, 9, 0], [9, 0, 0]]` |
| Transpose | `[[4, 9], [9, 0], [0, 0]]` |

**Other choices:** They either omit a transformation, mask the wrong entries, or keep the original 2-by-3 orientation. The final shape must be `(3, 2)`.

## Question 13: Test Membership

Which pieces of code set `y` to `True` if scalar `x` is 2, 5, or 9, and to `False` otherwise? Select all that apply.

### Option 1

```python
y = False
if x in [2, 5, 9]:
    y = True
```

Correct: `y` starts false and changes only on a match.

### Option 2

```python
if x in [2, 5, 9]:
    y = True
else:
    y = False
```

Correct: both outcomes are explicitly assigned.

### Option 3

```python
if x == [2, 5, 9]:
    y = True
else:
    y = False
```

Incorrect: comparing a scalar to an entire list is not a membership test. For an ordinary Python integer, the equality is false, even for 2, 5, or 9.

### Option 4

```python
y = x in [2, 5, 9]
```

Correct: the membership expression itself produces the required Boolean.

**Correct answer:** Options 1, 2, and 4.

**Rule:** `in` tests membership; `==` tests equality. Option 4 is the shortest direct expression of the requirement.

## Question 14: Enter the Debugger

What does `import pdb; pdb.set_trace()` do inside a script? For example:

```python
x = np.arange(5)
y = -np.arange(5)
x[y < -2] = 0
import pdb; pdb.set_trace()
x = 9
print(x)
```

| Option | Description | Correct? |
|---|---|---|
| 1 | Interrupts execution and temporarily gives control to the user. | Yes |
| 2 | Halts the program until the user presses a key. | No |
| 3 | Saves all variables to a file called `pdb`. | No |
| 4 | Prints all local data to the console. | No |

**Correct answer:** Option 1.

It enters Python's interactive debugger. Before the subsequent assignment `x = 9`, the array is `[0, 1, 2, 0, 0]`, and you can inspect it at the debugger prompt.

- `p x`: print the current value of `x`.
- `n`: execute the next line.
- `c`: continue normal execution.
- `q`: quit the debugging session, normally terminating this script.

It does not save variables or dump them automatically. In modern Python, `breakpoint()` is the usual shortcut; by default it invokes the same debugger, though its behavior is configurable.

## Practical Takeaways

- Nested lists establish rows; use `.shape` to confirm dimensions.
- Distinguish out-of-range scalar indexing from clipped or empty slices.
- Pass multi-dimensional shapes as a single tuple.
- Boolean masks select entries; `.nonzero()[0]` retrieves their indices for a 1D array.
- Import names before using them, and deserialize only trusted pickle files.
- Use `**` for powers and `in` for membership.
- Trace in-place operations sequentially, then apply the transpose.

## Related Study Materials

- [Python practical summary](../notes/python_information_and_tutorials.md)
- [Python HTML one-pager](../notes/python_one_pager.html)
- [MATLAB quiz answers and explanations](matlab_programming_quiz.md)