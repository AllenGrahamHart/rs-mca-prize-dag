# Proof

For a common-`K` source lift, the negative complete-fiber Vieta equation is

```text
A_1(kappa)+q_kappa B_2(kappa)=0,
q_kappa=x_kappa(a_kappa+b_kappa).                 (1)
```

The parent proves `x_kappa B_2(kappa)!=0` on all five `K` fibers.  If the
edge is antipodal, `a_kappa+b_kappa=0`, so `(1)` gives
`A_1(kappa)=0`.  Conversely a nonantipodal edge joins labels from distinct
signed pairs and has nonzero sum; hence its `q_kappa` is nonzero.

Three antipodal edge orbits lie over three distinct `K` labels.  Since
`deg A_1<=2`, they force `A_1=0`.  Every five-edge profile contains a
nonantipodal edge: there are only three antipodal types, and parent
injectivity forbids repeating their products.  At that edge, `(1)` becomes
`q_kappa B_2(kappa)=0`, contradicting both nonzero factors.  This proves
`(KBNL-1)`.

The parent lists seven injective multiplicity skeletons.  Their total loop
counts are respectively `1,2,3` in profile `(4,4,2)` and `0,1,2,3` in
profile `(4,3,3)`.  Removing the two count-three rows gives exactly
`(KBNL-2)`.  Finally, one or two distinct loop roots divide the degree-two
form `A_1`, proving the stated factor pins. QED.
