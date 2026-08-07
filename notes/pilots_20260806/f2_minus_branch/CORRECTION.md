# F2 minus-branch correction

This packet supersedes the all-admissible wording in the Round-17
`f2_adm` packet. The order identity used there omitted the
`p=3 mod 4` branch. The explicit official row

```text
p=2^61-1, q=p^2
```

has `ord_(2^41)(p)=2` but `2^40` singleton proportionality classes after
the antipodal quotient. The old bounded-class theorem is retained only for
`p=1 mod 4`; its Newton-distance and weighted-L2 descendants receive the
same scope restriction. The F2 prize target remains open rather than
refuted.

Canonical Round 18 at `prize@feadaa03` repeats the omitted-branch step in
its claim that admissibility forces `v_2(p-1)>=39` and that exactly three
generating classes survive. Its field-generic `Z-FLOOR` theorem is valid and
has been imported separately. The minus branch is repaired by the coupled
negacyclic reduction, not by retaining the bounded-class census.

The Round-18 route-(b) display also uses `1+2cos`, the unweighted ternary
enumerator. The weighted prize mass uses `1+cos=2cos^2`; the exact corrected
formula is banked in `f2_weighted_kernel_collision_floor`.
