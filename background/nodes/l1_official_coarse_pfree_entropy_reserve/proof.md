# Proof - L1 official coarse p-free entropy reserve

## 1. Exact ambient averages

There are `binom(n,k+d)` root sets of size `k+d`. The mixed coordinate map
has `d` field-valued coordinates. Forgetting the `r=floor(d/p)` elementary
checkpoints leaves `d-r` p-free coordinates. Averaging over the complete
ambient target spaces `F^d` and `F^(d-r)` gives `(CER2)` exactly; no
surjectivity assertion is needed.

## 2. The first checkpoint is 3,175 layers beyond the reserve

Since `d_0=ell_0-1` and `ell_0<=p-3174`, a checkpoint depth `d>=p`
satisfies

```text
Delta=d-d_0>=p-(ell_0-1)>=3175.                       (1)
```

The Frobenius-checkpoint router gives `r<=23`.

## 3. Binomial growth loses to the added codimension

For `Delta=d-d_0`, consecutive binomial ratios give

```text
binom(n,k+d)/binom(n,k+d_0)
 =product_(t=d_0)^(d-1) (n-k-t)/(k+t+1).
```

Because the smallest official rate is `1/16`, every factor is strictly less
than

```text
(n-k)/k<=15.                                          (2)
```

Also `n|q-1` implies `q>n>=2^13`. Therefore

```text
mu_free(d)/mu_mix(d_0)
 <15^Delta/q^(Delta-r)
 <2^(4 Delta-13(Delta-r))
 =2^(-9 Delta+13r)
 <=2^(-9*3175+13*23)
 =2^(-28276).
```

This proves `(CER3)`.

## 4. Canonical reserve and the finite target

The canonical reserve states

```text
q^d_0>=binom(n,k+d_0)^(1+eta),       eta>0.
```

Thus `mu_mix(d_0)<=binom(n,k+d_0)^(-eta)<=1`, proving `(CER4)`.
If `(CER6)` holds, then

```text
max_s |Fib_free(d,s)|
 =K_d mu_free(d)
 <q 2^28148 2^(-28276)
 =q/2^128.
```

The mixed-to-coarse inclusion from the Frobenius-checkpoint router transfers
the same bound to every exact mixed prefix fiber. This proves the claimed
sufficient condition, without asserting it.

## 5. Fifteen bits per p-free condition are affordable

Suppose a checkpoint depth exists. Then `p<=d<=n-k`. Every official rate has
`k>=n/16>=512`, so `p+1<n`. The order bound

```text
f>=n/(p+1)
```

and integrality of `f` imply `f>=2`. Since `p>=3583>2^11`, this gives
`log_2 q=f log_2 p>22`.

The canonical reserve estimate used by the Newton-window router also gives

```text
d_0=ell_0-1<=ceil(5(p+1)/(4 log_2 p))
              <=ceil(5(p+1)/44)
              <=5(p+1)/44+1.                         (3)
```

Return to the proof of `(CER3)`, now using `log_2 q>22`. If the owner-pruned
extras count satisfies `(CER8)`, then

```text
log_2(max_s Exc_d(s)/mu_mix(d_0))
 <-18 Delta+22r+15(d-r)
 =-3 Delta+7r+15d_0
 =-3d+18d_0+7r.
```

Because `d>=rp` and `-3p+7<0`, the right side is at most

```text
r(-3p+7)+18d_0
 <=-3p+7+18d_0
 <=-3p+7+18(5(p+1)/44+1)
 =-(21p-595)/22
 <=-(21*3583-595)/22
 <-3393.                                              (4)
```

Together with `mu_mix(d_0)<=1`, equation `(4)` proves `(CER9)`. Since every
`Exc_d(s)` is a nonnegative integer, all extras vanish. In particular they
are below the finite threshold. The separate structured fibers are not part
of this inequality and retain their declared owners.

The bit 15 is meaningful at this level of information. At the extremal coarse
parameters `p=3583`, `d_0=ceil(5(p+1)/44)=408`, `d=p`, and `r=1`, replacing
15 by 16 makes the exponent estimate

```text
-18(d-d_0)+22r+16(d-r)=184,
```

so the same official inequalities no longer certify extras emptiness or the
finite target. This is a route-boundary statement, not a counterexample to a
16-bit theorem on the actual generated rows.
