# E1 prime-field L2 norm collision radius

- **status:** PROVED
- **closure:** proof plus exact arithmetic

Let `N=2h` be `256` or `512`, let `zeta` be a primitive `N`-th root,
and let two distinct characteristic-zero E1 classes have raw representatives
`B,B'` at swap distance

```text
s=|B\B'|=|B'\B|.
```

Fold their nonzero signed difference coefficients across antipodes:

```text
alpha=e_1(B)-e_1(B')=sum_(i=0)^(h-1) c_i zeta^i,
S=sum_i c_i^2.
```

Orthogonality over the odd cyclotomic conjugates and AM-GM give the sharper
norm bound

```text
|Norm(alpha)| <= S^(h/2).
```

Either `S<=4s-2`, or every swap is paired with its antipode; in the latter
case `alpha=2 beta` and

```text
|Norm(beta)| <= s^(h/2).
```

At every pair-feasible named anchor, `p>=2^250` and `p` is odd. Consequently:

- for `N=256`, no two distinct E1 classes at swap distance `s<=4` collide
  modulo `p`, since `14^64<2^250` and `4^64<2^250`;
- for `N=512`, no two distinct E1 classes at swap distance `s=1` collide
  modulo `p`, since `2^128<2^250`.

Thus the minimum raw-representative swap distance of a live collision is at
least five for the rates `1/4,1/8`, and at least two for rate `1/16`. This does
not bound the remaining bands or pay a row.
