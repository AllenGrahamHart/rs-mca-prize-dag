# Proof

The near-square union router proves that a nontrivial stabilizer of a
primitive union is `{1,-1}` and that `-1` exchanges its two reconstructed
supports. Write them as `P` and `Q=-P`, and put `A=L_P`, `B=L_Q`. Then

```text
B(X)=(-1)^h A(-X).                                  (1)
```

The top shift-pair condition says that `A-B` is a nonzero constant. Write

```text
A(X)=sum_(j=0)^h (-1)^j e_j(P)X^(h-j).
```

The coefficient of `X^(h-j)` in `B` is `e_j(P)`. Hence the corresponding
coefficient of `A-B` is

```text
((-1)^j-1)e_j(P).                                  (2)
```

For odd `j<h`, equation `(2)` vanishes exactly when `e_j(P)=0`; even `j`
vanish automatically. If `h` were even, the constant term would also vanish,
contradicting `A!=B`. Thus `h` is odd and `(SOM1)` holds. Since `e_h(P)` is
the nonzero product of the roots, the constant difference is nonzero.
Equations `(1)--(2)` also give

```text
A=S-e_h(P),       B=S+e_h(P),
```

where `S` contains only odd powers and has zero constant term.

Let `p_j(P)=sum_(x in P)x^j`. Newton's identities read

```text
k e_k=sum_(i=1)^k (-1)^(i-1)e_(k-i)p_i.            (3)
```

For odd `k<h`, assume inductively that the preceding odd elementary
symmetric functions and odd power sums vanish. In `(3)`, a term with odd
`i<k` contains a vanishing `p_i`, while a term with even `i` contains a
vanishing odd `e_(k-i)`. The only remaining term is `p_k`, so

```text
k e_k=p_k.                                         (4)
```

Official rows have `p>=n^2>h`, so `k` is invertible. Induction proves the
equivalence of `(SOM1)` and `(SOM2)`.

Conversely, take odd `h` and an antipodal-free `P` satisfying `(SOM1)`.
Equation `(2)` shows that `L_P` and `L_(-P)` agree in every nonconstant
coefficient and differ in their nonzero constants. They are therefore a top
shift pair. Antipodal-freeness makes the supports disjoint, and the stated
common-stabilizer hypothesis makes the ordered pair primitive. Its union is
fixed by `-1`, which exchanges the sides, so the near-square router places it
in the swap class.

Every swap union is a union of `h` antipodal pairs. If it is anchored at one,
it contains the pair `{1,-1}`, leaving at most
`binom(n/2-1,h-1)` candidate unions. The near-square orbit identity says each
swap union orbit contributes exactly `h` anchored unions, proving `(SOM3)`.

Finally choose one square root `r_i` from each selected antipodal pair. Every
partition `(P,-P)` is a sign vector `epsilon_i`, unique up to simultaneous
sign reversal. Substitution into `(SOM2)` gives `(SOM4)`. QED.
