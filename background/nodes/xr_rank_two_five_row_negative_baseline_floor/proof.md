# Proof

For a full minimal Maxwell core, the collision-defect identity gives

```text
-e=Delta=D_0+2C<=0,
C=3I+sigma+H>=0,
0<=e<=h-1.                                           (1)
```

Hence `D_0<=0`. The zero-baseline arithmetic router excludes odd active-row
arity at every official odd reserve, so `D_0!=0` and therefore `D_0<0`.

For five rows the baseline formula is `(F5N1)`. Put `b=-D_0`. Reduction
modulo six gives

```text
b congruent -5h (mod 6),
```

proving `(F5N2)`. Since `h` is odd, `b_0` is one of `1,3,5`.

Solving `(F5N1)` for the zero mass gives

```text
Z=(5h+12D+b)/6.                                     (2)
```

Every one of the five disjoint zero fibers has size at most `d=D-1`.
Consequently

```text
(5h+12D+b)/6=Z<=5(D-1),
```

or

```text
D>=(5h+b+30)/18.                                   (3)
```

Both `D` and the rank floor increase with `b`, so replace `b` by its least
positive permitted value `b_0` and take the integer ceiling in `(3)`. The
five zero fibers are disjoint subsets of `|X|=a+D`, so `Z<=a+D`. Substitute
`(2)` to obtain

```text
a>=Z-D=(5h+6D+b)/6.
```

This is increasing in both `D,b`, proving `(F5N3)`.

Finally `(1)` with `D_0=-b` gives `b=e+2C`. The range
`0<=e<=h-1` and nonnegativity of `C` give exactly `(F5N4)`. Substitution of
the four official reserve classes computes the table. The verifier checks the
residue, capacity inequality, rank floor, and defect window using exact
integers. QED.
