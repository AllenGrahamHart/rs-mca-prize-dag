# Proof

Put `q_0=257=4m+1`, `m=64`, and let `g=3`, a primitive element of
`F_257`. Let `H=<g^4>` be the subgroup of order `m`, and let

```text
A_i=g^i H,       0<=i<4.
```

These four sets partition `F_257^*`.

## 1. The quartic difference family

For every nonzero additive difference `delta`, the total number of ordered
pairs `(u,v)` lying in a common `A_i` and satisfying `u-v=delta` is exactly
`m-1`.

Indeed, such a pair has `h=u/v in H\{1}`. Conversely, each
`h in H\{1}` gives the unique pair

```text
v=delta/(h-1),       u=hv.
```

The two entries lie in the same multiplicative coset. This is a bijection,
so there are `|H|-1=m-1` pairs.

## 2. The saturated block system

Take

```text
D={0,1,2,3} x F_257^*.
```

For `gamma in F_257`, first put

```text
B_gamma={(i,gamma+u):u in A_i, gamma+u!=0}.
```

Finally delete `(0,1)` from `B_0`, and write the resulting blocks as
`S_gamma`.

If `gamma!=0`, exactly one of the four cosets contains `-gamma`, so
`B_gamma` has `4m-1` points. The undeleted `B_0` has `4m` points and the
single deletion gives the same size. Thus every block has size
`rho=4m-1`.

Every point `(i,x)` with `x!=0` belongs before the final deletion to the
`m` blocks indexed by `gamma=x-u`, `u in A_i`. Hence every point has degree
`m`, except `(0,1)`, whose degree is `m-1`. Therefore

```text
sum_x(m-d_x)=1.
```

For two distinct block indices, their intersection before removing zero
coordinates is counted by same-coset representations of their nonzero
difference. Section 1 gives `m-1`; omitting zero coordinates and the final
point can only reduce it. Hence

```text
|S_gamma intersect S_gamma'|<=m-1,
|S_gamma union S_gamma'|>=2(4m-1)-(m-1)=7m-1=a.
```

This proves all block and saturation identities analytically.

## 3. The distinguished set

The result artifact stores `W` as a 1024-bit little-endian mask with SHA-256

```text
72155c521c66909f8bd117d0a557a67e8f33920f5d88c4d84e03d72e87db944f.
```

The primary verifier reconstructs the quartic cosets and blocks from the
generator. The independent verifier instead tests coset membership through
the quartic-power criterion. Both decode the mask and obtain

```text
|W|=447,
min_gamma |S_gamma\W|=66=m+2,
max_gamma |S_gamma intersect W|=189=3m-3,
min_(gamma!=gamma') |S_gamma union S_gamma'|=447=a.
```

The unique maximizer is `gamma=0`. Since `189-2m=61=m-3`, the exact
`2m` max-intersection conclusion fails while every registered incidence
premise holds. QED.
