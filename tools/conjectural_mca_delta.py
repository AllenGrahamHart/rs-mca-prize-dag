#!/usr/bin/env python3
"""Conjectural grand-MCA delta map.

This is a row-level implementation of the speculative map discussed in the
critical-DAG program:

    C = RS[F, L, k]  |F| = q, |L| = n  ->  delta_C^*

The output is conditional, not a proof artifact.  It assumes the remaining
critical DAG leaves needed by mca_safe / adjacency_closing / mca_grand close in
their CURRENT re-posed form.  Under those assumptions, the adjacent certificate is

    B_C(a* - 1) > floor(q / 2^128) >= B_C(a*)

and the reported delta is (n - a*) / n.  The adjacent unsafe delta obtained by
adding one to the numerator is also printed.

Status note (2026-07-05): two leaf statements were re-posed after this tool was
first written -- dli (sup formulation refuted; now the U-weighted-average / RES
count) and the petal gates N/D/L (mid-stabilization; primitive-coordinate
foundation out for definition).  These re-posings change the PROOF ROUTE, not the
B_C counting bound this tool evaluates, so the delta VALUES here are unaffected;
only the "close as stated" wording needed updating to "close in re-posed form".

The computation is intentionally lightweight: it uses a monotone binary search
and log-gamma evaluations, with no large binomial materialization.
"""

from __future__ import annotations

import argparse
import json
import math
from collections.abc import Mapping
from dataclasses import dataclass
from fractions import Fraction
from typing import Any


EPS_BITS = 128
FIELD_BITS_CAP = 256
MAX_K = 1 << 40
SUPPORTED_RATES = {
    Fraction(1, 2),
    Fraction(1, 4),
    Fraction(1, 8),
    Fraction(1, 16),
}
LN2 = math.log(2.0)


def parse_int(text: str) -> int:
    """Parse decimal or Python-style base-prefixed integers."""
    try:
        value = int(text, 0)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid integer: {text!r}") from exc
    if value < 0:
        raise argparse.ArgumentTypeError("integer must be nonnegative")
    return value


def parse_rate(text: str) -> Fraction:
    try:
        rate = Fraction(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"invalid rate: {text!r}") from exc
    if rate <= 0 or rate >= 1:
        raise argparse.ArgumentTypeError("rate must lie strictly between 0 and 1")
    return rate


def is_power_of_two(value: int) -> bool:
    return value > 0 and (value & (value - 1)) == 0


def log2_binom_lgamma(n: int, r: int) -> float:
    if r < 0 or r > n:
        return float("-inf")
    r = min(r, n - r)
    if r == 0:
        return 0.0
    return (math.lgamma(n + 1) - math.lgamma(r + 1) - math.lgamma(n - r + 1)) / LN2


def margin_bits(n: int, k: int, t: int, log2_q: float) -> float:
    """Positive means the t-excess point is on the safe side of the bound."""
    return t * log2_q - log2_binom_lgamma(n, n - k - t) - EPS_BITS


def corridor_edge(n: int, k: int, log2_q: float) -> int:
    """Smallest t >= 1 satisfying the conjectural MCA safe inequality."""
    max_t = n - k
    if max_t < 1:
        raise ValueError("need k < n")
    if margin_bits(n, k, max_t, log2_q) < 0:
        raise ValueError(
            "no crossing before full agreement; field is too small for this row"
        )

    lo, hi = 1, max_t
    while lo < hi:
        mid = (lo + hi) // 2
        if margin_bits(n, k, mid, log2_q) >= 0:
            hi = mid
        else:
            lo = mid + 1
    return lo


