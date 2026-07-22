# Proof

Take a maximum-agreement quotient slope `z`, with paid threshold
`B=k+t_z` and first-matched scale `c`. Since the scale is rate-preserving,
`c|k`. Since it is active at `B`, `0<t_z<c`. Hence

```text
floor(B/c)=k/c,       B-c floor(B/c)=t_z.
```

The maximum-agreement theorem says the quotient support is the witness
codeword's full agreement set. Its complete-fiber part consequently has
exactly `k/c` fibers and `k` points, proving `(QCR1)`. Also `t_z>=t_0`, so
every scale that can occur satisfies `c>t_0` and is present in the initial
active scale family.

Fix one scale. There are exactly

```text
C(n/c,k/c)
```

possible `k`-point complete-fiber cores. A key occurring once owns at most
one slope, so summing over the initial active scales proves the first
inequality in `(QCR2)`.

Put `N=n/c` and `h=k/c`. Since `0<t_0<c`,

```text
floor((n-A_0)/c)=floor((n-k-t_0)/c)=N-h-1.
```

The scale-`c` term in the conservative quotient envelope is therefore

```text
C(N,N-h-1)=C(N,h+1).
```

The rate hypothesis gives `h/N=k/n<=1/4`, hence `2h+1<=N` and

```text
C(N,h)<=C(N,h+1).
```

This comparison holds term by term for every rate-preserving active scale.
The conservative envelope may contain additional scales, so summing proves
the second inequality in `(QCR2)`.

It remains to identify nonsingleton keys. Suppose distinct slopes `z_1,z_2`
have the same key `(c,K)`, with witness codewords `p_1,p_2`. On the `k` points
of `K`, solve the two slope equations to obtain codewords

```text
c_1=(p_1-p_2)/(z_1-z_2),
c_0=(z_1 p_2-z_2 p_1)/(z_1-z_2)
```

that explain `(u,v)` on `K`. Any other slope `z` with the same key has a
witness `p_z` agreeing with `c_0+z c_1` on all `k` points of `K`; RS
uniqueness gives `p_z=c_0+z c_1` globally.

Because its full quotient support is noncontained, its tail contains at
least one coordinate where `(c_0,c_1)` does not jointly explain `(u,v)`.
Choose that coordinate and any other `t_0-1` tail points. Together with `K`
they form a noncontained `A_0`-point witness support. Thus every slope in a
nonsingleton key shares the same size-`k` core with another live slope at the
initial threshold. After any earlier paid owner is removed, a generic-branch
survivor is exactly in the P-A predicate class; a nongeneric survivor remains
in the mismatch bridge. This routing is disjoint after the fixed key order
and proves the final assertion. QED.
