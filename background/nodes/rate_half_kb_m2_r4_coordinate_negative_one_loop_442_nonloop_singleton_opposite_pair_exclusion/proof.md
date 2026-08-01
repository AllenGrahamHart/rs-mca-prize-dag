# Proof

Put `x=r^2`.  The product minor using the loop, the two `AB` records, and
the nonsingleton `AC` record is

```text
(x^2+2bx+1)c-b(bx^2+b+2x)=0.                    (1)
```

If the coefficient of `c` vanishes, `(1)` also requires
`b(x^2+1)+2x=0`.  The resultant in `b` of these two equations is

```text
-(x-1)^2(x+1)^2.
```

Thus `x=+/-1`, which collides one of the labels `r^2,-r^2` with one of
`1,-1`.  On the guarded locus the coefficient is therefore nonzero and

```text
c=b(bx^2+b+2x)/(x^2+2bx+1).                     (2)
```

Substitute `(2)` into the q weld involving the nonsingleton `AC` record.
After deleting the nonzero factors `2i b^2 r^2(b-1)^2(b+1)^2`, its four
sign specializations factor as follows:

```text
(epsilon_1,epsilon_2)    remaining factors
(+1,+1)                  (r-1)(r-i)(r^2-i)
(+1,-1)                  (r+1)(r-i)(r^2+i)
(-1,+1)                  (r+1)(r+i)(r^2-i)
(-1,-1)                  (r-1)(r+i)(r^2+i).      (3)
```

In each row, either linear factor makes `r^2` equal to `1` or `-1`, again
colliding the labels in `(KB41O-2)`.  The quadratic factor says

```text
r^2=epsilon_2*i.
```

Then `x^2=-1`, and the guarded denominator in `(2)` is `2bx`; its numerator
is also `2b^2x`.  Therefore `(2)` gives `c=1`, contradicting distinct target
pairs `A` and `C`.

This excludes all four root-sign choices in the normalized cell.  Replacing
`C` by `-C` swaps `AC+` and `AC-`, carrying the other cell in the orbit to
this one without changing any guard. QED.
