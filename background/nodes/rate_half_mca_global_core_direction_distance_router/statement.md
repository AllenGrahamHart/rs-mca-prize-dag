# Global-core direction-distance MCA gate

- **status:** PROVED
- **closure:** field-general Johnson-ray gate and exact deployed arithmetic
- **scope repair:** no affine-span payment is included

After whole-line global-core cancellation, write the shortened row as

```text
(N,K,m)=(R+s,s,d+s),       t=R-d.
```

Let `y_1` be the shortened received-line direction syndrome and put

```text
d_U(y_1)=min{wt(e):He=y_1},       j=R-d_U(y_1).
```

Then `y_1!=0`, `j>=0`, and the selected slope family is paid whenever

```text
D_s(j)=d^2-(R-2d)s-(R+s)j > 0
```

and

```text
floor((R+s)(d-j)/D_s(j)) <= B*.
```

At fixed `s`, the exact paid prefix is `0<=j<=J_B(s)`, with `J_B(s)`
defined by the strict integer formula in `source_contract.json`.

## Official gates

```text
KoalaBear:    s=1..4982; J_B(1)=4340, J_B(4982)=0.
Mersenne-31:  s=1..4979; J_B(1)=4337, J_B(4979)=0.
```

The largest paid bounds are respectively `168818566` and `16131678`, far
below their official budgets.  The complete thirteen Mersenne budget spikes
are pinned in the contract.

No assertion is made for a defect above `J_B(s)` or a dimension after the
printed terminal.  In particular, the former claim that every direction was
paid through `s=13`/`s=5` is retracted with the affine-span compiler.

## Falsifier

A shortened selected family satisfying the displayed gate but exceeding the
bound, or an incorrect exact official prefix.
