# Deployed identity-prefix owner-scope audit

- **status:** PROVED
- **closure:** proof
- **role:** roadmap N3 stress test against the upstream deployed unsafe rows
- **upstream:** `przchojecki/rs-mca@32a41660`

The four deployed identity-prefix attacks have the following exact adjacent
values:

| row | object | `a0` attack | `a+` attack | `B*` |
|---|---|---:|---:|---:|
| KoalaBear | MCA | 138634741058327852652 | 57198030366 | 274980728111395087 |
| KoalaBear | list | 157702518233425975347 | 65065153468 | 274980728111395087 |
| Mersenne-31 | MCA | 4281388998575706 | 1752700 | 16777215 |
| Mersenne-31 | list | 4870025984688527 | 1993678 | 16777215 |

In each row the printed attack is above budget at `a0` and below budget at
`a+=a0+1`. The latter is only cessation of this lower attack, not a safe
upper certificate.

These attacks do not contradict the local aperiodic-column bounds:

1. a boundary identity-prefix list member is a prefix/Q owner at its complete
   agreement shell;
2. every strict-interior support spray from the same construction cancels
   from the lower exact shell and reappears as boundary Q at its true higher
   shell; and
3. the MCA rows apply the identity-prefix list through the simple-pole
   conversion, so their local owner is the F1 pole/list column, before the
   post-strip aperiodic residual.

The Mersenne-31 circle rows are useful arithmetic stress rows but are not in
the official multiplicative-coset smooth-domain quantifier. Therefore the N3
audit verdict is `NO ISSUE`: the upstream floors do not enter local `B_ap`.
No aperiodic upper bound or adjacent safe row is proved.
