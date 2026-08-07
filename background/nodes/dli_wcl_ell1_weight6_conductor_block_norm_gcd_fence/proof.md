# Proof

Write every signed sum with exponents in `[0,255]`. Its representing
polynomial has degree at most `255`, whereas the minimal polynomial of
`zeta_512` is `X^256+1`. Hence a nonempty signed polynomial cannot vanish in
characteristic zero, proving `S_epsilon!=0`.

The nontrivial automorphism of `K/K_0` sends `zeta` to `-zeta`. Applying it
term by term gives `(CB2)`. On global-sign classes, multiplication by `eta`
has a fixed point exactly when `eta` is a global sign, equivalently when all
six exponents have the same parity.

Choose the largest power `2^d` for which the six residue classes lie in one
coset modulo `2^d`. Write

```text
x_i=c+2^d z_i mod 256.
```

Changing an integer representative by `256` multiplies the corresponding
order-512 root by `-1`, which is absorbed into `epsilon'_i`. This proves
`(CB3)`. Maximality makes the `z_i` mixed in parity. They remain distinct
modulo `256/2^d`. Since that modulus contains six distinct residues, it is
at least six, and hence `d<=5`.

Put `K_d=Q(zeta_(512/2^d))`. The cyclotomic degree ratio is
`[K:K_d]=2^d`. The root-of-unity prefactor in `(CB3)` has absolute rational
norm one, while an element of `K_d` has its `K_d/Q` norm repeated `2^d`
times under `K/Q`. This proves `(CB4)`.

It remains to compute the block norms at the maximal conductor. First suppose
the exponent sum is even. A parity-adapted pairing has three same-parity
pairs. Fixing the three internal pair signs defines one Heron block of four
global-sign classes; the four classes vary only by the external signs of the
three pair sums. The automorphism `sigma` preserves every internal sign and
flips the external sign exactly on odd-odd pairs. Because the support is
mixed, this external flip is not global. The block is therefore the disjoint
union

```text
{epsilon,sigma epsilon} union {theta,sigma theta}.
```

The pair-Heron identity says, up to an irrelevant sign,

```text
H=S_epsilon sigma(S_epsilon) S_theta sigma(S_theta).
```

Taking `K_0/Q` norms proves `(CB5)`.

Now suppose the exponent sum is odd. The parity-adapted pairing has exactly
one mixed pair. The automorphism reverses that pair's internal sign and
therefore exchanges the two conjugate Heron blocks. Their product is the
parent theorem's quadratic block `Q=C^2-dD^2`. Its eight sign classes form
four free `sigma`-orbits. Choosing one representative from each orbit gives

```text
Q=+/- product_(j=1)^4 S_(epsilon_j)sigma(S_(epsilon_j)),
```

and `(CB6)` follows after taking the `K_0/Q` norm.

Equations `(CB5)` and `(CB6)` show that every relevant block integer contains
`N_epsilon` as an integer factor. Their gcd therefore contains it as well.
This proves the route fence. QED.
