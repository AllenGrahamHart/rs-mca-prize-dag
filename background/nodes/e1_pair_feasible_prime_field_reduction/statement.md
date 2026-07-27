# E1 pair-feasible prime-field reduction

- **status:** PROVED
- **closure:** proof plus exact arithmetic

At each of the six named clean predecessor anchors, every pair-feasible E1 row
is a prime-field row:

```text
F=F_p,  q=p,  p=1 mod N,
```

where `N=256` at rates `1/4,1/8` and `N=512` at rate `1/16`.

By `e1_pair_feasible_ambient_generation`, the quotient roots generate `F`.
Thus, if `F=F_(p^d)`, then

```text
d=ord_N(p).
```

For a power-of-two `N`, every possible `d` is a power of two. Exact perfect-
power interval checks show that no `d>1` is compatible with either named
numerator-budget interval and the order equation. Therefore `d=1`.

This places the open collision target inside the prime-field scope of
`kernel_lattice_reframing`. It does not prove the collision allowance or
select the primes inside either interval.
