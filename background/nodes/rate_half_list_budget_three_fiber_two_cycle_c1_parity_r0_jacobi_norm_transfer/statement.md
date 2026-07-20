# Budget-three fiber-two c=1 parity R0 Jacobi-norm transfer

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_r0_lift_free_compiler`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_torsion_cyclotomic_norm_decomposition`

Retain the official `R0` packet and put

```text
M=2^36,       L=2M=2^37,       r^(32M)=1,
a=(r+r^(-1))/2,       u=r^2,
x=(u+u^(-1))/2=2a^2-1,
epsilon=r^(16M) in {1,-1}.                          (RJN1)
```

Let

```text
C(x)=C_L^(1/4)(x),       P(x)=P_(2L-1)(x).          (RJN2)
```

The primary gap, source torsion, and lift-free `R0` constant gate are exactly

```text
C(x)=0,       T_(8L)(a)=epsilon,
E_epsilon(x):=(1+epsilon P(x)^2)^2+x^2-1=0.         (RJN3)
```

Since the primary polynomial has no root at `x in {0,1,-1}`, define

```text
G_-(x)=T_(2L)(x),       G_+(x)=U_(2L-1)(x).         (RJN4)
```

For a fixed `epsilon`, the complete `R0` primary/torsion/constant packet is
nonempty over the algebraic closure if and only if

```text
gcd(C,G_epsilon mod C,E_epsilon mod C)!=1.          (RJN5)
```

The even-Jacobi transform halves the primary degree. Put

```text
w=2x^2-1,       z=(w+1)/2=x^2,
J(w)=J_M^(-1/4,-1/2)(w),
Q(w)=J_(L-1)^(0,1/2)(w) mod J(w),       deg Q<M,

F_epsilon(w)=(1+epsilon zQ(w)^2)^2+z-1,
K_-(w)=T_L(w),       K_+(w)=U_(L-1)(w).             (RJN6)
```

Then `(RJN5)` is coverage-equivalent to the two tests

```text
gcd(J,K_epsilon mod J,F_epsilon mod J)!=1,           (RJN7)
```

one for each torsion sign, with every representative reduced to degree less
than `M=2^36`.

The torsion-only prefilter is exactly the already-defined CR-002 norm pair

```text
R_-=Res_w(J,T_(2M)),       R_+=Res_w(J,U_(2M-1)).    (RJN8)
```

Up to powers of two, `R_-^2` is the order-`8M=2^39` cyclotomic norm, while
`R_+^2` is the 37-level tower at orders `2^2,...,2^38`. Thus a contributor
evaluation of those norms screens both the matched `c=0` packet and this
`c=1 R0` packet; no separate large norm run is needed.

In the nonsplit field shard, `epsilon=1` is the invariant-lift packet and
`epsilon=-1` is the anti-invariant `R0` packet. Both signs may occur in the
split shard.

This is a complete degree-halved primary/torsion/constant interface for
`R0`. It does not evaluate the norms, prove either gcd is one, or discharge
the Euclidean twisted-fourth-power and gcd gates.

