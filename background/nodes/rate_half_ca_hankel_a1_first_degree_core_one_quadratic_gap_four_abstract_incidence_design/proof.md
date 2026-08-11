# Proof

Extend `sigma_j` periodically to all integers. Since

```text
floor(7(j+b)/b)=floor(7j/b)+7,                       (1)
```

the word has period `b`, and telescoping gives

```text
sum_(j=0)^(b-1)sigma_j=7.                            (2)
```

For any cyclic interval of `e` consecutive starts beginning at `a`, its
number of marks is

```text
sum_(j=a)^(a+e-1)sigma_j
 =floor(7(a+e)/b)-floor(7a/b).                       (3)
```

A difference of floors in `(3)` is either the floor or ceiling of `7e/b`.
For `e>=7` and `b=3e+3`,

```text
2<7e/b<3.                                             (4)
```

Thus every length-`e` interval contains exactly two or three marks.

At start `j`, the construction creates `3-sigma_j` light points. Hence the
number of light points is

```text
sum_j(3-sigma_j)=3b-7=9e+2=3rho+5.                  (5)
```

Each one belongs to exactly `e` blocks by `(AID4)`. Block `t` sees the
length-`e` start interval ending at `t`, so its light size is

```text
sum_(j=t-e+1)^t(3-sigma_j)
 =3e-sum_(j=t-e+1)^t sigma_j
 in {3e-2,3e-3}.                                     (6)
```

Let `z` be the number of blocks of light size `3e-3`. Count incidences
between the seven marked starts and the block windows. Every marked start
lies in exactly `e` windows, while a window contains two or three marks.
Therefore

```text
7e=3z+2(b-z)=2b+z,
z=e-6.                                                (7)
```

Add `x_*` to precisely those `z` blocks. Every residual block now has

```text
3e-2=rho-1                                            (8)
```

points. Adding `s_0` makes every block size `rho`; its degree is `b`, and
the degree of `x_*` is `z=e-6`. Finally add `rho-7` inactive points. The
ambient size is

```text
1+(3rho+5)+1+(rho-7)=4rho=N.                         (9)
```

All degrees and block sizes in `(AID2)` now hold exactly. QED.
