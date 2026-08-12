# Global-core direction-distance MCA router

- **status:** PROVED
- **closure:** exact composition and deployed-row arithmetic
- **scope:** one non-global-affine whole-line global-core family

## Statement

Apply whole-line common-core cancellation to a selected support-wise MCA-bad
slope family.  Write its shortened row as

```text
(N,K,m)=(R+s,s,d+s),       t=N-m=R-d.
```

Let `H` be a parity check for the shortened code, let `y_1` be the syndrome
of the shortened received-line direction, and put

```text
d_U(y_1)=min{wt(e):He=y_1},       j=R-d_U(y_1).
```

Then `y_1!=0`, `j>=0`, and the entire selected slope family is paid whenever

```text
D_s(j)=d^2-(R-2d)s-(R+s)j > 0
```

and

```text
floor((R+s)(d-j)/D_s(j)) <= B*.
```

Equivalently, at fixed `s` it is paid for every integer `0<=j<=J_B(s)`,
where `J_B(s)` is the exact threshold printed in `source_contract.json`.

Together with the support-wise affine-span compiler, the official routers
are:

```text
KoalaBear:   all j paid for s<=13;
             0<=j<=J_B(s) paid for 14<=s<=4982.
Mersenne-31: all j paid for s<=5;
             0<=j<=J_B(s) paid for 6<=s<=4979.
```

On KoalaBear the budget never tightens denominator positivity: `J_B(s)` is
exactly the largest `j` with `D_s(j)>0`, and the largest resulting bound is
`168818566`.  On Mersenne-31 the largest paid bound is `16131678`; at exactly
thirteen dimensions the last positive-denominator defect is over budget and
the paid threshold is one smaller.  Those dimensions are pinned in the
contract.

## Residual

The only global-core branch left by this router is the explicit
`LOW_DIRECTION_DISTANCE_GLOBAL_CORE` cell:

```text
s>=4983, or j>J_B(s)       (KoalaBear),
s>=4980, or j>J_B(s)       (Mersenne-31).
```

## Nonclaims

This does not pay the low-direction cell, prove first-match coverage outside
the selected global family, close a deployed row, or close either prize.

## Falsifier

A shortened selected family satisfying the displayed paid gate but exceeding
the direction-distance bound, or any incorrect official integer threshold.
