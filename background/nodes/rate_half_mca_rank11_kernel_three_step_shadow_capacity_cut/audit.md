# Audit

The primary verifier reconstructs the exact primal and a rational Gaussian
dual on all 58 new rows, checks all 28 hierarchy inequalities, and rejects
hostile endpoint and active-set mutations.  The independent verifier derives
the dual by a backward recurrence on the seven-edge hierarchy tree.

Floating-point LP was used only to discover the active tree.  Status promotion
depends solely on the two exact integer/rational replays.
