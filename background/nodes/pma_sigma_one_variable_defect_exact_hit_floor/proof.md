# Proof - PMA sigma-one variable-defect exact-hit floor

Use a core `C` with `k/2` points in one index-two coset and `k/2-1` in the
other, containing a pair `{x,-x}`. Pair all but one of the `L+1` points
outside `C`, use the remaining point as background, and choose distinct
nonzero labels `c_1,...,c_M`. The source is

```text
U=1                         on C and the background,
U(y)=1+c_i L_C(y)           on petal T_i.
```

Fix `D subset C`, `|D|=d`, and `deg W<=d`. Define

```text
P=1+L_(C\D)W,       R=W/L_D.
```

Require `W` to be nonzero on `D`, the background, and all petal points, and
require all `L` values `R(y)` on petal points to be distinct. There are

```text
q^d(q-H_d),
H_d=binom(L,2)+L+d+1,
```

such numerators. The zero conditions contribute `L+d+1` nonzero linear
hyperplanes in the `d+1` coefficients of `W`. Each collision condition

```text
W(y)L_D(z)-W(z)L_D(y)=0
```

is another nonzero linear hyperplane: tests with `W=1` and `W=X` would
otherwise force `y=z`. The union bound gives the count.

Choose the source labels uniformly among injections into `F_q^*`. For one
good `(D,W)`, choose `a=d+2` petals and one side in each. The probability that
the selected labels equal the prescribed distinct rational values is
`1/(q-1)_a`. Conditional on this event, every remaining petal label is
uniform on the `q-1-a` unused values and has exactly two forbidden values.
The union bound gives probability at least

```text
1-2(M-a)/(q-1-a)
```

of no additional petal hit. Distinct selections give disjoint exact-hit
events. Averaging over labels and then over all `binom(K,d)` defects proves
the displayed lower bound.

The exact core miss set recovers `D`, and then
`W=(P-1)/L_(C\D)`, so distinct `(D,W)` give distinct codewords. Their exact
agreement count is

```text
(K-d)+a=k+1.
```

This odd support size excludes every nontrivial stabilizer in the cyclic
two-group. Each index-two coset contains at most `k/2+a` agreement points, so
the stated bound on `d` leaves more than `s_n` misses from either eligible
`k`-coset. The usual pair argument excludes an odd-lift source: if
`U(y)=(y-b)V(y^2)`, then `U(x)=U(-x)=1` forces both
`(x-b)V(x^2)=1` and `(-x-b)V(x^2)=1`, a contradiction. Every petal hit is a
singleton, so these codewords are outside the full-petal Top class.

For the asymptotic corollary, apply Linnik's theorem to the reduced residue
class `-1 mod n`. It gives absolute constants `C_0,L_0` and a prime

```text
p=-1 mod n,       p<=C_0 n^L_0.
```

After increasing the threshold, absorb `C_0` into a fixed power `n^A`. Put
`q=p^2`. Since `n|(p+1)`, `F_q^*` contains an order-`n` subgroup. Its
intersection with `F_p^*` has order at most two, so for `n>2` the subgroup is
not contained in `F_p` and generates the quadratic field. Also
`q>(n-1)^2>2H_d` for `d=n/8` and large `n`.

For `d=n/8`, `a=d+2`, and large `n`, elementary product bounds give

```text
binom(K,d) >= 3^d,
2^a binom(M,a) >= 3^a.
```

Moreover `(q-1)_a<=q^a`, `q-H_d>=q/2`, and the final conditional factor is
at least `1/2`. Therefore

```text
E N_d(U) >= 3^(d+a)/(4q) >= 3^(n/4)/(4q).
```

Because `q<=n^(2A)`, this exceeds every fixed power of `n` along the family.

## Imported theorem

The only external input is Linnik's least-prime theorem. A primary modern
source with an explicit absolute exponent is T. Xylouris, *On Linnik's
constant*, arXiv:0906.2749, https://arxiv.org/abs/0906.2749. The proof above
needs only the existence of some absolute exponent.
