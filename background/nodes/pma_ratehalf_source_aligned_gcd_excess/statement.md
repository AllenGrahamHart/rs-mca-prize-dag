# PMA rate-half source-aligned gcd excess

- **status:** PROVED
- **consumer:** `petal_mixed_amplification`
- **role:** expose the exact source coupling in the remaining `M=4,t=3` tail

## Statement

Use the rate-half tail notation of
`pma_ratehalf_core_triple_excess_reduction`. Let `C` be the core,
`L_C` its monic locator of degree

```text
N=4ell+b-2,
```

and let `L_1,L_2,L_3` be the three touched petal locators. Put
`L=L_1L_2L_3`. For distinct source labels `c_1,c_2,c_3`, let `E_c` be the
unique polynomial of degree less than `3ell` satisfying

```text
E_c == c_i mod L_i.                                  (AG1)
```

Euclidean division gives unique polynomials `P_*` and `Y` with

```text
L_C E_c=P_*+L Y,       deg P_*<3ell.                 (AG2)
```

Then `P_*` is exactly the degree-`<3ell` interpolant of the three planted
petal labels, and the core received word in the preceding reduction is

```text
y=Y|_C=-P_*/L|_C.                                    (AG3)
```

For fixed `C,L_1,L_2,L_3`, varying the three labels gives a
three-dimensional linear code on `C`. Every nonzero word in that code has
weight at least

```text
N-(3ell-1)=ell+b-1=K_0.                              (AG4)
```

Now let `H_1,H_2,H_3` be distinct polynomials of degree at most `K_0-1`, put

```text
P_i=P_*+L H_i,
A=H_1-H_2,       B=H_1-H_3,
```

and let `gcd` below be monic. Define

```text
u_12=deg gcd(L_C,A,P_1),
u_13=deg gcd(L_C,B,P_1),
u_23=deg gcd(L_C,B-A,P_2),
tau =deg gcd(L_C,A,B,P_1).                           (AG5)
```

If every `H_i` agrees with `y` on at least

```text
m=2ell+b+a-2
```

core points, then the exact source-aligned overlap certificate is

```text
u_12+u_13+u_23-tau
 >=3m-N
 =2(K_0-1)+3a.                                      (AG6)
```

Consequently a fixed tail cell has at most two contributors unless the
three-dimensional source quotient code admits (AG5)--(AG6). If no such
certificate occurs in any tail cell, all four touched triples and all tail
defects contribute at most `8n` codewords per carried source.

## Scope

This theorem does not exclude (AG6), count its solutions, or assign them to a
profile. It replaces the vague phrase "use source coupling" by an explicit
CRT quotient code and one polynomial-gcd inequality. Equality fibers not
aligned with `P_*` do not contribute to (AG6).
