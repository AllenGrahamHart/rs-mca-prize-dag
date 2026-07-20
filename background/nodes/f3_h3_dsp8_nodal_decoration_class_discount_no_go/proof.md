# Proof

The verifier constructs `H=<562>` directly. It checks

```text
562^256=1,       562^128=-1 mod 769,
```

so `H` has exact order 256. Each printed triple consists of three elements of
`H`, has product one and sum three, and the union of the triples and their
negatives has size twelve. The two product-one triples are therefore reduced,
signed-disjoint points on the singular unit-trace curve `sigma^3=27`.

The unit-product trace normal form gives the decorated target

```text
t=1+rs(r+s-sigma)=1-rs(sigma-r-s).
```

For the lexicographic `3 by 3` decoration matrix, direct field arithmetic
gives

```text
t = [[ 83,611,258],
     [ 50,411,539],
     [187,205,183]].
```

None is zero or one. Direct enumeration of ordered pairs in
`A=(1-H)\{0}` gives

```text
P = [[86,96,88],       R = [[84,84,79],
     [72,74,98],            [84,84,79],
     [80,78,74]],           [90,79,89]].
```

Hence every decoration satisfies `P>=25` and `R>0`. Finally, membership of
`1-t` in the exact square subgroup `H^2` has truth matrix

```text
[[1,0,1],
 [1,1,1],
 [0,1,1]],
```

whose sum is seven. The antipodal criterion is exactly `1-t in H^2`, so the
fixture proves the claim. The explicit check `769<256^2` limits the
counterexample to the stated decoration-only route. QED.
