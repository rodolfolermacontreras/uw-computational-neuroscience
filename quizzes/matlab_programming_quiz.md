# MATLAB Programming Quiz: Answers and Explanations

**Course:** University of Washington, Computational Neuroscience (Coursera)
**Recorded:** September 13, 2026
**Source:** The 14 questions shared as screenshots in this study session.
**Status:** Study answer key with explanations, not an official course answer key. Submission, score, and independent mastery have not been confirmed.

Option numbers follow the screenshots from top to bottom. Matrix notation and code are retained; the plot choices in Question 7 are described in words because the screenshots are not stored in this file.

## Quick Answer Key

| Question | Correct option(s) | Answer |
|---|---|---|
| 1 | 2, 4 | `[1; 2; 3]` and `[1 2 3]'` |
| 2 | 4 | `A(:,2:3)` |
| 3 | 1, 2, 3, 5 | `C * E`, `C .* E`, `d * B`, `A * B'` |
| 4 | 1, 3 | `B - [d' d'*2]` and `B + repmat(f',3,1)` |
| 5 | 2 | `ones(4,1) * 5` |
| 6 | 1, 4 | `[A(:,1) A(:,3) A(:,5)]` and `A(:,1:2:5)` |
| 7 | 3 | The more densely sampled curve starting at zero, with increasingly frequent oscillations |
| 8 | 4 | `[4 0 3 8 3]` |
| 9 | 4 | `7.63e-06` |
| 10 | 5, 6 | `zeros(2,3)` and `[0 0 0; 0 0 0]` |
| 11 | 3 | `A(A < 0) = 0` |
| 12 | 2 | `C = A .* B` |
| 13 | 3 | `find(x == 3, 1)` |
| 14 | 2 | Suspend execution and enter interactive debugging mode |

## Question 1: Create a Column Vector

Which expressions generate the column vector `[1; 2; 3]`? Select all correct answers.

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `[1, 2, 3]` | No | Commas separate entries within one row, giving a 1-by-3 row vector. |
| 2 | `[1; 2; 3]` | Yes | Semicolons separate rows, giving a 3-by-1 column vector. |
| 3 | `[1 2 3]` | No | Spaces also separate entries within one row. |
| 4 | `[1 2 3]'` | Yes | Transposing this real-valued row vector produces a column vector. |

**Correct answer:** Options 2 and 4.

**Rule:** Inside square brackets, spaces or commas join entries horizontally; semicolons join rows vertically. MATLAB's `'` is conjugate transpose, while `.'` is transpose without conjugation. They give the same result for these real numbers.

## Question 2: Select Matrix Columns

Given:

```matlab
A = [1 2 3;
     2 3 4;
     3 4 5;
     4 5 6];
```

Which expression returns `[2 3; 3 4; 4 5; 5 6]`?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `A(2:3,:)` | No | Selects rows 2 and 3, not columns 2 and 3. |
| 2 | `A(:,2)` | No | Selects only column 2. |
| 3 | `A(:,:)` | No | Returns the entire matrix. |
| 4 | `A(:,2:3)` | Yes | Selects every row and columns 2 through 3. |

**Correct answer:** Option 4.

**Rule:** Index as `A(rows, columns)`. A standalone `:` means all entries along that dimension. MATLAB ranges include the endpoint when the step reaches it.

## Question 3: Check Operation Dimensions

Given:

```matlab
A = [1 2; 3 4];
B = [2 2; 3 3; 4 4];
C = eye(3);
d = [1 2 3];
E = zeros(3,3);
```

Which commands will NOT give an error? Select all correct answers.

The shapes are: `A` is 2-by-2, `B` is 3-by-2, `C` and `E` are 3-by-3, and `d` is 1-by-3.

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `C * E` | Yes | Matrix multiplication: (3-by-3) times (3-by-3) gives 3-by-3. |
| 2 | `C .* E` | Yes | Element-wise multiplication of two identically shaped arrays. |
| 3 | `d * B` | Yes | (1-by-3) times (3-by-2) gives 1-by-2, specifically `[20 20]`. |
| 4 | `A - B` | No | Shapes 2-by-2 and 3-by-2 are incompatible. |
| 5 | `A * B'` | Yes | `B'` is 2-by-3, so (2-by-2) times (2-by-3) gives 2-by-3. |
| 6 | `A * B` | No | Inner dimensions 2 and 3 do not match. |

**Correct answer:** Options 1, 2, 3, and 5.

**Rule:** For matrix multiplication, `(m-by-n) * (n-by-p)` gives `m-by-p`. `.*` multiplies corresponding elements. Modern MATLAB supports implicit expansion for compatible element-wise operations, but the 2-versus-3 row mismatch in `A - B` is still invalid.

## Question 4: Concatenation and Repetition

Given:

```matlab
B = [2 2; 3 3; 4 4];
d = [1 2 3];
f = [8; 9];
```

