# Proof - L1 Mersenne HNF order-one involution-component exclusion

After multiplication by `h!`, the generalized-binomial coefficient defining
`Phi_h` is a polynomial over the integers because `h<p` on every row.

If `rho=0` or `c=0`, the generating series is `1`. If `c=1`, its two factors
cancel and the series is again `1`. Finally, at `c=-1`,

```text
(1-t)^(-rho)(1+t)^(-rho)=(1-t^2)^(-rho),             (1)
```

which has no odd-degree coefficient. Since `h` is odd, the four distinct
specializations vanish identically. The factor theorem gives (IOC1).
Direct exact expansion and division gives the degrees and term counts in
(IOC2); the verifier reconstructs this calculation from the coefficient
formula without SymPy.

It remains to exclude the only newly exposed component. Write each official
characteristic as

```text
p=2^q-1,       q in {13,17,19,31}.
```

The order of `2` modulo `p` is exactly `q`: it divides the prime `q` because
`2^q=1 mod p`, and it is not one. On `c=-1`, the torsion equation in the
order-one gate becomes, since every official `n` is even,

```text
(c-1)^n=(-2)^n=2^n=1 mod p.                          (2)
```

Equation (2) would force `q|n`. But every official `n` is a power of two and
each `q` is an odd prime. This is impossible. Hence the `c=-1` component is
empty, and every survivor lies on `Psi_h=0`. QED.
