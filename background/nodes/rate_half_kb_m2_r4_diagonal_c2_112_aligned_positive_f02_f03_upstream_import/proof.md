# Proof

This node imports the exact local theorem at upstream commit
`826c0e7610604d550b8dd9b772c197a4e660e525`. The proof object uses
`p=2130706433`, factors every q-slice equation before localization, and
removes only the 34 declared named-open factors.

For `F02-R11`, the unique residual branch has localized Groebner basis `[1]`.
For `F02-R02` and `F02-R20`, three of the four factor branches have basis
`[1]`; branch `(0,0)` survives. Their exact lex schemes have dimensions four
and eight, with `w` eliminants

```text
R02: w^2 + 940017546 w + 1,

R20: (w^2 + 584912723 w + 1)
     (w^2 + 1190675975 w + 1).                     (1)
```

All three quadratics are irreducible over `F_p`. The certificate enumerates
every point over `F_(p^2)`, checks all branch generators and the raw localizer,
reconstructs the complete source form, and evaluates both quotient
identities.

For a remainder `A w+B` modulo `w^2+a w+1`, its norm is

```text
N(Aw+B)=B^2-aAB+A^2 mod p.                         (2)
```

The six recorded mismatch pairs are:

| target | `a` | side | `A` | `B` | norm |
|---|---:|---|---:|---:|---:|
| R02 | 940017546 | J | 317112865 | 1161791022 | 627736383 |
| R02 | 940017546 | I | 462252474 | 145305698 | 1796550960 |
| R20 | 584912723 | J | 1671616282 | 297746731 | 555560394 |
| R20 | 584912723 | I | 134663927 | 1672091025 | 1334100861 |
| R20 | 1190675975 | J | 309729886 | 1997957961 | 2008265187 |
| R20 | 1190675975 | I | 1042061214 | 2038553966 | 1196113770 |

The local verifier recomputes every norm from these values. All are nonzero,
so no finite q-slice point satisfies either complete quotient identity.

Finally, the upstream compiler reconstructs all twelve source assignments
and proves the complete literal transport `F02(b^-1)=F03(b)` factor by
factor. This transports the three emptiness conclusions to `F03`.

The pinned proof-object hashes are:

```text
certificate raw SHA-256  4cfbc86bdf1c295e832fa23414d2a7b98ebc5a05bfe2cc88e0ecbf076c5e7925
certificate payload      51572f4d190a3bceb31494ae7ee48f6b026346413ae398d2da4f7b1da1402438
Sage compiler             e65439765b029443f8f309da74e4195ba7cd96db9f1d0c89145d3582e3d04061
Python verifier           80ab8beb9a4644b6d6779918c679baff440552bcd3c3134b4b405438c194cb4a
theorem note              b3aca650fc8f2f41f99e59d17fe2df926ab7a7fb4895cae6f20127c802b2c1d0
```

The exact upstream Python replay returned the payload above and
`fail-closed semantic mutations 26/26`. The upstream theorem note records an
independent full Sage/Python review. This proves the imported six-cell local
theorem. QED.
