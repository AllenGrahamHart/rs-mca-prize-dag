# Historical fpylll observation

The retired proof text reported a shortest-vector norm of approximately
`31.67`, compared with the Euclidean box radius `2 sqrt(64) = 16`, and an
observed vector infinity norm of `9`. These values came from the launcher
`modal_e1_cert.py` over

```text
p = 562949953421383 * 2^200 + 1.
```

No exact result record or completeness certificate was committed. The
launcher can silently fall back from exact SVP to BKZ, and its return object
does not distinguish those paths. Consequently these numbers are retained
only as a falsification-survival observation; they are not proof of the node.
