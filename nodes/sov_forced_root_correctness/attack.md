# ATTACK - sov_forced_root_correctness

Status: conditional.

The recursion algebra is now proved in
`sov_forced_root_recursion_algebra`. The active proof obligation is
`sov_active_core_obstruction_vanishing`: connect active-core equations in the
intended band to the finite `h`-trade square-shift model used by X79.

The Modal helper contains a gate for this predicate, but the recorded app logs
did not emit the gate JSON. Replaying the gate off-laptop is useful evidence,
not closure for the active-core bridge.
