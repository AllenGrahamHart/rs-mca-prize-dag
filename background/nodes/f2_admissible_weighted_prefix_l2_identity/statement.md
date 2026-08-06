# Plus-branch admissible F2 weighted-prefix L2 identity

- **status:** PROVED
- **closure:** proof

For one plus-branch (`p=1 mod 4`) admissible prime-field class, put

```text
H={zeta^s:0<=s<S},  ord(zeta)=2S,
Phi(A)=(sum_(y in A)y^(2j-1))_(j=1)^R in F_p^R,
N(v)=#{A subset H: Phi(A)=v}.
```

Then its weighted ternary mass is exactly

```text
Z_1 = 2^-S sum_(v in F_p^R) N(v)^2.                    (L2-1)
```

Equivalently, for the standard additive character `chi` of `F_p`,

```text
Z_1 = (2^S/p^R) sum_(u in F_p^R)
        prod_(s=0)^(S-1) cos^2(pi f_u(zeta^s)/p),       (L2-2)
f_u(y)=sum_(j=1)^R u_j y^(2j-1).
```

In particular,

```text
Z_1 >= max(1,2^S/p^R),                                 (L2-3)
```

and `Z_1<=2^{o(S)}` is equivalent to
`sum_v N(v)^2<=2^{S+o(S)}`.  This is a restricted weighted odd-prefix
`L^2` collision statement.  It is not the full max-fiber `(Q)` theorem.

For every nonempty fiber, choose one incidence vector `x_0`.  Since the
moment matrix is a parity check for the `[S,S-R]` GRS code `C`,

```text
N(v)=#{c in C: c_s in {-x_0(s),1-x_0(s)} for every s}.        (L2-4)
```

Thus each `N(v)` is also a full-agreement list-recovery output size for the
explicit GRS code with coordinate lists of size two.

No claim is made here for the coupled `p=3 mod 4` kernel.
