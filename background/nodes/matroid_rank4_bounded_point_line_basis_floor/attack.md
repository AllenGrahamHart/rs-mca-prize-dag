# Attack

The weak induction using only `c<=floor((a+1)/2)` fails near the longest
official shortening.  Retaining the independent simplification bound
`c<=floor((a+r)/4)` creates the recurrence `(BPL)`.  Its coloop resets and
non-coloop increments cross once, which makes the exact floor practical to
audit over a million downstream parameter rows.
