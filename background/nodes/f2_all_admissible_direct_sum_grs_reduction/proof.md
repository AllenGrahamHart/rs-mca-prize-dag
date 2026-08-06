# Counterexample proof

Let `n=2^41` and `p=2^61-1`. Lucas-Lehmer certifies that `p` is prime.
Also

```text
p=-1 mod n,
q=p^2<2^122<2^256,
n | q-1,
ord_n(p)=2.
```

Hence `F_q` is an official admissible field and the row is generating:
`ord_n(p)=[F_q:F_p]=2`.

The erroneous all-row order formula used `v2(p-1)=1` to predict
`ord_n(p)=2^40`; the actual order is two. More intrinsically, for the
dyadic root group `G` of order `n`,

```text
|G intersect F_p^*|=gcd(n,p-1)=2.
```

Two root positions are `F_p`-proportional exactly when their ratio lies in
this intersection. The only possible ratio is therefore `+1` or `-1`.
The antipodal half-system contains one representative from every pair
`{y,-y}`, so no two distinct retained positions are proportional. It has
`n/2=2^40` positions and hence `C=2^40` singleton classes, contradicting
`C<=4`.
