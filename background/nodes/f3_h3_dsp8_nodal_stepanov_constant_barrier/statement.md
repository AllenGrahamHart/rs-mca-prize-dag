# DSP8 nodal Stepanov constant barrier

- **status:** PROVED
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_affine_coset_pair_cubic_preimage_stepanov`,
  `f3_h3_dsp8_nodal_cube_preimage_envelope`

Consider any positive parameters `m,A,B,D` in the one-auxiliary-polynomial
Stepanov construction used by the nodal affine-pair theorem. Its two counting
constraints are

```text
D(A+D)<AB^2,       AB<=m.                            (NSB1)
```

Then its degree-to-multiplicity quotient necessarily satisfies

```text
(A+2mB)/D > 2^(5/3)m^(2/3).                         (NSB2)
```

Thus `2^(5/3)` is a strict constant floor for this ansatz, independently of
how its integer parameters are retuned. The current printed constant is very
close to that floor:

```text
(51/16)^3=132651/4096 >32=(2^(5/3))^3.              (NSB3)
```

In the three-cubic-root nodal lane, applying this ansatz once to the order-`n`
quotient line and once to the order-`3n` cube-preimage intersection yields a
class-blind leading coefficient strictly greater than

```text
17*32*3^(4/3)>2176>76599/40.                        (NSB4)
```

Consequently no choice of `A,B,D` inside the existing one-polynomial
Stepanov proof can make the class-blind three-cubic-root nodal envelope fit
the live uniform `G=4K` DSP8 allowance. A useful next argument must exploit
the target, richness, signed-disjointness, trace distribution, or a genuinely
stronger multi-fiber theorem.

This is a proof-method barrier, not a lower bound on the actual nodal record
count and not a counterexample to DSP8.
