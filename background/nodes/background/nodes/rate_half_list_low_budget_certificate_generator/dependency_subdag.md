# Dependency sub-DAG

```text
descriptor [TARGET, pinned implementation evidence] --ev-+
compiler [PROVED] ---------------------------------------+
rate_half_list_low_budget_exact_crossing [PROVED] -------+-> rate_half_list_low_budget_certificate_generator [PROVED]
rate_half_list_low_budget_all_arity_crossing [PROVED] ---+       |
                                                                 +-> list_grand [evidence: executable B*=1,2 certificates]
```

The three theorem/compiler edges are requirements. The descriptor edge is
implementation evidence, following the canonical artifact-semantics policy.
The outgoing edge is evidence only: the grand list node still contains every
larger-budget and clean-rate branch.
