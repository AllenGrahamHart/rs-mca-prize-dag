# proof: census_window_arithmetic

## Claim
Per (rate, candidate A): undecided rows = {admissible q = 1 mod n :
floor(q/2^128) in [L(n,A), K(n,A))} with K now EXACT (census_exact_counts) and
L = the certified-distinct lower bound (the certification-strength input). The
census output is the exact map L -> undecided window.

## Proof
With K(n,A) = C(N'*, l'(A)) exact (census_exact_counts), the window is
[L, K) by definition: rows with B* < L are decided-unsafe by the certified
family; rows with B* >= K cannot be witnessed by this stratum's raw count;
the interior is undecided. Window sizes in bits = log2 K - log2 L, from the
exact table; as L -> K the windows vanish (monotone in L, trivially). The
dodge complement: exhibited-row partials select q with B* outside every
window — always possible since the windows have finite total measure in
B*-space while admissible primes are unbounded (census_dodge_selection's
content, cited). The rate-1/2 window is bounded below the gate by the exact
3.8-bit shortfall; rate 1/4's window spans the staircase gap [103.24, 128];
rates 1/8 and 1/16 have gate-interior windows whose exact K-side endpoints
are the table entries. ∎
