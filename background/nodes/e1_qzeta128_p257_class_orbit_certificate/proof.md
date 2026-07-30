# Proof

Put

```text
K=Q(zeta_128),        K+=Q(zeta_128+zeta_128^(-1)),
G=Gal(K/Q)=(Z/128Z)^x.
```

Write `sigma_a(zeta_128)=zeta_128^a` and let `c=sigma_127` be complex
conjugation.

## 1. Class conjugation is inversion

The proved conductor-256 real-class theorem gives

```text
h(Q(zeta_256)^+)=1.                                  (1)
```

Let `F=Q(zeta_128)^+` and `E=Q(zeta_256)^+`. If an ideal class `y` of `F`
is extended to `E`, it becomes principal by `(1)`. Norming back through the
quadratic extension `E/F` gives `y^2=1`. Weber's theorem says that class
numbers of 2-power cyclotomic fields, and their plus factors, are odd.
Therefore `y=1`, proving

```text
h(K+)=1.                                              (2)
```

For every fractional ideal `I` of `K`,

```text
I c(I)=N_(K/K+)(I) O_K.
```

The ideal on the right is principal by `(2)`. Hence complex conjugation acts
on `Cl(K)` by inversion:

```text
c([I])=[I]^(-1).                                     (3)
```

Weber's theorem also says that `h(K)` is odd. Thus `Cl(K)` has no nontrivial
element of order two.

## 2. Two products exclude all involutions

The residue `9` has order 128 modulo 257. The 64 primes above 257 are

```text
q_a=(257,zeta_128-9^a),       a in G.
```

For the involutions used below, `sigma_a(q_1)=q_a`. Let `x=[q_1]` and let

```text
H={a in G:sigma_a(x)=x}
```

be its stabilizer.

The three nonidentity involutions of `G` are

```text
63=-65,       65,       127=-1        (mod 128).     (4)
```

Since `sigma_63=c sigma_65`, equation `(3)` gives

```text
65 in H  iff  [q_1 q_63]=1.                          (5)
```

Indeed, if `sigma_65(x)=x`, then
`sigma_63(x)=c(x)=x^(-1)`. Conversely, if
`x sigma_63(x)=1`, then applying `c` to
`sigma_63(x)=c(x)` gives `sigma_65(x)=x`. The same argument with 63 and 65
interchanged gives

```text
63 in H  iff  [q_1 q_65]=1.                          (6)
```

The proved two-involution node says both products in `(5)--(6)` are
nonprincipal, so
neither 63 nor 65 lies in `H`. It also implies `x` is nontrivial. If 127 lay
in `H`, then `(3)` would give `x=x^(-1)`, hence `x^2=1`; oddness of `h(K)`
would force `x=1`, a contradiction. Thus none of the three involutions in
`(4)` belongs to `H`.

Every nontrivial subgroup of the finite 2-group `G` contains an element of
order two. Therefore `H` is trivial. The orbit of `x` consequently has
`|G|=64` elements. Since `G` acts transitively on the 64 primes above 257,
their ideal classes are pairwise distinct. QED.
