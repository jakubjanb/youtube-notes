# Gradient Descent Intuition

Gradient descent is an iterative method for reducing a loss function. At the current parameter value, the gradient points toward the steepest local increase. Moving in the opposite direction is therefore a local strategy for decreasing the loss.

The basic update is:

```tex
\theta_{k+1} = \theta_k - \eta \nabla L(\theta_k).
```

The learning rate `eta` controls the step size. Small values can be slow; large values can overshoot.

