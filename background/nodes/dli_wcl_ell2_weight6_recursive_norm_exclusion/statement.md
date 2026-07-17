# DLI ell-two weight-six recursive-norm exclusion

- **status:** PROVED
- **closure:** exact computation plus proof
- **dependencies:** `dli_wcl_ell2_weight3_ambient_exclusion` and
  `dli_wcl_ell2_weight6_triple_cubic_router`

Let `q<2^256` be an official production characteristic with
`v_2(q-1)>=41`, and let `omega` have exact order `1024` in `F_q`. There is no
reduced signed polynomial `P` of weight six such that

```text
P(omega)=P(omega^3)=0.
```

Equivalently, the residual weak-column slot `(ell,w)=(2,6)` is empty on every
official row.

The exact certificate quotients the triple-cubic router by odd Galois
dilation and by rechoosing the normalized root inside the selected triple.
It covers all `404,740` resulting candidates. Of these, `404,230` have a
nonzero saturated norm gcd whose complete prime factorization has

```text
443 distinct prime roots,       max v_2(p-1)=18<41.
```

The remaining `510` candidates make both obstruction elements identically
zero in `Z[zeta_1024]`. The power-of-two vanishing-sum lemma forces an
antipodal pair in the reconstructed six-root multiset, so none passes the
reduced-support guard.
