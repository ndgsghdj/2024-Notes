# Generating Functions

for a sequence of numbers

$$a_1, a_2, a_3, ... a_n, ...$$

the corresponding generating function is:

$$f(x) = a_1x + a_2 x^2 + .. + a_n x^n + ...$$

$$ = \sum^{\infty}_{r = 0} a_r x^r$$
 
## Questions

### The grocery store sells paper plates in packages of $1$, $5$, $20$, or $75$. In how many different ways can Ji Ping buy a total of $95$ paper plates?

#### Solution

Buying packages of $1$ at a time:

$$1 + x + x^2 + x^3 + ... = \sum^{\infty}_{r=0} x^i = \frac{1}{1 + x}$$

Buying packages of $5$ at a time:

$$1 + x^5 + x^{10} + x^{15} + ... = \sum_{r=0}^{\infty} x^{5r} = \frac{1}{1 + x^5}$$

Buying packages of $20$ at a time:

$$1 + x^{20} + x^{40} + x^{60} + ... = \sum_{r=0}^{\infty} x^{20r} = \frac{1}{1 + x^{20}}$$

Buying packages of $75$ at a time:

$$1 + x^{75}$$

Expanding this binomial expansion would then yield the solution as a coefficient of $x^{95}$:

$$(1 + x + x^2 + x^3 + ...)\left(1 + x^5 + x^{10} + ...\right)\left(1 + x^{20} + x^{40} + ...\right)\left(1 + x^{75}\right)$$

