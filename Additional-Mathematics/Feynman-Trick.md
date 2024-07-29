# Feynman Integrals

## Find:

$$\int_0^1 \frac{x^2 -1}{\ln{x}}dx$$

I feel like for me this technique was kinda the point where you have:
- Pure Mathematics
- Integration

instead of just:
- Pure Mathematics

### Solution

$$
I = \int_0^1 \frac{x^2 - 1}{\ln{x}} dx \\
$$

$$
$$

$$
\text{Let: }
I(\alpha) = \int_0^1 \frac{x^\alpha - 1}{\ln{x}} dx \\
$$

$$
I'(\alpha) = \int_0^1 \frac{\left(x^\alpha - 1\right)\ln{x}}{\ln{x}} dx
$$

$$
= \int_0^1x^\alpha - 1 \space dx
$$

$$
= \left[\frac{x^{\alpha + 1}}{\alpha + 1} - x\right]^1_0
$$

$$
= \frac{1}{\alpha + 1}
$$

$$
I(\alpha) = \int \frac{1}{\alpha + 1} dx
$$

$$
= \ln{(\alpha + 1)} + C
$$

When $\alpha = 0$,

$$
\int_0^1\frac{x^0 - 1}{\ln{x}} = \ln{(1)} + C \\
C = 0
$$

$$
\therefore I 
= I(\alpha=2)
= \ln{3}
$$

## Feynman's Trick / Leibniz's Rule

The integral makes use of the fact that:

$$\frac{\partial}{\partial\alpha} \int_a^b f(x,\alpha)\space dx = \int_a^b \frac{\partial f}{\partial \alpha} \space dx$$

i.e. You can swap the differentiation operators and differentiate the integrand with respect to a second parameter.

Feynman's trick is used __very often__ to simplify complex integrals that would otherwise require __contour integration__.
