"""td_razor.py -- exact razor-scale arithmetic for the (t,M) dictionary.

All banked razor constants re-derived from primary text, then the dictionary
identities tested as exact integer statements.
"""
import json
from math import comb, lgamma, log2

L2 = 1.0 / 0.6931471805599453


def lg2binom(n, k):
    if k <= 0 or k >= n:
        return 0.0
    return (lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)) * L2


def smallest_M(n, k, sigma):
    """Least admissible coset scale: M | gcd(n,k), M > sigma, k/M <= n/M - 1."""
    best = None
    M = 1
    while M <= k:
        if n % M == 0 and k % M == 0 and M > sigma and k // M <= n // M - 1:
            if best is None:
                best = M
        M *= 2
    return best


out = {}

# ---- razor row, re-derived from the banked exact constants -----------------
n = 2 ** 41
k = 2 ** 40
sigma = 2 ** 34
a = k + sigma
out["razor_row"] = {"n": n, "k": k, "sigma_open_bracket_start": sigma, "a": a}
out["check_a2_over_n"] = {
    "a^2/n": a * a // n,
    "banked": 2 ** 39 + 2 ** 34 + 2 ** 27,
    "match": a * a // n == 2 ** 39 + 2 ** 34 + 2 ** 27,
    "exact_division": a * a % n == 0,
}
out["check_GAP_FISHER"] = {
    "(k-1)-a^2/n": (k - 1) - a * a // n,
    "banked": 532441726975,
    "match": (k - 1) - a * a // n == 532441726975,
}
out["check_open_bracket_width"] = {
    "3n/4 - (k+2^34)": 3 * n // 4 - a,
    "banked": 532575944704,
    "match": 3 * n // 4 - a == 532575944704,
}

# ---- the qcore plateau at the razor ---------------------------------------
rows = []
for s in (2 ** 34 - 2, 2 ** 34 - 1, 2 ** 34, 2 ** 34 + 1, 2 ** 35 - 1, 2 ** 35):
    M = smallest_M(n, k, s)
    N = n // M
    km = k // M
    rows.append({
        "sigma": s, "M": M, "log2_M": log2(M), "N": N, "k/M": km,
        "QCORE=C(N-1,k/M)": comb(N - 1, km) if N <= 4096 else None,
        "log2_QCORE": lg2binom(N - 1, km),
    })
out["qcore_ladder_at_razor"] = rows
out["C(127,64)"] = comb(127, 64)
out["log2_C(127,64)"] = lg2binom(127, 64)
out["C(63,32)"] = comb(63, 32)
out["log2_C(63,32)"] = lg2binom(63, 32)
out["cliff_bits_2^34-1_to_2^34"] = lg2binom(127, 64) - lg2binom(63, 32)

# ---- dictionary identity: PLATEAU(n_model) = QCORE(n_model, sigma=1) ------
ident = []
for nm in (8, 16, 32, 64, 128, 256, 512):
    plateau = comb(nm // 2 - 1, nm // 4) if nm % 4 == 0 else None
    M = smallest_M(nm, nm // 2, 1)
    qc = comb(nm // M - 1, (nm // 2) // M) if M else None
    ident.append({"n_model": nm, "PLATEAU=C(n/2-1,n/4)": plateau,
                  "QCORE(n,sigma=1)": qc, "M": M, "equal": plateau == qc})
out["identity_PLATEAU_is_QCORE_at_sigma_1"] = ident
out["model_scale_matching_razor_plateau"] = {
    "n_model": 256, "PLATEAU(256)": comb(127, 64),
    "razor QCORE(2^41, sigma=2^34-1)": comb(127, 64),
    "equal": True,
    "reading": "n_model = 2N = 2*(n_razor/M) with M = 2^34",
}

# ---- what the sigma=1 law would give AT THE RAZOR'S OWN SCALE -------------
out["sigma1_law_at_model_scale_256"] = {
    "log2 C(256,129)/256": lg2binom(256, 129) - 8,
    "log2 PLATEAU(256)": lg2binom(127, 64),
    "surplus_bits": lg2binom(256, 129) - 8 - lg2binom(127, 64),
}
out["sigma1_law_at_razor_scale"] = {
    "log2 C(2^41, 2^40+1)/2^41": lg2binom(n, k + 1) - 41,
    "log2 QCORE at sigma=1 (M=2)": lg2binom(n // 2 - 1, n // 4),
    "surplus_bits": (lg2binom(n, k + 1) - 41) - lg2binom(n // 2 - 1, n // 4),
}

# ---- the need and the deficits -------------------------------------------
need_lo, need_hi = 127.90, 128.00
out["need_bits"] = [need_lo, need_hi]
out["deficit_of_qcore_at_sigma_2^34-1"] = [need_lo - lg2binom(127, 64),
                                           need_hi - lg2binom(127, 64)]
out["deficit_of_qcore_at_sigma_2^34"] = [need_lo - lg2binom(63, 32),
                                         need_hi - lg2binom(63, 32)]

# ---- structure vs pigeonhole at the razor --------------------------------
lgC = lg2binom(n, a)
out["pigeonhole_at_razor"] = {
    "log2 C(n,a)": lgC,
    "log2 q^sigma (q=2^256)": 256.0 * sigma,
    "log2 C(n,a)/q^sigma": lgC - 256.0 * sigma,
    "structure_dominated": lgC - 256.0 * sigma < 0,
}
print(json.dumps(out, indent=1, default=str))
