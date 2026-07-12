# Proof

Let `H` be the cyclic evaluation group of order `n=2^s`, and let

```text
K=Stab_H(S)={h in H:hS=S},       c=|K|.
```

The stabilizer is a subgroup. Since `H` is cyclic, it is the unique subgroup
`H_c` of order `c`, and `c` is dyadic.

If `c=1`, the support is aperiodic by definition. If `c>=2`, invariance under
`H_c` says exactly that `S` is a union of `H_c`-orbits. These orbits are the
complete fibers of the scale-`c` quotient map. Because an agreement support in
the top band is nonempty, it contains at least one complete fiber. Taking all
of `S` as the full-fiber part and the tail to be empty makes it a strict
staircase at scale `c`: the tail has size `0<c`.

The cases `c=1` and `c>=2` are disjoint and exhaustive. This proves the
closure-form G2 statement.

The proof does not assert staircase structure at a prescribed larger scale.
The fixed-scale mutation is false: the banked `n=32` witness has `c(S)=2`, is
staircase at scale `2`, and is not staircase at scale `4` or `8`.
