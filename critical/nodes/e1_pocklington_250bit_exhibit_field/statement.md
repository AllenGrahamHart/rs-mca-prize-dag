# e1_pocklington_250bit_exhibit_field

- **status:** PROVED
- **closure:** proof

## Statement

The integer

```text
p = 904625697166646869347790708689937759412227977745095982970820953353127723009
  = 562949953421383 * 2^200 + 1
```

is prime, has bit length `250`, satisfies `p < 2^256`, and satisfies
`p = 1 mod 256`.

Consequently `F_p` is a valid named E1 exhibit field for both open folded
certificate cells `N'=128` and `N'=256`. It contains primitive roots of both
orders; in particular, with base `3`,

```text
rho_128 = 3^((p-1)/128) mod p
        = 440266185830122294862552098878717819794821358702875176198798016633729926114

rho_256 = 3^((p-1)/256) mod p
        = 368095729527972287347366462180303065908636718991804826343652948937354262881
```

have exact orders `128` and `256`, respectively.

## Falsifier

A failed Pocklington condition for `p`, `p >= 2^256`, `p != 1 mod 256`, or
failure of one of the displayed root-order checks.
