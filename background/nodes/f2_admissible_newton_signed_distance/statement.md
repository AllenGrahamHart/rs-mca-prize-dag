# Plus-branch admissible F2 Newton signed-distance transport

- **status:** PROVED
- **closure:** proof

Let one class of an official plus-branch (`p=1 mod 4`) admissible F2 kernel
have support

```text
1,zeta,...,zeta^(S-1),   ord(zeta)=2S,
```

over `F_p`, and suppose the imposed moments include
`1,3,...,2R-1`.  Every nonzero

```text
eps in ker(A_c) intersect {-1,0,1}^S
```

has Hamming weight at least `2R+1`.  If `2R>=S`, the intersection is
trivial.  Consequently

```text
Z_1 = 1 + sum_(eps != 0, wt(eps)>=2R+1) 2^-wt(eps).
```

At the banked maximal generating witness,

```text
S=2^38,
R=4,294,967,340,
2R+1=8,589,934,681=S/32+89.
```

The theorem applies class by class on generating and non-generating
plus-branch admissible rows. It makes no claim for `p=3 mod 4`. It is a
distance theorem, not an upper bound on `Z_1`.
