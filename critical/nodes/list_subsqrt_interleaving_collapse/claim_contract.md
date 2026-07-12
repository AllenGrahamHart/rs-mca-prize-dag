# Claim contract: sub-square-root interleaving collapse

- **claim id:** `list_subsqrt_interleaving_collapse`
- **mathematical statement:** if the base worst list has size `L<|F|`, then
  the `m`-interleaved worst list is at most
  `floor(L(|F|-1)/(|F|-L))`; it equals `L` when `L^2<|F|`.
- **quantifiers and row scope:** every finite field, every linear code, every
  agreement threshold, and every integer `m>=1`.
- **consumer and slot:** safe/unsafe arity transport in
  `list_large_m_scope_closure`.
- **status:** PROVED.
- **proved dependencies:** finite-field linearity and Cauchy-Schwarz only.
- **new open content:** none.
- **falsifier:** a finite linear code with a common-support interleaved list
  exceeding the displayed rational upper bound.
- **proof route:** average collisions over all linear row projections; use
  diagonal tuples for the lower bound.
- **replay:** `python3 critical/nodes/list_large_m_scope_closure/verify.py`.
- **upstream mapping:** general list/interleaving bridge; not one of the five
  MCA hard inputs and should be offered separately if useful.
