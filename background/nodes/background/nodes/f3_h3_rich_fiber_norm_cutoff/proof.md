# Proof

Put `m=n/2`, let `zeta` be a primitive `n`th root of unity, and index the
standard basis of `Z^m` by `Z/mZ`. For an exponent `e mod n`, write

```text
e=bar(e)+m h(e),       0<=bar(e)<m,       h(e) in {0,1},
epsilon(e)=(-1)^h(e).
```

For every odd `r`,

```text
zeta^(re)=epsilon(e) zeta^(r bar(e)).             (1)
```

An unordered root pair `E={i,j}`, with `i,j!=0 mod n`, has shifted product

```text
beta_E=(1-zeta^i)(1-zeta^j)=1+q_E,
q_E=zeta^(i+j)-zeta^i-zeta^j.
```

Represent its nonconstant part by the integer vector

```text
v_E=epsilon(i+j)e_bar(i+j)
    -epsilon(i)e_bar(i)-epsilon(j)e_bar(j).        (2)
```

## Odd-conjugate Parseval identity

The Galois conjugates of `Q(zeta)` are indexed by the `m` odd residues `r`
modulo `n`. The characters `r -> zeta^(ra)`, `0<=a<m`, are orthogonal on
those residues: their cross-sum is the power-of-two Ramanujan sum and vanishes
for distinct `a` in this range. Hence, for two unordered pairs `E,F`,

```text
(1/m) sum_(r odd) |sigma_r(beta_E-beta_F)|^2
  = ||v_E-v_F||_2^2.                              (3)
```

The constant terms in the two shifted products cancel, which is why `(3)`
uses `v_E-v_F`.

## Ten-pair packing lemma

Each vector `(2)` is a sum of three signed standard basis vectors. Therefore

```text
||v_E||^2<=9.                                     (4)
```

If its squared norm exceeds `3`, two of the three terms must combine with the
same sign. The two negative terms combine only when `i=j`. The positive term
and the `i` term combine only when `j=m`, since this equality says
`zeta^(i+j)=-zeta^i`; symmetrically the final possibility is `i=m`. Thus

```text
||v_E||^2>3  =>  i=j or i=m or j=m.               (5)
```

All three terms combine with the same sign only for `i=j=m`, so this is the
unique norm-`9` vector. Every other vector covered by `(5)` has squared norm
at most `5`.

Now take ten distinct unordered representations of one nonzero finite-field
product `t`. At most two are diagonal, because `a^2=t` has at most two roots.
At most one contains the root `-1`: its shifted factor is `2`, so its other
factor is forced to be `t/2`. By `(5)`, at least seven of the ten lifted
vectors therefore satisfy

```text
||v_r||^2<=3.                                      (6)
```

Every squared distance `||v_r-v_s||^2` is even. Indeed, the coordinate sum
of each `v_r` is odd modulo two, so the coordinate sum of a difference is
even, and an integer square equals its base modulo two. Restrict to seven
vectors satisfying `(6)`. If all 21 distances were greater than `6`, each
would consequently be at least `8`. But the centroid identity gives

```text
168 <= sum_(r<s)||v_r-v_s||^2
     = 7 sum_r ||v_r||^2-||sum_r v_r||^2
     <=7*21=147,
```

a contradiction. Thus two of the ten pairs, say `E,F`, satisfy

```text
||v_E-v_F||^2<=6.                                 (7)
```

## Norm transfer

If `P(t)>=19`, the swap involution gives at least
`ceil(P(t)/2)>=10` distinct unordered representations, so the packing lemma
applies. The proved dyadic shifted-product Sidon theorem says

```text
alpha=beta_E-beta_F
```

is a nonzero cyclotomic integer. Under the reduction `zeta -> g` matching a
primitive generator of `H`, both products reduce to `t`; hence `alpha` lies
in a prime above `p` and `p` divides its rational norm.

Apply geometric mean at most arithmetic mean to the squared conjugate
absolute values in `(3)`, then use `(7)`:

```text
|Norm(alpha)|^(2/m)
  <= (1/m) sum_(r odd)|sigma_r(alpha)|^2
  <=6.
```

Since `m=n/2`,

```text
p<=|Norm(alpha)|<=6^(m/2)=6^(n/4).
```

This proves `(RFNC)`. If `p>6^(n/4)`, no `P(t)>=19` exists, so every term in
`X_18` vanishes.
