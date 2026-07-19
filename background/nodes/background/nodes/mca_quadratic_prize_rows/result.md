# Verification result

The standalone verifier passed on Modal on 2026-07-13:

```text
app: ap-ch5PkckXFfHvrs8p6qHR03
MCA_QUADRATIC_PRIZE_ROWS_PASS
proof_rows=32654
toy_max=(1, 2)
r1_2:  n=2^41, pbits=167, B=389500552609
r1_4:  n=2^42, pbits=169, B=1210584858040
r1_8:  n=2^43, pbits=170, B=2879806199253
r1_16: n=2^44, pbits=171, B=6233898019554
MODAL_RUN exit=0 peak_rss=57MB
```

The run checked 32,654 finite parameter instances of the quadratic proof
arithmetic, exhaustively enumerated a small MDS syndrome-space model, replayed
all four Proth certificates, and checked every target division and adjacent
quadratic sign with exact integers.

Repository integration also passed:

```text
full replay: 129/129 PASS, app ap-IT8b7Rpz4JqaGmpxLRPfXF
five gates:  MODAL_GATE_AUDIT_PASS, app ap-ELTrVGhWfnEyHxbVPlliFi
orbit build: MODAL_ORBIT_BUILD_PASS, app ap-p6o5AEiHIQLwvuxa4oxHBo
open truth leaves after rebuild: 9
```
