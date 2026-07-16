# Proof - PMA sigma-one generic defect-four source obstruction

Work over `F_q` with `q=65537^2`. Its multiplicative group contains the
cyclic subgroup `H` of order `n=65536`. Put `k=n/2`, `K=k-1`, `L=n-k`, and
`M=L/2`.

Choose a core `C` with `k/2` points in one coset of the index-two subgroup and
`k/2-1` points in the other. Require that `C` contain one pair `{x,-x}`.
Choose a background point outside `C` and pair the remaining `L` points
arbitrarily. Set the base polynomial to `Q=1`.

For an injective label tuple `(c_i)` in `F_q^*`, define the source word by

```text
U=1                       on C and the background,
U(y)=1+c_i L_C(y)         on petal T_i.
```

The `M` polynomials `1+c_iL_C` are distinct planted anchors, so this is a
maximal `sigma=1` source layout.

Fix `D subset C`, `|D|=4`, and a polynomial `W` of degree at most four. Put

```text
P=1+L_(C\D) W,             R=W/L_D.
```

Require `W` to be nonzero on `D`, the background, and every petal point, and
require the `L` values `R(y)` on the petal points to be pairwise distinct.
Then `P` has exact core defect `D`, no background agreement, and on `T_i`
agrees with `U` exactly where `R(y)=c_i`.

There are at least

```text
q^4(q-H_0),
H_0=binom(L,2)+L+5,                                      (G1)
```

admissible `W` for each `D`. Indeed, every forbidden zero is one nonzero
linear hyperplane in the five coefficients of `W`. For distinct petal points
`y,z`, the collision equation

```text
W(y)L_D(z)-W(z)L_D(y)=0
```

is also a nonzero linear hyperplane: if its two evaluation functionals were
proportional for every degree-four `W`, testing `W=1` and `W=X` would force
`y=z`. There are `L+5` zero hyperplanes and `binom(L,2)` collision
hyperplanes. The union bound proves `(G1)`.

Now choose the `M` labels uniformly among injections into `F_q^*`; put
`Q_0=q-1`. For one admissible `(D,W)`, choose six petals and one of their two
points. The probability that the six selected labels equal the six prescribed
distinct values is `1/(Q_0)_6`. Conditional on this event, each remaining
petal label is marginally uniform on the `Q_0-6` unused values and has two
forbidden values. The union bound therefore gives conditional probability at
least

```text
1-2(M-6)/(Q_0-6)                                         (G2)
```

that no other petal point agrees. The exact-six events for distinct choices
of six petals and sides are disjoint. Hence the expected number `N(U)` of
the constructed exact-six codewords satisfies

```text
E N(U) >= binom(K,4) q^4(q-H_0)
          * 2^6 binom(M,6)/(Q_0)_6
          * (1-2(M-6)/(Q_0-6)).                         (G3)
```

The exact integer comparison in the verifier proves that the right side of
`(G3)` is strictly greater than `n^6`. Therefore one injective label tuple
has `N(U)>n^6`.

Different pairs `(D,W)` give different codewords: the exact core miss set of
`P` recovers `D`, and then `W=(P-1)/L_(C\D)`. Each constructed codeword has

```text
(k-1-4)+6=k+1
```

total agreements. It is non-planted and diffuse because all rational values
on petal points were required distinct.

It remains to check the global owners. A nontrivial stabilizer in the cyclic
two-group has even orbit size, whereas the exact agreement set has odd size
`k+1`; exact periodicity is impossible. For a dyadic coset to miss at most
`s_n` agreement points, its size must lie between `k-s_n` and `k+1+s_n`.
The only dyadic size in that interval is `k`. The balanced core and six added
petal points meet either `k`-coset in at most `k/2+6`, leaving more than
`s_n` misses. Finally, if `U(y)=(y-a)V(y^2)`, then at the chosen core pair
`{x,-x}` where `U=1`,

```text
1=(x-a)V(x^2)=(-x-a)V(x^2),
```

which forces `2xV(x^2)=0` and then `1=0`, a contradiction. Thus the odd-lift
owner is also unavailable.

All `N(U)` codewords remain in the source-level `Top disjoint_union Post`
partition. If the finite PMA assertion held, the proved Top bound and Post
allowance would give total size at most

```text
N_top+B_post=n^6,
```

contradicting `N(U)>n^6`. This proves the obstruction.
