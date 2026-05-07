# Envelope Curves

## Summary

Envelope curves appear when a family of simpler curves has a shared limiting edge. This note derives the envelope conditions \(F=0\) and \(F_t=0\), applies them to a parabola from lines, proves that the string-art connector construction gives a quadratic Bezier curve, and models the bright curve at the bottom of a mug as a reflected-ray caustic.

## Key Ideas

- Envelope candidates satisfy both the family equation and the parameter derivative equation.
- A finite line drawing approximates a continuous line-family envelope.
- The string-art construction is the tangent-line family of a quadratic Bezier curve.
- Coffee-cup caustics are envelopes of reflected light rays under geometric optics.

## Important Equations

```tex
F(x,y,t)=0,\qquad F_t(x,y,t)=0

B(t)=(1-t)^2P_0+2(1-t)tP_1+t^2P_2

c_R(\theta)=
R\left(
\frac{3\cos\theta-\cos3\theta}{4},
\frac{3\sin\theta-\sin3\theta}{4}
\right)
```

## Related Notes

- Marden's Theorem
