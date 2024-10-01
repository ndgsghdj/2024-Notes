# Challenge

## Given that $x = e^{3t}\cos{3t}$ and $y = e^{3t}\sin{3t}$, show that $\frac{dy}{dx} = \tan{\left(3t + \frac{1}{4}\pi\right)}$

### Solution

$$\frac{dx}{dt} = 3e^{3t}\cos{3t} - 3e^{3t}\sin{3t}$$

$$\frac{dy}{dt} = 3e^{3t}\sin{3t} + 3e^{3t}\cos{3t}$$

$$\frac{dy}{dx} = \frac{3e^{3t}\sin{3t} + 3e^{3t}\cos{3t}}{3e^{3t}\cos{3t} - 3e^{3t}\sin{3t}}$$

$$\frac{dy}{dx} = \frac{3e^{3t}\left(\sin{3t} + \cos{3t}\right)}{3e^{3t}\left(\sin{3t} - \cos{3t}\right)}$$

$$ = \frac{\sin{3t} + \cos{3t}}{\cos{3t} - \sin{3t} }$$

$$ = \frac{1 + 2\sin{3t}\cos{3t}}{\cos{6t}}$$

$$ = \frac{1 + \sin{6t}}{\cos{6t}}$$

$$ = \frac{1}{\cos{6t}} - \tan{6t}$$

$$ = \frac{1}{\cos{6t}} + \frac{2\tan{3t}}{1 - \tan^2{3t}}$$

$$ = \frac{1}{\cos^2{3t} + \sin^2{3t}} - \frac{2\tan{3t}}{1 - \tan^2{3t}}$$

$$ = \frac{\sec^2{3t}}{1 - \tan^2{3t}} + \frac{2\tan{3t}}{1 - \tan^2{3t}}$$

$$=\frac{\sec^2{3t} + 2\tan{3t}}{1 - \tan^2{3t}}$$

$$=\frac{1 + \tan^2{3t} + 2\tan{3t}}{1 - \tan^2{3t}}$$

$$=\frac{\left(1 + \tan{3t}\right)^2}{\left(1 + \tan{3t}\right)\left(1 - \tan{3t}\right)}$$

$$=\frac{1 + \tan{3t}}{1 - \tan{3t}}$$

$$=\frac{\tan{\frac{\pi}{4}} + \tan{3t}}{ \tan{\frac{\pi}{4}} - \tan{3t}}$$

$$=\tan{\left(3t + \frac{1}{4}\pi\right)}$$

