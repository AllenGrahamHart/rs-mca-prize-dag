# Proof

The coordinate source lift gives

```text
star(-x)=-star(x).                                 (1)
```
Replacing `([r:s],a,b)` by `([-r:s],-a,-b)` fixes both `ab` and
`r*s*(a+b)`. Swapping `a,b` also fixes them, proving that `(KBKV-1)`
is a quotient-fiber record. Rescaling `[r:s]` gives `q` weight two,
which is exactly the weight used below.

For the positive source form, evaluation at `X=x_kappa` gives

```text
H(T,x_kappa)=A_2(kappa)T^2
             +r*s B_1(kappa)T+A_0(kappa).         (2)
```
The actual star consists of the two roots `a_kappa,b_kappa`, and its
leading coefficient is nonzero. Comparing `(2)` with
`A_2(kappa)(T-a_kappa)(T-b_kappa)` gives

```text
A_0(kappa)=p_kappa A_2(kappa),
r*s B_1(kappa)=-(a_kappa+b_kappa)A_2(kappa).
```
Multiplying the second identity by `r*s` and using
`(r*s)^2=u*v` proves `(KBKV-2+)`. If `r*s!=0`, the converse follows
by division. If `r*s=0`, star transport fixes the source point and forces
the prescribed edge to be `{a,-a}`; equation `(2)` is even, and the first
equation recovers its product. Thus the converse also holds at ramification.

For the negative source form,

```text
H(T,x_kappa)=r*s B_2(kappa)T^2
             +A_1(kappa)T+r*s B_0(kappa).         (3)
```
At `r*s=0`, its binary quadratic is proportional to `T_0T_1`, whose
roots are the two fixed points of `tau`; neither lies in the fixed-point-
free label set `J`. Hence an actual negative `J-J` star has
`r*s B_2(kappa)!=0`. Comparison with
`r*s B_2(kappa)(T-a_kappa)(T-b_kappa)` then gives exactly `(KBKV-2-)`,
and the converse follows by Vieta.

Writing the coefficients of `A_2,A_0,B_1` gives eight homogeneous
unknowns in `(KBKV-2+)`, while `B_2,B_0,A_1` gives seven in
`(KBKV-2-)`. A nonzero actual source form therefore forces the printed
rank bounds. The second positive equations alone have the following
homogeneous coefficient rows on `(A_2,B_1)`:

```text
[q*v^2,q*u*v,q*u^2,u*v^2,u^2*v].
```

The negative rows on `(B_2,B_0)` and `(B_2,A_1)` are respectively

```text
[-p*v,-p*u,v,u],
[q*v,q*u,v^2,u*v,u^2].
```

Their rank and determinant consequences are `(KBKV-3+)--(KBKV-3-)`.
In the affine chart `v=1` these reduce to the initially displayed
`kappa` formulas. QED.
