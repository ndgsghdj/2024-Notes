# B7  Laplace Transforms

In the field of Applied Mathematics, one common type of problem that is solved is a differential equation. A differential equation is an equation in terms of an objective function's derivatives, e.g. an equation of the form:

$$af(x) + bf'(x) + cf''(x) + ...  = ...$$

The Laplace transform is an integral transform used to convert functions of time, $f(t)$, into functions of another variable, $F(s)$. This transformation makes solving differential equations simpler by converting them into algebraic equations. The Laplace transform of a function $f(t)$ is defined as:

$$\mathscr{L}\{f(t)\} = F(s) = \int_0^{\infty} e^{-st} f(t) dt$$

Some useful properties of the Laplace transform are:

1. $\mathscr{L}\{af(t) + bg(t)\} = aF(s) + bG(s)$ - Linearity
2. $\mathscr{L}\{f'(t)\} = sF(s) - f(0)$
3. $\mathscr{L}\{f''(t)\} = s^2 F(s) - sf(0) - f'(0)$

Provided is a table of functions and their Laplace transforms (Fig. 1.1)

| Function                   | Laplace Transform    |
|----------------------------|----------------------|
| 1                          | $\frac{1}{s}$        |
| $e^{at}$                   | $\frac{1}{s - a}$    |
| $t^n,\space n = 1,2,3,...$ | $\frac{n!}{s^{n+1}}$ |

( a ) Using the properties of the Laplace transform, find the Laplace transform of the following differential equation in terms of $Y(s)$ and $s$:

$$y'' - 10y' + 9y = 5t$$

( b ) Hence, given that $y(0)=-1$ and $y'(0) = 2$, solve for the function $Y(s)$

( c ) Using your answer in (b) and the Laplace Transforms in Fig. 1.1, solve for the objective function $y(t)$.
