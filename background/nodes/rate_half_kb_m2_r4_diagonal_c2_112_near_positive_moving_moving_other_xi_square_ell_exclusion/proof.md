# Proof

Use the normalization in `(KBMMOS-2)`. Exact reconstruction and removal of
the incidence square give the primitive cores

```text
c product (4,8,8)  380 a3c2f655933d7fa4
c sum     (4,12,9) 632 f9448c2c1e47ba1b
d product (6,6,6)  312 7e429596156cea96
d sum     (5,10,8) 576 ab75e229a25e9053.             (1)
```

Both `c` cores are reciprocal in `b`. Their exact trace digests are
`162035e9c06a96e0` and `a4fe8c32d48892ac`; the terminal-subresultant parent
has digest `4b4738172d468601`. Complete factor multiplicities bind every
factor to a standard forbidden equation except

```text
39a8eb9fc1019be9 (2,3),
4805246499888132 (4,4),
90db6ed8f237340f (2,1).                            (2)
```

The `d` product factors into cubic branches `66126ac940fcff2b` and
`c492f19d9e524690`; the `d` sum is imposed on both. Their branch parents
have digests `a1dc3a87772a71b9` and `0e840b145172f378`. Complete factor
multiplicities leave exactly the common `(3,3)` component
`0296f5575e6cc6eb` and the second-branch `(16,12)` component
`04be7ea167bd1525`.

The six pair projections, in the sorted `3x2` component router, have digests

```text
ff1037d63f8c13a0 219a64c00e4cb01b
b9fc77fc477d33ea 30db7d2c7e8bff84
5a73d058fdbb04d7 6209b4ab207d7275.                 (3)
```

Their characteristic-zero factor multiplicities and complete modular
factorizations are pinned in both checkers. Removing standard support and
irreducible degrees not dividing six leaves exactly

```text
d-594504303; d-538097078;
d^2-568598655d-374354523;
d^6-642577042d^5+588486998d^4+926294591d^3
   +679398950d^2-111286545d-26700929;
d+251370115; d-299352588;
d+579618345; d+996338454; d+583634928; d-583634934;
d^2+16458322d-979475259;
d^2+699968870d-224576527;
d^2+703795947d-753996681;
d^2+957200620d+246061440;
d^2-97750688d+1;
d-499377018; d-151267790;
d^3-414708410d^2+399639044d-799507796;
d^2+462837669d+643446795;
d^2+1033375787d-244556338;
d^2-748014748d+1;
d^6+52868123d^5+322738914d^4-848385901d^3
   +322738914d^2+52868123d+1.                      (4)
```

For each factor in `(4)`, adjoin all four equations `(1)` over
`F_2130706433` and saturate by

```text
bcd; b,c,d in {2,1/2,1,-1};
(b-c)(bc-1)(b-d)(bd-1)(c-d)(cd-1);
5cd-4c-4d+5; 4c^2d-2c^2-3cd+3c+2d-4.             (5)
```

Every saturated basis is `[1]`. Since an irreducible polynomial over
`F_p` has a root in `F_(p^6)` only when its degree divides six, `(3)`--`(5)`
exhaust every deployed-field point.

The primary uses direct inversion and resultants. The no-import audit proves
the source identities with `DomainMatrix.solve_den`, reverse-lifts the
reciprocal `c` traces, and uses terminal subresultants for both cubic parents
and all six pair projections. Both validate the sparse checkpoints and all
22 saturations. Therefore the swapped square chart is empty. QED.
