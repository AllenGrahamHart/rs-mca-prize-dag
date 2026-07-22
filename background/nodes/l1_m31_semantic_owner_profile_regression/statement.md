# M31 line-profile compiler and semantic owner regression

- **status:** PROVED
- **closure:** exact finite-field replay plus independent Lean build
- **consumer:** `l1_mixed_petal_amplification` (evidence and interface pin)
- **upstream:** `przchojecki/rs-mca` PR `#1047`, exact head
  `0e735999acf24a7779b2271553deb26207396cda`

For the auxiliary deployed Mersenne-31 list row, put

```text
p=2147483647,  n=2097152,  a+=1116023,
omega=n-a+=981129,  w=67447,  Abar=1993678.
```

Two line-local compilation statements hold.

1. A theorem-certified duplicate-free near-rational finite-slope list of
   length at most one is a paid profile with exact numerator `1`.
2. A theorem-certified duplicate-free primitive one-pencil slope list after
   common-GCD deletion has length at most
   `floor(n/omega)=2` and is a paid profile with exact numerator `2`.

Both profiles keep the slope denominator `p` separate from the natural
profile denominator `p^w`, and both exact numerators fit the calibrated
natural numerator

```text
1+Abar=1993679.                                      (MSO-1)
```

These are compilers for supplied theorem-certified slope lists. They do not
prove that the two branches classify all explanations, count all realized
pencils, or exhaust any deployed first-match residual.

Separately, on the order-twenty subgroup of `F_241`, there is one explicit
received line carrying eleven genuine degree-`<8` Reed-Solomon explanation
states on distinct slopes. Ten states are deficiency-six neighbors of an
anchor and share locator prefix `(92,135)`. Two of them, with slopes `115`
and `22`, have a certified common-GCD projective pencil whose only split
parameters with at least seven moving roots are `0` and infinity. Assigning
exactly those two states to the earlier owner leaves eight literal unowned
neighbors. The residual obeys

```text
241^2 (8-3) = 290405 <= 308700 = 7 binom(10,6)^2,   (MSO-2)
```

with margin `18295`.

Thus a chronology-valid semantic owner can repair the false support-only
`3+7` shell inequality in this exact fixture. No universal deployed M31
`3+7` theorem, exhaustive C1--C8 owner atlas, row-sharp Q payment, complete
list-interior ledger, adjacent safe row, or Prize result is asserted.
