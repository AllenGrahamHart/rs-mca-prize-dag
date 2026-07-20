# Dependency sub-DAG

```text
mca_grand [CONDITIONAL] ----+
                              +--> submission_quality_paper_dossier [TARGET/artifact]
list_grand [CONDITIONAL] ---+          |
                                       v
compiler [PROVED] ----------------> packaging [CONDITIONAL] --> prize [CONDITIONAL]
harness [PROVED] --------------------^ 
dossier_partial [PROVED] ------------^  (template only)
bridge_ledger [PROVED] ---------------^
```

The final dossier target carries its own materialization work after the grand
claims become green. It prevents the partial dossier from silently satisfying
the roadmap's submission-quality termination condition.
