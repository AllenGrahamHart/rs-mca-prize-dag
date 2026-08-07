# Audit

- Batch app: `ap-No47lO7RZNHv7Y28bnT35H`; output SHA-256
  `5f1ea688ab3a8ca66cdcfa0343673588c4f60bf70925b24808bf8ed32a1bbcce`.
- `F07-R02` retry app: `ap-mmwbs5ExgtVnZv87wE1Tey`; output SHA-256
  `d78864704fa48cfe08bcf69716b8c0d5c04d244737a820324da64edb949d0cdf`.
- The batch had two completed proofs and four bounded timeouts. The verifier
  accepts only completed `DONE` records and checks the timeout scopes
  separately.
- The successful retry took 1056 seconds and under 0.92 GB peak resident
  memory in its Modal container.
