### 2026-08-10 general-t FPC5 fixed joint-owner payment

The new PROVED node `l1_fpc5_tpetal_joint_owner_packing` supplies the first
counting theorem after the arbitrary-`t` coordinate reductions. At one fixed
joint owner `Q` of degree `q`,

```text
|F_Q| <= binom(N+b-q,r-q+1)
         / binom(d+max(0,u)-q,r-q+1).
```

This pays every bounded co-deficiency chamber `q=r-O(1)` polynomially per
owner and gives a sharp one-subset ratio at `q=r`.

No critical status changes. The theorem does not permit summing over all
divisors `Q`; chronology-valid coalescence of realized owners is now the
precise aggregate obstruction.