Which commands will NOT give an error? Select all correct answers.

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `B - [d' d'*2]` | Yes | Both `d'` and `d'*2` are 3-by-1. Joining them horizontally gives 3-by-2, matching `B`. |
| 2 | `B - repmat(f,1,3)` | No | Repeating the 2-by-1 vector across three columns gives 2-by-3, incompatible with `B`. |
| 3 | `B + repmat(f',3,1)` | Yes | `f'` is 1-by-2. Repeating it down three rows gives 3-by-2. |
| 4 | `B + [f; f; f]` | No | Stacking three 2-by-1 vectors gives 6-by-1, incompatible with `B`. |

**Correct answer:** Options 1 and 3.

**Rule:** `repmat(array, rowCopies, columnCopies)` tiles an array. Work out the resulting shape before adding or subtracting it.

## Question 5: Create a Constant Vector

Which expression creates a 4-by-1 vector containing 5 in every position?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `fives(4,1)` | No | `fives` is not a standard MATLAB function. |
| 2 | `ones(4,1) * 5` | Yes | Creates four rows of ones, then scales every entry by 5. |
| 3 | `ones(4) * 5` | No | Creates a 4-by-4 matrix of fives. |
| 4 | `ones(4,1)` | No | Correct shape, but the values are 1. |
| 5 | `eye(4) * 5` | No | Creates a 4-by-4 matrix with 5 on its diagonal and 0 elsewhere. |

**Correct answer:** Option 2.

**Rule:** `ones(n)` creates an n-by-n matrix. Specify both dimensions when you want a vector: `ones(n,1)`.

## Question 6: Select Every Other Column

Given:

```matlab
A = [1 2 3 4 5;
     2 3 4 5 6;
     3 4 5 6 7;
     4 5 6 7 8;
     5 6 7 8 9];
```

Which expressions return the following matrix? Select all correct answers.

```matlab
[1 3 5;
 2 4 6;
 3 5 7;
 4 6 8;
 5 7 9]
```

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `[A(:,1) A(:,3) A(:,5)]` | Yes | Joins columns 1, 3, and 5 horizontally. |
| 2 | `[A(1,:) A(1,:) A(1,:)]` | No | Repeats the first row horizontally, producing a 1-by-15 row vector. |
| 3 | `A(:,1:3)` | No | Selects columns 1, 2, and 3. |
| 4 | `A(:,1:2:5)` | Yes | `1:2:5` generates column indices `[1 3 5]`. |
| 5 | `A(1:2:5,:)` | No | Selects every other row instead of every other column. |

**Correct answer:** Options 1 and 4.

**Rule:** `start:step:stop` generates regularly spaced indices.

## Question 7: Recognize a Plot

What plot results from this code?

```matlab
x = 0:0.05:5;
y = sin(x.^2);
plot(x,y);
```

| Option | Plot description from the screenshots | Correct? |
|---|---|---|
| 1 | Starts at zero but has visibly coarse, jagged segments and poorly sampled later peaks. | No |
| 2 | Starts at 1, then oscillates increasingly quickly. | No |
| 3 | Starts at zero and is more densely sampled, with increasingly frequent oscillations. | Yes |

**Correct answer:** Option 3, the lower plot in the second screenshot for this question.

**Explanation:** `x.^2` squares each element before taking the sine. Thus the plotted function is $y = \sin(x^2)$, not $\sin^2(x)$ or $\cos(x^2)$.

- At `x = 0`, the value is `sin(0) = 0`, ruling out option 2.
- The phase is $x^2$, so its derivative is $2x$: oscillations become faster as x increases.
- The first peak is at $x = \sqrt{\pi/2} \approx 1.253$.
- The samples are spaced 0.05 apart, giving 101 points from 0 through 5. This matches the more densely sampled third plot.
- At `x = 5`, the value is $\sin(25) \approx -0.132$.

**Rule:** Read the initial value, changing oscillation rate, and sampling density before choosing a plot.

## Question 8: Trace a Loop

What is `b` after this code executes?

```matlab
A = [1 0 -4 8 3; 4 -2 3 3 1];
b = zeros(1,5);
for index = 1:size(A,2)
    if A(1,index) > A(2,index)
        b(index) = A(1,index);
    else
        b(index) = A(2,index);
    end
end
```

| Option | Answer | Correct? |
|---|---|---|
| 1 | `[1 0 -4 8 3]` | No |
| 2 | `[4 -2 3 3 1]` | No |
| 3 | `[1 -2 -4 3 1]` | No |
| 4 | `[4 0 3 8 3]` | Yes |
| 5 | None of these | No |

**Correct answer:** Option 4.

**Explanation:** `size(A,2)` is the number of columns, 5. Each iteration copies the larger value from the current column into `b`.

| Column | First row | Second row | Selected value |
|---|---|---|---|
| 1 | 1 | 4 | 4 |
| 2 | 0 | -2 | 0 |
| 3 | -4 | 3 | 3 |
| 4 | 8 | 3 | 8 |
| 5 | 3 | 1 | 3 |

The equivalent vectorized expression for this matrix is `b = max(A,[],1)`.

## Question 9: Trace a While Loop

What is `x`, rounded to three significant figures, after this code executes?

```matlab
x = 1;
while x > 1e-5
    x = x / 2;
end
```