def q_max_admissible(bits: int, n: int) -> int:
    """Largest integer q < 2^bits with q == 1 mod n.

    This only enforces the subgroup divisibility arithmetic.  It is not a
    certificate that q is a prime power.
    """
    if bits <= 0:
        raise ValueError("bits must be positive")
    return 1 + n * (((1 << bits) - 2) // n)


def rate_label(rate: Fraction) -> str:
    return f"{rate.numerator}/{rate.denominator}"


def branch_for_rate(rate: Fraction) -> str:
    if rate == Fraction(1, 2):
        return "rate_half_conjectural_band"
    return "clean_rate_conjectural_corridor"


def assumptions_for_rate(rate: Fraction) -> list[str]:
    assumptions = [
        # 2026-07-05: dli sup REFUTED -> re-posed to U-weighted-average/RES count
        # (same B_C bound); petal gates N/D/L mid-stabilization (primitive-coordinate
        # foundation out for definition). These change proof route, not delta value.
        "critical_8_open_nodes_close_in_current_reposed_form_2026_07_05",
        "dli_weighted_average_RES_count_holds",
        "petal_gates_N_D_L_close_via_primitive_coordinate_foundation",
        "mca_safe_conditional_chain_sound",
        "adjacency_closing_conditional_chain_sound",
        "crossing_localization_monotonicity_integrality_applies",
    ]
    if rate == Fraction(1, 2):
        assumptions.append("rate_half_band_closure_closes_as_stated")
    else:
        assumptions.append("clean_rate_corridor_closes_as_stated")
    return assumptions


@dataclass(frozen=True)
class CodeRow:
    """A row abstraction for C = RS[F, L, k]."""

    n: int
    k: int
    q: int | None = None
    log2_q_override: float | None = None
    q_source: str = "exact"

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "CodeRow":
        q_raw = data.get("q")
        q = None if q_raw is None else int(q_raw)
        log2_q_raw = data.get("log2_q")
        log2_q = None if log2_q_raw is None else float(log2_q_raw)
        return cls(
            n=int(data["n"]),
            k=int(data["k"]),
            q=q,
            log2_q_override=log2_q,
            q_source=str(data.get("q_source", "mapping")),
        )

    @property
    def log2_q(self) -> float:
        if self.log2_q_override is not None:
            return self.log2_q_override
        if self.q is None:
            raise ValueError("row needs either q or log2_q")
        return math.log2(self.q)

    @property
    def b_star(self) -> int | None:
        if self.q is None:
            return None
        return self.q // (1 << EPS_BITS)


@dataclass(frozen=True)
class DeltaCertificate:
    row: CodeRow
    rate: Fraction
    a_star: int
    safe_excess_t: int
    safe_margin_bits: float
    unsafe_margin_bits: float
    branch: str
    assumptions: list[str]
    warnings: list[str]

    @property
    def delta_num(self) -> int:
        return self.row.n - self.a_star

    @property
    def delta_den(self) -> int:
        return self.row.n

    @property
    def unsafe_delta_num(self) -> int:
        return self.delta_num + 1

    @property
    def unsafe_agreement(self) -> int:
        return self.a_star - 1

    def adjacent_check_errors(self) -> list[str]:
        errors: list[str] = []
        if self.safe_margin_bits < 0:
            errors.append(
                "safe point failed: expected margin(a_star) >= 0, "
                f"got {self.safe_margin_bits}"
            )
        if self.unsafe_margin_bits >= 0:
            errors.append(
                "adjacent unsafe point failed: expected margin(a_star - 1) < 0, "
                f"got {self.unsafe_margin_bits}"
            )
        return errors

    def to_json_dict(self) -> dict[str, Any]:
        q_decimal = None if self.row.q is None else str(self.row.q)
        b_star_decimal = None if self.row.b_star is None else str(self.row.b_star)
        adjacent_errors = self.adjacent_check_errors()
        return {
            "status": "CONJECTURAL_CONDITIONAL_ON_CRITICAL_DAG",
            "criterion": "B_C(a_star - 1) > floor(q/2^128) >= B_C(a_star)",
            "input": {
                "q_decimal": q_decimal,
                "q_source": self.row.q_source,
                "n": self.row.n,
                "k": self.row.k,
                "rate": rate_label(self.rate),
                "log2_q_used": self.row.log2_q,
                "B_star_floor_q_over_2^128": b_star_decimal,
            },
            "output": {
                "delta_fraction": f"{self.delta_num}/{self.delta_den}",
                "delta_num": self.delta_num,
                "delta_den": self.delta_den,
                "delta_decimal": self.delta_num / self.delta_den,
                "a_star": self.a_star,
                "safe_excess_t": self.safe_excess_t,
                "safe_agreement": self.a_star,
                "unsafe_after_adding_one_to_delta_numerator": {
                    "delta_fraction": f"{self.unsafe_delta_num}/{self.delta_den}",
                    "delta_num": self.unsafe_delta_num,
                    "delta_den": self.delta_den,
                    "delta_decimal": self.unsafe_delta_num / self.delta_den,
                    "agreement": self.unsafe_agreement,
                    "unsafe_excess_t": self.safe_excess_t - 1,
                },
            },
            "comparison_margins_bits": {
                "safe_point_margin": self.safe_margin_bits,
                "adjacent_unsafe_point_margin": self.unsafe_margin_bits,
                "sign_convention": "safe iff margin >= 0",
            },
            "adjacent_self_consistency_check": {
                "passed": not adjacent_errors,
                "safe_agreement_margin_nonnegative": self.safe_margin_bits >= 0,
                "adjacent_lower_agreement_margin_negative": self.unsafe_margin_bits < 0,
                "errors": adjacent_errors,
            },
            "branch": self.branch,
            "assumptions": self.assumptions,
            "warnings": self.warnings,
            "precision": "float_lgamma_log_binomial; not a formal integer certificate",
        }


def validate_row(row: CodeRow, *, strict_admissible: bool) -> tuple[Fraction, list[str]]:
    warnings: list[str] = []
    if row.n <= 0:
        raise ValueError("n must be positive")
    if row.k <= 0:
        raise ValueError("k must be positive")
    if row.q is not None and row.q <= 0:
        raise ValueError("q must be positive")
    if row.k >= row.n:
        raise ValueError("need k < n")
    if not is_power_of_two(row.n):
        raise ValueError("official smooth rows require n to be a power of two")

    rate = Fraction(row.k, row.n)
    if rate not in SUPPORTED_RATES:
        allowed = ", ".join(rate_label(r) for r in sorted(SUPPORTED_RATES))
        raise ValueError(f"rate {rate_label(rate)} is not in {{{allowed}}}")
    if row.k > MAX_K:
        raise ValueError(f"k={row.k} exceeds official cap 2^40")

    if row.log2_q <= EPS_BITS:
        raise ValueError("log2(q) must exceed 128 for a nonzero B* threshold")

    if row.q is None:
        warnings.append(
            "log2_q mode: B*=floor(q/2^128) and field admissibility are not exact"
        )
    else:
        if row.q >= (1 << FIELD_BITS_CAP):
            message = "official rows require q < 2^256"
            if strict_admissible:
                raise ValueError(message)
            warnings.append(message)
        if (row.q - 1) % row.n != 0:
            message = "q-1 is not divisible by n, so the multiplicative subgroup row is not certified"
            if strict_admissible:
                raise ValueError(message)
            warnings.append(message)
        if row.b_star == 0:
            raise ValueError("B*=floor(q/2^128) is zero")

    if row.q_source.startswith("q_max_admissible"):
        warnings.append(
            "q_max_admissible enforces q == 1 mod n but does not certify q is a prime power"
        )

    return rate, warnings


def f_conj(
    C: CodeRow | Mapping[str, Any],
    *,
    strict_admissible: bool = False,
) -> DeltaCertificate:
    """Return the conjectural maximal safe delta certificate for one row."""
    row = C if isinstance(C, CodeRow) else CodeRow.from_mapping(C)
    rate, warnings = validate_row(row, strict_admissible=strict_admissible)
    t_star = corridor_edge(row.n, row.k, row.log2_q)
    a_star = row.k + t_star
    return DeltaCertificate(
        row=row,
        rate=rate,
        a_star=a_star,
        safe_excess_t=t_star,
        safe_margin_bits=margin_bits(row.n, row.k, t_star, row.log2_q),
        unsafe_margin_bits=margin_bits(row.n, row.k, t_star - 1, row.log2_q),
        branch=branch_for_rate(rate),
        assumptions=assumptions_for_rate(rate),
        warnings=warnings,
    )


def build_row_from_args(args: argparse.Namespace) -> CodeRow:
    if (args.n is None) == (args.n_exp is None):
        raise SystemExit("provide exactly one of --n or --n-exp")
    if args.n_exp is not None and args.n_exp < 0:
        raise SystemExit("--n-exp must be nonnegative")
    n = args.n if args.n is not None else 1 << args.n_exp

    if args.k is None and args.rate is None:
        raise SystemExit("provide --k or --rate")
    if args.rate is not None:
        k_from_rate = n * args.rate.numerator // args.rate.denominator
        if k_from_rate * args.rate.denominator != n * args.rate.numerator:
            raise SystemExit("--rate does not give an integral k for this n")
        if args.k is not None and args.k != k_from_rate:
            raise SystemExit("--k and --rate disagree")
        k = k_from_rate
    else:
        k = args.k

    q_sources = [
        args.q is not None,
        args.q_pow2_minus_one is not None,
        args.q_max_admissible_bits is not None,
        args.log2_q is not None,
    ]
    if sum(q_sources) != 1:
        raise SystemExit(
            "provide exactly one of --q, --q-pow2-minus-one, "
            "--q-max-admissible-bits, or --log2-q"
        )

    if args.q is not None:
        return CodeRow(n=n, k=k, q=args.q, q_source="exact")
    if args.q_pow2_minus_one is not None:
        bits = args.q_pow2_minus_one
        if bits <= 0:
            raise SystemExit("--q-pow2-minus-one must be positive")
        return CodeRow(n=n, k=k, q=(1 << bits) - 1, q_source=f"2^{bits}-1")
    if args.q_max_admissible_bits is not None:
        bits = args.q_max_admissible_bits
        if bits <= 0:
            raise SystemExit("--q-max-admissible-bits must be positive")
        return CodeRow(
            n=n,
            k=k,
            q=q_max_admissible(bits, n),
            q_source=f"q_max_admissible_{bits}_bits",
        )
    return CodeRow(
        n=n,
        k=k,
        log2_q_override=args.log2_q,
        q_source=f"log2_q={args.log2_q}",
    )


def run_self_test() -> None:
    n = 1 << 41
    log2_q = 255.9
    targets = {
        Fraction(1, 2): 8592912739,
        Fraction(1, 4): 7014660390,
        Fraction(1, 8): 4722556392,
        Fraction(1, 16): 2943177800,
    }
    print("self-test: corridor edge t* at log2_q=255.9, n=2^41")
    ok = True
    for rate, expected in targets.items():
        row = CodeRow(
            n=n,
            k=n * rate.numerator // rate.denominator,
            log2_q_override=log2_q,
            q_source="self_test_log2_q",
        )
        cert = f_conj(row)
        got = cert.safe_excess_t
        match = got == expected
        adjacent_ok = not cert.adjacent_check_errors()
        ok &= match and adjacent_ok
        print(
            f"  rate {rate_label(rate):>4}: t*={got} "
            f"expected={expected} match={match} adjacent_ok={adjacent_ok}"
        )
    if not ok:
        raise SystemExit(1)
    print("ALL PASS")


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compute the conjectural grand-MCA delta threshold for one row."
    )
    parser.add_argument("--n", type=parse_int, help="evaluation length |L|")
    parser.add_argument("--n-exp", type=int, help="set n = 2^N_EXP")
    parser.add_argument("--k", type=parse_int, help="dimension k")
    parser.add_argument("--rate", type=parse_rate, help="one of 1/2, 1/4, 1/8, 1/16")
    parser.add_argument("--q", type=parse_int, help="exact field size q")
    parser.add_argument(
        "--q-pow2-minus-one",
        type=int,
        metavar="BITS",
        help="set q = 2^BITS - 1",
    )
    parser.add_argument(
        "--q-max-admissible-bits",
        type=int,
        metavar="BITS",
        help="set q to the largest integer < 2^BITS with q == 1 mod n",
    )
    parser.add_argument(
        "--log2-q",
        type=float,
        help="log-only model; skips exact B* and subgroup checks",
    )
    parser.add_argument(
        "--strict-admissible",
        action="store_true",
        help="turn admissibility warnings into errors where possible",
    )
    parser.add_argument(
        "--verify-adjacent",
        action="store_true",
        help="exit nonzero unless a_star is safe and a_star-1 is unsafe",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="reproduce the banked n=2^41, log2(q)=255.9 corridor table",
    )
    return parser


def main() -> None:
    parser = make_parser()
    args = parser.parse_args()
    if args.self_test:
        run_self_test()
        return
    row = build_row_from_args(args)
    cert = f_conj(row, strict_admissible=args.strict_admissible)
    adjacent_errors = cert.adjacent_check_errors()
    if args.verify_adjacent and adjacent_errors:
        for error in adjacent_errors:
            print(f"adjacent verification failed: {error}")
        raise SystemExit(1)
    print(json.dumps(cert.to_json_dict(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
