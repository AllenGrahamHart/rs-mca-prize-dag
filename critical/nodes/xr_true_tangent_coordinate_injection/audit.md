# Audit

The proof isolates the part of upstream `thm:deep-mca` Step 3 that never used
minimum distance. Deepness is needed earlier to prove that every close
codeword equals the recovered line codeword. Once that equality is an
explicit branch hypothesis, the coordinate injection is unconditional.

`verify.py` exhausts all `3^8` error pairs of length four over `F_3`, checks
the injection for every finite slope, and checks the repaired DAG edge.
