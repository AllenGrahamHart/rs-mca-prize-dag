### 2026-08-10 FPC5 M=4,t=2 typed frontier

The current upstream master-flatness and split-pencil programme does not
already close the rate-half FPC5 `M=4,t=2` leaf. It poses the correct generic
count, but its growing-dimensional max-to-mean statement remains
conjectural. Two additional exact structures of the local sharp endpoint are
now banked as separate PROVED background nodes.

First, every exact contributor has an injective rational-map encoding

```text
phi=L_1A_1/(L_2A_2),       deg phi=2ell-3.
```

Its complete reduced `1`-fiber is the core defect, the touched petals lie in
the zero and pole fibers, the full background lies in the distinct
`c_1/c_2` fiber, and each untouched petal avoids its own further marked
fiber. The six marks are pairwise distinct. At the sharp arithmetic the
core, background, and four petals partition the whole official domain. This
is a concrete determinantal-incidence/value-set interface stronger than the
untyped projective flat, but it supplies no map count.

Second, shortening the common agreement block formed by the background and
touched pair gives an injective LIST interface:

```text
RS[C,2ell-1],       |C|=5ell-5,
agreement=3ell-2,   radius=2ell-3=floor(2(N-K_0)/3).
```

The FPC5 cofactor and exact-owner conditions remain filters on this list.
The parameters lie outside the ordinary Johnson range, so this is not a
hidden standard list-decoding closure. It identifies precisely what a
source-core-specific or cofactor-aware list theorem would need to prove.

The live upstream PR #1125 determinant atlas transports exactly after this
shortening. Its balance parameters become `w=ell-1`, `omega=2ell-3`, and
`s=ell-2`. For one anchor it recovers every common-error owner
`D=gcd(F_0,F)` by one determinant gcd and pays each fixed owner by the two
explicit bounds in `(SH8)`; the maximal-intersection owner has size at most
two. This removes fixed-pencil and coefficient multiplicity from the sharp
frontier. The unpaid object is the aggregate number of realized gcd owners.

The critical node remains TARGET. A closure must still:

1. coalesce the sharp realized gcd owners using the marked rational-map or
   cofactor structure, without summing all divisors of one anchor;
2. handle every nonsharp `s` cell in the uniform root-rich split-pair locus;
3. retain the six touched-pair owners and avoid a sum over background sets;
4. compose through first-layout domination without reintroducing source
   layouts.

No Modal computation was used. The advance is structural and proof-level,
not numerical evidence.
