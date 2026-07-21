# HGE4 cyclotomic-norm quarter-width exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_exact_ratio_tower_orbit_compiler`,
  `f3_hge4_near_third_belyi_necklace_bound`

Let `m=2^r>=16`, let `p` be prime with

```text
p=1 mod m,       p>=m^2,
```

and let `E_h^prim(m,p)` have the exact-level meaning from the tower compiler.
Then

```text
E_h^prim(m,p)=0       whenever m/4<=h<m/3.          (CNQ1)
```

In particular, after the proved non-full complement-third gate, the complete
exact-level target reduces from

```text
4<=h<=floor((m-1)/3)
```

to

```text
4<=h<=m/4-1.                                      (CNQ2)
```

The exclusion includes the equality width `h=m/4` and the whole retained
Kummer near-third strip `m/4<h<m/3`. Therefore no trace-to-pencil fiber bound
is needed in that strip, even when the scalar trace-power gcd is nonconstant.

The theorem does not estimate any width in the lower-quarter range below
`m/4`, prove the remaining exact-level aggregate, or close HGE4.