| Option | Answer | Correct? |
|---|---|---|
| 1 | `7.63e-05` | No |
| 2 | `1` | No |
| 3 | `1.53e-05` | No |
| 4 | `7.63e-06` | Yes |
| 5 | `3.81e-06` | No |

**Correct answer:** Option 4.

**Explanation:** After n iterations, $x = 2^{-n}$.

- After 16 iterations: $x = 0.0000152587890625 > 0.00001$, so the loop continues.
- After 17 iterations: $x = 0.00000762939453125 \leq 0.00001$, so the loop stops.
- Rounded to three significant figures: `7.63e-06`.

**Rule:** The loop stops at the first value that makes its condition false, not necessarily at the threshold itself.

## Question 10: Create a Zero Matrix

Which expressions create a 2-by-3 matrix containing only zeros? Select all correct answers.

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `zeros(2)` | No | Creates a 2-by-2 matrix. |
| 2 | `zeros(3)` | No | Creates a 3-by-3 matrix. |
| 3 | `zeros(3,2)` | No | Creates three rows and two columns. |
| 4 | `eye(2,3)` | No | Has ones on its main diagonal, so it is not all zeros. |
| 5 | `zeros(2,3)` | Yes | Creates two rows and three columns of zeros. |
| 6 | `[0 0 0; 0 0 0]` | Yes | Explicitly supplies two rows of three zeros. |
| 7 | `[0 0; 0 0; 0 0]` | No | Explicitly supplies three rows of two zeros. |

**Correct answer:** Options 5 and 6.

**Rule:** Array constructors take dimensions in row, column order.

## Question 11: Replace Negative Entries

Given:

```matlab
A = [5 -2 3;
     2 -3 4;
     3 4 -8];
```

Which expression sets the negative entries of `A` to zero while preserving the other entries?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `A < 0 = 0` | No | Not valid assignment syntax. |
| 2 | `(A < 0) = 0` | No | Cannot assign to a comparison expression this way. |
| 3 | `A(A < 0) = 0` | Yes | Uses a logical mask to select and replace negative entries. |
| 4 | `A(:) = 0` | No | Sets every entry to zero, including the positive entries. |

**Correct answer:** Option 3.

**Explanation:** `A < 0` creates a logical array identifying the negative entries. `A(A < 0)` selects those entries for assignment. The result is `[5 0 3; 2 0 4; 3 4 0]`.

## Question 12: Element-Wise Multiplication

Given `A = [1; 2; 3]` and `B = [-1; -2; -3]`, which expression produces `C = [-1; -4; -9]`?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `C = A * B` | No | Matrix multiplication fails: (3-by-1) times (3-by-1) has incompatible inner dimensions. |
| 2 | `C = A .* B` | Yes | Multiplies matching entries: `1*(-1)`, `2*(-2)`, and `3*(-3)`. |
| 3 | `C = A' * B` | No | Gives the scalar dot product `-14`, not a column vector. |

**Correct answer:** Option 2.

**Rule:** A dot before `*`, `/`, or `^` indicates the element-wise version of that operation.

## Question 13: Find the First Matching Index

Given `x = [1 1 2 2 1 3 2 2 3 1]`, which expression returns the index of the first element equal to 3?

| Option | Expression | Correct? | Explanation |
|---|---|---|---|
| 1 | `x == 3` | No | Returns a logical mask, not an index. |
| 2 | `find(x == 3)` | No | Returns both matching indices, `[6 9]`. |
| 3 | `find(x == 3, 1)` | Yes | Limits the result to the first matching index, `6`. |
| 4 | `x = 3` | No | Assigns 3 to `x`, replacing the original vector. |

**Correct answer:** Option 3.

**Rule:** `==` compares; `=` assigns. MATLAB indices start at 1.

## Question 14: Understand the Keyboard Command

What does `keyboard` do when placed in a MATLAB script? For example:

```matlab
x = 5;
y = [3 5 7];
z = x * y;
keyboard;
w = z .^ 2;
```

| Option | Answer | Correct? | Explanation |
|---|---|---|---|
| 1 | Halts the program until the user presses a key on the keyboard. | No | Describes the behavior of `pause` without an argument. |
| 2 | Stops execution of the program and gives control to the keyboard. | Yes | Suspends the script and enters interactive debugging mode. |
| 3 | Collects character input and stores it in the most recently referenced variable. | No | `keyboard` does not collect and assign input this way. |

**Correct answer:** Option 2.

**Explanation:** At the `K>>` prompt, you can inspect and change variables and run commands in the paused workspace. Here, `z` is `[15 25 35]`; the assignment to `w` has not run yet. Use `dbcont` to resume. If nothing was changed while paused, `w` then becomes `[225 625 1225]`.

## Practical Review

- Check array dimensions before doing arithmetic.
- Use `A(rows, columns)` and remember MATLAB's 1-based indexing.
- Distinguish horizontal concatenation with spaces from vertical concatenation with semicolons.
- Use `.*` and `.^` for element-wise calculations; use `*` for matrix multiplication.
- Trace loops one iteration at a time, especially the final condition check.
- Distinguish logical masks, matching indices, and assignment.
- Recognize plots using their starting value, oscillation rate, and sample spacing.