# Proof

Use the kernel-basis pencils from the proved affine-core all-zero charge. For
each coordinate basis `T` of the kernel slice, let

```text
e_T(gamma)=b_T+gamma q_T,
```

let `p_T` be the number of persistent coordinates outside `T`, and let `M_T`
be the number of selected pairs for which `T` is a basis contained in the
error zero set. Since

```text
c=n-r-a=k+h-a,
```

the all-zero argument gives

```text
M_T(c-p_T) <= n-a-p_T.                                (1)
```

If `M_T>=2`, choose two distinct slopes counted by `M_T`. A coordinate
outside `T` vanishes at both slopes exactly when its affine coordinate
polynomial is persistent. Hence the common zero set of the two selected
errors is exactly `T` together with the `p_T` persistent coordinates. The
post-strip core hypothesis gives

```text
a+p_T <= kappa.                                      (2)
```

The ratio on the right side of `(1)` is increasing in `p_T`, because

```text
(n-a-p)/(k+h-a-p)=1+r/(k+h-a-p).
```

Using `(2)` therefore yields

```text
M_T
 <= floor((n-a-p_T)/(k+h-a-p_T))
 <= floor((n-kappa)/(k+h-kappa)).                    (3)
```

If `M_T<=1`, the same bound holds because `R>=h` and `kappa<=k` make the
last floor at least one.

As in the cogirth theorem, every selected pair contributes at least
`C(h+a,a)` kernel bases contained in its zero set. There are at most
`C(n,a)` coordinate `a`-sets, and `(3)` bounds the number of pairs over each
one. Counting pair-basis incidences gives `(PSP)`.

The proved strip rung supplies `kappa=k` for every post-strip selector. In
the low-core stratum the defining pairwise bound supplies `kappa=k-1`.
Substitution in `(PSP)` gives the six exact paid ranks
`4,4,4,15,15,14`, as replayed by `verify.py`.
