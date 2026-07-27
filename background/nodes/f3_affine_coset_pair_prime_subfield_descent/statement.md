# Mattarei affine-pair prime-subfield descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound` (evidence)
- **dependency:** `f3_affine_coset_pair_mattarei_bound`

Let `F_q/F_p` be a finite extension, let `K<=F_p^*` have order `m`, and
put `d=(p-1)/m`. Let

```text
L_i(X)=a_i X+b_i,       a_i in F_p^*, b_i in F_p,
```

be nonproportional affine forms. Then

```text
{x in F_q:L_1(x),L_2(x) in K}
 ={x in F_p:L_1(x),L_2(x) in K}.                 (PSD1)
```

Consequently, if `d>=4` and `d^3>=4m`, the Mattarei transport gives

```text
#{x in F_q:L_1(x),L_2(x) in K}
 <C_M m^(2/3),       C_M=3*2^(-2/3).              (PSD2)
```

Thus a nonprime ambient field is not by itself an obstruction: the pointwise
bound survives whenever the subgroup and the affine pencil descend to the
prime subfield.

For the deployed KoalaBear parameters

```text
p=2^31-2^24+1,       q=p^6,       n=2^21,
```

one has

```text
p-1=127*2^24,        (p-1)/n=1016,
1016^3=1048772096>4n,       p=2 (mod 3).           (PSD3)
```

Hence `H=mu_n` lies in `F_p`, its cube-preimage subgroup is again `H`, and
every DSP8 nodal or quotient affine pencil whose coefficients are built from
`H` descends to `F_p`. Mattarei's pointwise bound is therefore valid for that
subproblem even when it is viewed inside `F_(p^6)`.

This descent does not apply to the deployed Mersenne-31 quartic domain:
for `p_M=2^31-1`, `v_2(p_M-1)=1`, so an order-`2^21` domain subgroup is not
contained in `F_(p_M)`. No extension-field Mattarei theorem is claimed.
