# Attack plan

The direct falsifier is one official row and one production level with a
complete exact primitive ledger satisfying

```text
W_cl(R,L) > 1/32.
```

Because the ledger is nonnegative, a certified partial ledger already
exceeding `1/32` is sufficient to refute the claim; completeness is needed only
to prove the upper bound. Toy exceptional rows show that such large ledgers
can occur, but they do not refute the official-row statement.

The proof route must be per-row. A1-PROD's exceptional-prime density theorem
does not determine whether either fixed official field lies in the exceptional
set.


---

## Wave-7 additions (2026-07-13, maintainer-ratified decision 4; appended per #104 — the original text above stands, with "raw" now the ruled reading)

FALSIFIER (r2 form): one official DLI row and one production level `j`
with a complete exact RAW primitive ledger satisfying `W_cl(R,j) > 1/32`.
Multiplier shadows, additive clusters, and level lifts are not deleted
from this ledger. They may organize the search, but C1' prices every
primitive orbit at its own level and weight. See
`dli_wcl_raw_ledger_interface_guardrail`.

The exact row `(q,n',N,ell)=(65537,512,256,1)` is a positive control for
the attack machinery: its primitive weight-3 orbit contributes `64`, so
the unscoped generated-row version fails by a factor `2048`. It is not an
official DLI production row because `v_2(q-1)=16<41`; it cannot host the
ambient top subgroup. Any claimed official-row falsifier must check that
ambient split, not merely the terminal `n'=512` split.

The other banked terminal construction is also now scoped exactly:
`dli_wcl_engineered_terminal_scope` proves that its six-term norm is `2q`
with `q` prime and `v_2(q-1)=9`. See `official_terminal_attack.md` for
the correct terminal obligations and the next affine-Galois-quotiented
norm sweep.
