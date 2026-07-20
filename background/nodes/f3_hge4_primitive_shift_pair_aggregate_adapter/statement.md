# HGE4 primitive shift-pair aggregate adapter

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `x81_minimal_trade_square_shift`,
  `x82_square_shift_certifier_keys`,
  `x83_uniform_square_shift_obstruction_gate`, `f3_shiftpair_weld`,
  `v13_prefix_collision_ledger`, and
  `v13_second_moment_shift_pair_identity`

Fix an official row with domain `H=mu_n`, where

```text
n=2^s,        13<=s<=41,
p>=n^2,       p==1 mod n.
```

For `h>=4`, let

```text
F_h(z)=#{P subset H: |P|=h,
                   (e_1(P),...,e_(h-1)(P))=z},
C_h=sum_z F_h(z)(F_h(z)-1).
```

Let `SP_h^prim` be the ordered top shift-pair count obtained from `C_h` after
deleting the quotient-pullback/full-fiber class charged to the quotient
column. Then

```text
C_h=sp_(h-1)(h;H),
N_h^strip<=SP_h^prim<=C_h.                         (PSA1)
```

Here `N_h^strip` is exactly the direct-column record count in
`f3_hge4_norm_gate_count`. The first inequality uses the existing convention
that an unordered surviving trade creates at most two direct-column records;
the ordered shift-pair count contains its two orientations.

Put

```text
B_h=binom(n,h)(binom(n,h)-1)/p^(h-1).              (PSA2)
```

The following finite-track primitive shift-pair estimate is sufficient for
the HGE4 norm-gate target:

```text
SP_h^prim<=7000n max(1,B_h)                        (PSA3)
```

for every `4<=h<=H_max`. More precisely, `(PSA3)` implies

```text
sum_(h=4)^H_max N_h^strip <14n^3.                  (PSA4)
```

Thus `(PSA3)` is an explicit upstream-facing tolerance for primitive
shift-pair control. This node proves the reduction and summation compiler,
not `(PSA3)` itself, and it creates no new conditional DAG premise.

