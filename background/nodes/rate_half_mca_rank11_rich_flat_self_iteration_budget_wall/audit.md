# Audit

1. The primary verifier uses `math.comb`; the audit verifier reconstructs
   every binomial and falling factorial by independent product loops and
   scans both domains in reverse order.
2. Both implementations reproduce all `M_q`, the PR `#1173` first-rung
   threshold/slack/adjacent wall, and both two-rung minima with exact gaps.
3. The serial scan grants one branch the complete low budget and omits every
   sibling charge. Its failure is therefore a valid wall for this method.
4. The node does not infer that the rich-flat terminal is false or hopeless.
   It rules out only repetition of the same independent census.
5. Modal replays used one 256 MiB worker each; no large local computation was
   performed.
