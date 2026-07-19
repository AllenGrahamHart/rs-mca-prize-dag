# proof: e1_pocklington_250bit_exhibit_field

Let

```text
c = 562949953421383
F = 2^200
p = cF + 1.
```

The verifier checks the exact displayed decimal value of `p`, `p < 2^256`,
`p mod 256 = 1`, and `F^2 > p`.

Use Pocklington's theorem with the known factor `F = 2^200` of `p-1`.
The only prime divisor of `F` is `2`. For base `a=3`, the verifier checks

```text
3^(p-1) = 1 mod p
gcd(3^((p-1)/2) - 1, p) = 1.
```

Since `F > sqrt(p)`, these two checks satisfy Pocklington's criterion, so `p`
is prime.

Because `p-1` is divisible by `256`, the multiplicative group `F_p^*` contains
elements of orders `128` and `256`. The same verifier checks the displayed
`rho_128` and `rho_256` by testing

```text
rho_N^N = 1 mod p
rho_N^(N/2) != 1 mod p
```

for `N in {128,256}`. These are exact primitive roots for the two E1 folded
certificate cells.
