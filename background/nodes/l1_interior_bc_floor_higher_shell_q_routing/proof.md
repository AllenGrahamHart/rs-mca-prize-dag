# Proof - L1 interior BC floor routes to higher-shell Q

## 1. Complete agreement is `m'`

Both `U` and `L_M'` are monic of degree `m'` and have the same next
`d_1-1` coefficients.  Their difference therefore has degree at most

```text
m'-d_1=k-1,
```

so `(FR2)` is a codeword.  Moreover

```text
U-c_M'=L_M'.                                       (1)
```

The right side has exactly the `m'` distinct roots `M'`.  Hence the complete
agreement set is exactly `M'`, not merely a support containing it.

## 2. The level-`m` guard deletes every sub-support

Let `T subset M'` have size `m`.  Write `L_T` for its locator and

```text
Q=L_M'/L_T=L_(M'\T),       W=Omega/L_T.             (2)
```

The agreement cofactor `Q` has positive degree because `m'>m`.  Every root
of `Q` lies in `M'\T`, hence in `H\T`, which is the root set of `W`.
Therefore `Q|W`, so `gcd(Q,W)!=1`.  This is precisely failure of the
complete-agreement guard at level `m`.  At level `m'`, equation `(1)` has
cofactor one and the complete support is retained once.

Since `m'-k=d_1-1`, identity `(FR3)` follows.  The floor codeword is thus a
boundary-Q member at its true shell, even though all its `m`-subsupports
appear in the unguarded strict-interior support census.

## 3. Binomial inversion

One codeword with complete agreement `m'` contributes `binom(m',t)` to the
support moment `C_t` for every `t<=m'`.  Its coefficient in the inverse for
`Z_m` is

```text
sum_(t=m)^m' (-1)^(t-m) binom(t,m) binom(m',t)
=binom(m',m) sum_(j=0)^(m'-m) (-1)^j binom(m'-m,j)
=0,
```

because `m'>m`.  This proves `(FR5)` and shows that all codewords in the
heaviest prefix fiber cancel independently.  Multiplying by the guaranteed
fiber size in Paper D gives `(FR4)` as deleted support multiplicity, not an
exact level-`m` floor.
