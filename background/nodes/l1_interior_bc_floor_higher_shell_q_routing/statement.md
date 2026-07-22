# L1 interior BC floor routes to higher-shell Q

- **status:** PROVED
- **role:** remove Paper D's unavoidable interior support-census floor from
  the L1 exact level where it is not complete
- **consumer:** `l1_mixed_petal_amplification`

## Statement

Fix `k<=m`, put `w=m-k`, and choose a strict-interior profile

```text
d_1>=w+2,       m'=k-1+d_1>=m+1.                    (FR1)
```

Let `U=P_z` be any degree-`m'` monic identity-prefix witness with its top
`d_1-1` nonleading coefficients fixed.  For every degree-`m'` split locator
`L_M'` in that prefix fiber,

```text
c_M'=U-L_M'                                      (FR2)
```

has degree below `k` and agrees with `U` on exactly the `m'` roots `M'`.
Consequently:

1. its `binom(m',m)` level-`m` support witnesses all fail the complete-
   agreement gcd guard;
2. it contributes zero to the exact level-`m` shell `Z_m(U)`;
3. it contributes once to `Z_m'(U)`; and
4. at level `m'`, the same degree `d_1` is the boundary profile

   ```text
   d_1=(m'-k)+1.                                    (FR3)
   ```

Thus every codeword used in Paper D v13.2's strict-interior base-field floor

```text
binom(m',m) ceil(binom(n,m')/|B|^(d_1-1))           (FR4)
```

is higher-shell boundary-Q mass, counted once at its complete agreement
level.  It is not an unavoidable lower floor for the L1 exact level-`m`
interior BC cell.

## Exact cancellation

For one such codeword, its support-moment contribution cancels from binomial
inversion at level `m`:

```text
sum_(t=m)^m' (-1)^(t-m) binom(t,m) binom(m',t)=0.   (FR5)
```

## Scope

The theorem removes the named support-floor contribution only.  Other
codewords may have complete agreement exactly `m`, and their guarded
strict-interior split-pencil count remains open.  No base-field independence,
row-sharp Q bound, owner coalescing, or finite reserve inequality is proved.
