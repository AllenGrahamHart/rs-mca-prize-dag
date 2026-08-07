# Proof: LS6 canonical-owner packing

## 1. The owner is exact

Let `P` be an irreducible factor of the squarefree locator `D_0`. Reducing
the determinant identity modulo `P` gives

```text
H == -D_HQ_0 mod P.
```

The base is primitive, so `Q_0` is a unit modulo every such `P`. Therefore
`P|H` if and only if `P|D_H`. Since `D_0` is squarefree, this proves
`gcd(D_0,H)=gcd(D_0,D_H)` with monic normalization. The non-base coordinate
`H` is nonzero and has degree at most `h<j`, so `0<=g<=h`.

Both locators are squarefree and their exact gcd is `G`. It follows that
`G,A,B` are pairwise coprime and that `A,B` have degree `j-g`. Dividing the
determinant identity by `G` gives

```text
K=AQ_H-BQ_0,       deg K<=h-g.                       (1)
```

Modulo `A`, equation `(1)` reads `K=-BQ_0`. Both factors on the right are
units modulo `A`, so `gcd(K,A)=1`. Modulo `B`, it reads `K=AQ_H`; because
`A` is a unit modulo `B`,

```text
gcd(K,B)=1 iff gcd(Q_H,B)=1.                          (2)
```

Finally `D_H=GB`, with `gcd(G,B)=1`, so

```text
gcd(D_H,Q_H)=1
 iff gcd(G,Q_H)=gcd(B,Q_H)=1.
```

Combining this equivalence with `(2)` proves the exact guard `(CO5)`.

## 2. Fixed-owner packing

For a candidate with exact owner `G`, all roots of `B` lie in
`C\Z(D_0)` and there are `w=j-g` of them. Take two distinct candidates
`D_i=GB_i`. The primitive pair-determinant theorem supplies a nonzero
polynomial

```text
P_12=D_1Q_2-D_2Q_1
    =G(B_1Q_2-B_2Q_1),       deg P_12<=h.             (3)
```

Every common factor of `B_1` and `B_2` divides `P_12/G`. Thus the two
candidate-only root sets meet in at most `h-g=t-1` points.

Each `B` contains `binom(w,t)` subsets of size `t`, while no such subset can
belong to two different members. The ambient set `C\Z(D_0)` has size
`v=|C|-j`, hence contains `binom(v,t)` such subsets. Double counting proves
`(CO7)`.

## 3. Top-owner specialization

For `|C|=4ell+b-2` and `g=h-c`, direct substitution gives

```text
v=2ell+a+b-2,       w=ell+a+c,       t=c+1.
```

Since `b<ell`, one has `v<3(ell+a)`. Therefore every factor in the binomial
ratio obeys

```text
(v-i)/(w-i) <= v/(w-c)=v/(ell+a)<3       (0<=i<=c).
```

Multiplying the `c+1` factors proves `(CO8)`. QED.
