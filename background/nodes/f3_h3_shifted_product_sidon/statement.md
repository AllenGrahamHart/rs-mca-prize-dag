# Dyadic shifted roots are multiplicatively Sidon in characteristic zero

- **status:** PROVED
- **role:** finite-characteristic reduction for the C36' non-swap moment

Let `n=2^s`, `s>=2`, let `H=mu_n(C)`, and put

```text
A=(1-H)\{0}.
```

Then `A` is multiplicatively Sidon up to the unavoidable swap:

```text
ab=cd,  a,b,c,d in A  =>  {a,b}={c,d}.          (SID)
```

It follows that every nonidentity quotient fiber over `C` also has
multiplicity at most one.

Consequently, if `p=1 mod n`, `H_p=mu_n(F_p)`, and
`A_p=(1-H_p)\{0}`, every non-equal, non-swap product collision in `A_p`
is a finite-characteristic norm-gate event. More precisely, after lifting its
four root exponents to `zeta_n`, the nonzero cyclotomic integer

```text
alpha=(1-x)(1-y)-(1-u)(1-v)
```

reduces to zero at a prime above `p`; hence

```text
p divides Norm(alpha),       0<|Norm(alpha)|<=6^(phi(n)).
```

Thus every record counted by the C36' non-swap multiplicity `Q(t)` is
`p`-specific. Moreover, at a finite row one has the exact accident-depth split

```text
S_ns = sum_(t!=1,R(t)>0) Q(t)
     + sum_(t!=1) Q(t)(R(t)-1)_+.               (AD)
```

Every record in the first sum requires one finite-characteristic collision.
Every unit in the second also requires a nonunique quotient representation,
which is another collision forbidden in characteristic zero. This theorem
does not bound how many such records can concentrate at one official prime,
and it does not prove the open `S_ns^rich<=1200n^2` estimate.
