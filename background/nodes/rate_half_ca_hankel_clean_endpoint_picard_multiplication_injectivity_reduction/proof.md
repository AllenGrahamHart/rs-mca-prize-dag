# Proof

Tensor the ideal sequence of the bidegree-`(rho,m)` curve by `O(N,-T)`:

```text
0 -> O(N-rho,-T-m) --Q--> O(N,-T)
  -> O_C(N,-T) -> 0.                                 (1)
```

Both ambient line bundles have negative parameter degree, so their zeroth
cohomology groups vanish. The long exact sequence identifies

```text
H^0(C,O_C(N,-T))=ker mu_Q.                           (2)
```

The Picard theorem identifies the left side with
`H^0(C,O_C(P_*))`, which contains the canonical point section. This proves
`(PMI3)`.

For `a>=0` and `c>=2`, Kunneth gives

```text
dim H^1(P^1xP^1,O(a,-c))=(a+1)(c-1).                (3)
```

Apply `(3)` first with

```text
a=N-rho=12m+1,       c=T+m=5m+1,
```

and then with `a=N=16m`, `c=T=4m+1`. This proves `(PMI4)`.

Let `pi` be projection to the domain `P^1`. Since the parameter degrees in
`(1)` are negative, relative cohomology turns `(PMI2)` into the map

```text
O(N-rho) tensor H^1(P^1,O(-T-m))
 -> O(N) tensor H^1(P^1,O(-T)),                     (4)
```

whose ranks are `T+m-1=5m` and `T-1=4m`. At a domain point `x`, the dual of
the fibre map is multiplication by the nonzero degree-`m` form `Q(-;x)`:

```text
H^0(P^1,O(T-2)) -> H^0(P^1,O(T+m-2)).               (5)
```

It is injective, so `(4)` is fibrewise surjective. The clean absolute
irreducibility excludes a parameter-independent `X` factor and guarantees
that `Q(-;x)` is nonzero at every projective domain point. Hence its kernel
is a vector bundle `K_Q` of rank `5m-4m=m`.

Degrees in the short exact sequence give

```text
deg K_Q=5m(N-rho)-4mN=m(5-4m).                      (6)
```

Taking global sections of the kernel sequence and using the relative
identification recovers `ker mu_Q=H^0(K_Q)`, so `(PMI3)` proves the final
assertion in `(PMI6)`.

Finally write the Birkhoff-Grothendieck splitting as

```text
K_Q=sum_i O(k_i).
```

Then `H^0(K_Q)=0` exactly when every `k_i<0`. This proves the equivalence and
the closing criterion `(PMI7)`. The four-Hankel frame is supplied by the
other required parent. QED.
