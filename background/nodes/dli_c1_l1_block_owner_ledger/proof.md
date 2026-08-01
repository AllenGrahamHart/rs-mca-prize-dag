# Proof

Signed differences on the first `4(j+1)` coordinates split uniquely into a
difference on the first `4j` coordinates and a difference on block `j`.
Ternary weight is additive across this split, hence
`K_(j+1)=K_j*kappa_j`.  Each coordinate contributes total weighted mass
`1+1/2+1/2=2`, so `sum_s kappa_j(s)=2^4=16`.

At zero,

```text
Z_(j+1)=kappa_j(0)K_j(0)
        +sum_(s!=0) kappa_j(s)K_j(-s).            (1)
```

Besides the zero pattern, a contribution to `kappa_j(0)` is a nonzero
signed relation of weight at most four among four consecutive powers of
`omega`.  Dividing by `omega^(4j)` gives a terminal `L=1` relation of the
same weight.  The wired Newton and official ambient exclusions rule out
weights one through four, so `kappa_j(0)=1`.  Equation `(1)` is therefore
`Z_(j+1)=Z_j+A_j`, proving `(BO-2)`.

The Haar baseline satisfies

```text
B_(j+1)=16B_j=B_j+15*2^(4j)/q.
```

Subtracting this from `(BO-2)` proves `(BO-3)`.  Finally `Z_0=1` and
`B_0=1/q`, so summing `(BO-3)` over `j=0,...,63` proves `(BO-4)`.
The inequality `Z-2^256/q<=4` is equivalent to `(BO-5)` after subtracting
`1-1/q`. QED.

The telescoping formula in this node is asserted on the official admissible
stratum where the wired exclusions prove `kappa_j(0)=1`; no unconditional
claim is made before that hypothesis.
