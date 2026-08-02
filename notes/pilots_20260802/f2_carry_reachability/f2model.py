#!/usr/bin/env python3
"""Exact F_{p^2} arithmetic and the F2 first-descent carry model.

Work package F2A.2 (carry reachability audit), pilot 2026-08-02.

MODEL (see REPORT.md sec. 1 for provenance and assumptions).

Ambient: p an odd prime, F_{p^2} = F_p(w) with w^2 = N a fixed quadratic
non-residue.  Frobenius is (a + b w) -> (a - b w).  psi(z) = e_p(Tr(z)),
Tr(a + b w) = 2a.

mu_n <= F_{p^2}^*, n | p^2 - 1, n even, n does not divide p - 1 (so the
subgroup genuinely leaves F_p).

For a frequency c in F_{p^2}^* and x in mu_n:

    s_c(x) = least residue of Tr(c x) in [0, p),
    1 + psi(c x) = 2 cos(pi s_c(x) / p) * exp(i pi s_c(x) / p).

Hence  prod_{x in mu_n} (1 + psi(c x)) = (-1)^{K + U} prod 2|cos(pi s/p)|
with K = (sum_x s_c(x)) / p (an integer, because sum_{x in mu_n} x = 0
for n > 1) and U = #{x : s_c(x) > p/2}.  (-1)^K depends only on
(sum_x s_c(x)) mod 2p: it is h_p(r) = +1 if r < p else -1.

FIRST-DESCENT ABSTRACTION.  mu_n splits into Frobenius-fixed elements
(mu_{gcd(n, p-1)} <= F_p) and m = (n - gcd(n, p-1))/2 genuine conjugate
PAIRS {y, y^p}.  The descent turns each pair into a free ORIENTATION
variable tau_i in {+1, -1} selecting one element of the pair; the local
residue is s_i(tau).  The carry parity of an orientation vector is
h_p( sum_i s_i(tau_i)  mod 2p ), so the whole carry question is the
reachability structure of the partial sums, i.e. of the sumsets of the
per-pair DIFFERENCES delta_i = s_i(+1) - s_i(-1) mod 2p.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Iterable, Sequence

# ---------------------------------------------------------------- field ---


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % q == 0:
            return m == q
    d = m - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def factorize(m: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= m:
        while m % d == 0:
            out[d] = out.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        out[m] = out.get(m, 0) + 1
    return out


_FACT_CACHE: dict[int, dict[int, int]] = {}
_GEN_CACHE: dict[tuple[int, int], tuple[int, int]] = {}


def _factor_cache(m: int) -> dict[int, int]:
    if m not in _FACT_CACHE:
        _FACT_CACHE[m] = factorize(m)
    return _FACT_CACHE[m]


def divisors(m: int) -> list[int]:
    f = factorize(m)
    out = [1]
    for q, e in f.items():
        out = [d * q**i for d in out for i in range(e + 1)]
    return sorted(out)


def nonresidue(p: int) -> int:
    """Smallest quadratic non-residue mod p."""
    for a in range(2, p):
        if pow(a, (p - 1) // 2, p) == p - 1:
            return a
    raise ValueError(f"no non-residue for p={p}")


@dataclass(frozen=True)
class Fp2:
    """The field F_{p^2} = F_p(w), w^2 = N."""

    p: int
    N: int = field(default=0)

    @staticmethod
    def make(p: int) -> "Fp2":
        return Fp2(p, nonresidue(p))

    def mul(self, x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
        p, N = self.p, self.N
        a1, b1 = x
        a2, b2 = y
        return ((a1 * a2 + N * b1 * b2) % p, (a1 * b2 + a2 * b1) % p)

    def pow(self, x: tuple[int, int], e: int) -> tuple[int, int]:
        r = (1, 0)
        b = x
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def frob(self, x: tuple[int, int]) -> tuple[int, int]:
        return (x[0], (-x[1]) % self.p)

    def trace(self, x: tuple[int, int]) -> int:
        return (2 * x[0]) % self.p

    def norm(self, x: tuple[int, int]) -> int:
        return (x[0] * x[0] - self.N * x[1] * x[1]) % self.p

    def order(self, x: tuple[int, int]) -> int:
        o = self.p * self.p - 1
        for q in _factor_cache(o):
            while o % q == 0 and self.pow(x, o // q) == (1, 0):
                o //= q
        return o

    def generator(self) -> tuple[int, int]:
        key = (self.p, self.N)
        if key in _GEN_CACHE:
            return _GEN_CACHE[key]
        target = self.p * self.p - 1
        primes = list(_factor_cache(target))
        for a in range(self.p):
            for b in range(self.p):
                if (a, b) == (0, 0):
                    continue
                x = (a, b)
                if all(self.pow(x, target // q) != (1, 0) for q in primes):
                    _GEN_CACHE[key] = x
                    return x
        raise ValueError("no generator found")

    def subgroup(self, n: int) -> list[tuple[int, int]]:
        """The unique subgroup mu_n of order n (n | p^2 - 1), as a list."""
        order = self.p * self.p - 1
        if order % n:
            raise ValueError(f"{n} does not divide p^2-1={order}")
        g = self.pow(self.generator(), order // n)
        out = []
        cur = (1, 0)
        for _ in range(n):
            out.append(cur)
            cur = self.mul(cur, g)
        assert cur == (1, 0)
        return out


# ------------------------------------------------------------ the model ---


def pair_reps(F: Fp2, mu: Sequence[tuple[int, int]]) -> list[tuple[int, int]]:
    """One representative per genuine conjugate pair.

    Convention: the representative with w-component in [1, (p-1)/2].
    (Flipping the convention on any subset of pairs translates the
    difference sumset; it never changes its cardinality.)
    """
    half = (F.p - 1) // 2
    return [y for y in mu if 1 <= y[1] <= half]


def residues(F: Fp2, c: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    """(s(+1), s(-1)) = least residues of Tr(c y), Tr(c y^p)."""
    p, N = F.p, F.N
    ac, bc = c
    ay, by = y
    s_plus = (2 * (ac * ay + N * bc * by)) % p
    s_minus = (2 * (ac * ay - N * bc * by)) % p
    return s_plus, s_minus


def deltas(F: Fp2, c: tuple[int, int],
           reps: Sequence[tuple[int, int]]) -> list[int]:
    """delta_i = s_i(+1) - s_i(-1) mod 2p, one per conjugate pair."""
    two_p = 2 * F.p
    out = []
    for y in reps:
        sp, sm = residues(F, c, y)
        out.append((sp - sm) % two_p)
    return out


def carry_sign(p: int, r: int) -> int:
    return 1 if r % (2 * p) < p else -1


# ------------------------------------------------------------- sumsets ----


def rot(mask: int, d: int, width: int, full: int) -> int:
    d %= width
    if d == 0:
        return mask
    return ((mask << d) | (mask >> (width - d))) & full


def sumset_curve(ds: Sequence[int], two_p: int,
                 max_k: int | None = None) -> tuple[list[int], int, int]:
    """Return (sizes, terminal_mask, k_terminal).

    sizes[k] = |S_k|, S_k = { sum over any subset of {d_1..d_k} } mod 2p,
    S_0 = {0}.  Exact integer arithmetic (bitmask over Z/2p).
    """
    full = (1 << two_p) - 1
    S = 1  # {0}
    sizes = [1]
    target_g = math.gcd(two_p, *ds) if ds else two_p
    target_size = two_p // target_g
    k_term = 0
    for k, d in enumerate(ds, start=1):
        S |= rot(S, d, two_p, full)
        sz = S.bit_count()
        sizes.append(sz)
        if sz == target_size and k_term == 0:
            k_term = k
        if max_k is not None and k >= max_k and sz == target_size:
            break
        if sz == target_size and k >= 2 * target_size:
            break
    return sizes, S, k_term


def suffix_sumsets(ds: Sequence[int], two_p: int) -> list[int]:
    """C[k] = bitmask of { sum over any subset of {d_{k+1}..d_m} } mod 2p."""
    full = (1 << two_p) - 1
    m = len(ds)
    C = [0] * (m + 1)
    S = 1
    C[m] = S
    for k in range(m - 1, -1, -1):
        S |= rot(S, ds[k], two_p, full)
        C[k] = S
    return C


def carry_mask(p: int) -> int:
    """Bit r of the returned mask is 1 iff h_p(r) = +1, r in [0, 2p)."""
    return (1 << p) - 1


def myhill_nerode_classes(p: int, prefix_mask: int, suffix_mask: int) -> int:
    """#distinct carry behaviours among reachable prefix states.

    Two reachable partial sums r, r' merge iff h_p(r+t) = h_p(r'+t) for
    every REACHABLE continuation t.  This is the exact minimal state count
    of the carry automaton at that cut.
    """
    two_p = 2 * p
    full = (1 << two_p) - 1
    H = carry_mask(p)
    sigs = set()
    r = 0
    mask = prefix_mask
    while mask:
        low = mask & -mask
        r = low.bit_length() - 1
        mask ^= low
        # bit t of rot(H, -r) is h(r + t)
        sigs.add(rot(H, two_p - (r % two_p), two_p, full) & suffix_mask)
    return len(sigs)


def describe_structure(S: int, two_p: int) -> dict:
    """Exactly classify the terminal reachable set S <= Z/2p."""
    elems = [i for i in range(two_p) if (S >> i) & 1]
    size = len(elems)
    g = math.gcd(two_p, *elems) if elems else two_p
    subgroup = [i for i in range(0, two_p, g)]
    is_subgroup = size == len(subgroup) and all((S >> i) & 1 for i in subgroup)
    return {
        "size": size,
        "index": two_p // size if two_p % size == 0 else None,
        "generated_subgroup_order": two_p // g,
        "generated_subgroup_gen": g,
        "is_subgroup": bool(is_subgroup),
        "is_full": size == two_p,
        "elements": elems if size <= 32 else None,
    }


# ------------------------------------------------- carry DFT / contraction --


def carry_dft_abs(p: int) -> list[float]:
    """|hhat_p(k)| for k in [0, 2p): 0 (k even), 2/|sin(pi k /(2p))| (odd)."""
    two_p = 2 * p
    out = []
    for k in range(two_p):
        if k % 2 == 0:
            out.append(0.0)
        else:
            out.append(2.0 / abs(math.sin(math.pi * k / two_p)))
    return out


def carry_dft_l1_normalized(p: int) -> float:
    """sum_k |hhat_p(k)| / (2p) -- display-only float."""
    return sum(carry_dft_abs(p)) / (2 * p)


def local_balance(p: int, sp: int, sm: int) -> float:
    """4ab/(a+b)^2 with a = 2|cos(pi s+/p)|, b = 2|cos(pi s-/p)|."""
    a = 2.0 * abs(math.cos(math.pi * sp / p))
    b = 2.0 * abs(math.cos(math.pi * sm / p))
    if a + b == 0.0:
        return 0.0
    return 4.0 * a * b / (a + b) ** 2


def half_flag(p: int, s: int) -> int:
    """u = [s > p/2] -- the U_c indicator for one term."""
    return 1 if 2 * s > p else 0
