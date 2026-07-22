# Proof of the QA.22 small-scale ledger extension

The complete proof is `qme_proof.md`; this file records the conventional
critical-node interface.

1. Since `A_own(M)<=k+M<=n-M` for `M<=t`, every binomial cell exists.
2. `n/(n-A_own)<=2/(1-rho)<=4`, so Lemma COL's landing is at most
   `4 Q_M(A_own)`, inside the allowance by the exact factor `719/4`.
3. Exact stabilizer scale separates `[2,t]` from `(t,n]`. Agreement parity
   separates every even `A_own` from the seven banked odd-agreement rows.
4. For `13<=s<=20`, the first-scale inequality is checked with exact
   integers. For `21<=s<=44`, elementary binomial entropy bounds with
   dyadic-rational logarithm certificates prove it with at least 168,245 bits
   of margin. The exact overlap rows validate the certificate inequalities.
5. Pascal's identity relates the top extension column to the planted column,
   and exact integer division gives `719=floor(n^6/C(n+6,6))` at all four
   maximal rows.

`qme_verify.py` independently replays 3,392 own cells, all four rate maxima,
the exact and certified regimes, the planted-column identity, and five
required-to-trip mutations. `verify.py` hash-pins that source and its packet
and requires byte-identical output to the banked result.

This proof consumes the already-proved column lemma, exact stabilizer
partition, ledger convention, and planted lower count. It makes no claim for
their statements beyond the interfaces identified in `qme_claim_contract.md`.
