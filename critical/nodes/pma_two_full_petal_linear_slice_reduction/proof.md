# Proof: PMA two-full-petal linear-slice reduction

For `(F,W) in V_s`, divisibility gives unique polynomials

```text
A_i=(W-c_iF)/L_i,       deg A_i<=d-ell=s.
```

Subtracting the two equations yields

```text
L_1A_1-L_2A_2=(c_2-c_1)F,
```

and then `W=c_1F+L_1A_1`. This proves that every member has the form (TF2).
Conversely (TF2) gives

```text
W-c_1F=L_1A_1,
W-c_2F=L_2A_2,
```

and all degrees are at most `ell+s=d`, so it gives a member of `V_s`.

The parameter map is injective. If `L_1A_1=L_2A_2`, coprimality implies
`L_1|A_2`; but `deg A_2<ell` unless it is zero. Hence `A_2=0`, and then
`A_1=0`. The parameter space therefore has dimension `2(s+1)`, proving
(TF3). The same argument proves that its projection to `F` is injective, so
(TF4) follows.

Assume `gcd(F,L_1L_2)=1`. A common root of `F` and `W` is not a root of
either `L_i`; from `W-c_iF=L_iA_i` it is therefore a common root of
`A_1,A_2`. Conversely a common root of `A_1,A_2` is a common root of `F,W`
by (TF2). This proves (TF5) over an algebraic closure and hence the polynomial
gcd equivalence over `K`. QED.

The proof has used only the two displayed petal divisibilities. In the PMA
application, the core-defect reduction additionally says that every selected
background agreement is a root of `W`. Hence `V_s` is an ambient envelope for
a fixed PMA cell; no converse from an arbitrary member of `V_s` to an exact
contributor is asserted here.
