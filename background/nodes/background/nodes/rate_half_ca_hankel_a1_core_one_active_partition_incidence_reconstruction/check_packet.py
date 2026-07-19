#!/usr/bin/env python3
"""Check a bounded prime-field active-partition packet for CR-003 pilots."""

import argparse
import hashlib
import json
from collections import deque
from pathlib import Path


class PacketError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise PacketError(message)


def canonical_hash(packet):
    raw = json.dumps(packet, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def field_values(values, p, label):
    require(all(isinstance(v, int) for v in values), f"{label}: noninteger value")
    require(all(0 <= v < p for v in values), f"{label}: value outside [0,p)")
    require(len(set(values)) == len(values), f"{label}: repeated value")


def monic_locator(roots, p):
    coeffs = [1]
    for root in roots:
        nxt = [0] * (len(coeffs) + 1)
        for i, value in enumerate(coeffs):
            nxt[i] = (nxt[i] - root * value) % p
            nxt[i + 1] = (nxt[i + 1] + value) % p
        coeffs = nxt
    return coeffs


def poly_eval(coeffs, value, p):
    out = 0
    for coeff in reversed(coeffs):
        out = (out * value + coeff) % p
    return out


def poly_mul(left, right, p):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return out


def interpolate(xs, ys, p):
    result = [0] * len(xs)
    for i, (x_i, y_i) in enumerate(zip(xs, ys)):
        basis = [1]
        denom = 1
        for j, x_j in enumerate(xs):
            if i == j:
                continue
            basis = poly_mul(basis, [(-x_j) % p, 1], p)
            denom = denom * (x_i - x_j) % p
        scale = y_i * pow(denom, -1, p) % p
        for j, value in enumerate(basis):
            result[j] = (result[j] + scale * value) % p
    return result


def matrix_rank(matrix, p):
    require(matrix and matrix[0], "rank: empty matrix")
    work = [row[:] for row in matrix]
    rank = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(rank, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], -1, p)
        work[rank] = [value * inv % p for value in work[rank]]
        for i in range(len(work)):
            if i == rank or not work[i][col]:
                continue
            factor = work[i][col]
            work[i] = [
                (left - factor * right) % p
                for left, right in zip(work[i], work[rank])
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def parse_fibers(packet, p, e_star, r):
    clean = packet.get("clean_fibers")
    saturated = packet.get("saturated_fibers")
    require(isinstance(clean, list) and clean, "clean_fibers: missing or empty")
    require(
        isinstance(saturated, list) and saturated,
        "saturated_fibers: missing or empty",
    )

    slopes = [entry.get("slope") for entry in clean]
    rows = [entry.get("row") for entry in saturated]
    field_values(slopes, p, "clean slopes")
    field_values(rows, p, "saturated rows")

    clean_roots = []
    for index, entry in enumerate(clean):
        roots = entry.get("roots")
        require(isinstance(roots, list), f"clean fiber {index}: roots missing")
        field_values(roots, p, f"clean fiber {index} roots")
        require(len(roots) == r, f"clean fiber {index}: expected {r} roots")
        clean_roots.append(roots)

    saturated_roots = []
    for index, entry in enumerate(saturated):
        roots = entry.get("roots")
        require(isinstance(roots, list), f"saturated fiber {index}: roots missing")
        field_values(roots, p, f"saturated fiber {index} roots")
        require(
            len(roots) == e_star,
            f"saturated fiber {index}: expected {e_star} roots",
        )
        saturated_roots.append(roots)

    return slopes, rows, clean_roots, saturated_roots


def recover_potentials(slopes, rows, clean_roots, saturated_roots, p):
    clean_locators = [monic_locator(roots, p) for roots in clean_roots]
    saturated_locators = [monic_locator(roots, p) for roots in saturated_roots]
    row_sets = [set(roots) for roots in saturated_roots]
    clean_sets = [set(roots) for roots in clean_roots]

    adj_clean = [[] for _ in slopes]
    adj_row = [[] for _ in rows]
    edge_count = 0
    for x_index, row in enumerate(rows):
        for g_index, slope in enumerate(slopes):
            from_clean = row in clean_sets[g_index]
            from_row = slope in row_sets[x_index]
            require(
                from_clean == from_row,
                f"incidence mismatch at row={row}, slope={slope}",
            )
            if from_clean:
                continue
            f_value = poly_eval(clean_locators[g_index], row, p)
            g_value = poly_eval(saturated_locators[x_index], slope, p)
            require(f_value and g_value, "nonincidence edge has zero locator value")
            theta = f_value * pow(g_value, -1, p) % p
            adj_clean[g_index].append((x_index, theta))
            adj_row[x_index].append((g_index, theta))
            edge_count += 1

    a = [None] * len(slopes)
    b_values = [None] * len(rows)
    a[0] = 1
    queue = deque([("clean", 0)])
    while queue:
        side, index = queue.popleft()
        if side == "clean":
            for x_index, theta in adj_clean[index]:
                candidate = theta * a[index] % p
                if b_values[x_index] is None:
                    b_values[x_index] = candidate
                    queue.append(("row", x_index))
                elif b_values[x_index] != candidate:
                    raise PacketError(
                        f"cycle mismatch at row={rows[x_index]}, slope={slopes[index]}"
                    )
        else:
            for g_index, theta in adj_row[index]:
                candidate = b_values[index] * pow(theta, -1, p) % p
                if a[g_index] is None:
                    a[g_index] = candidate
                    queue.append(("clean", g_index))
                elif a[g_index] != candidate:
                    raise PacketError(
                        f"cycle mismatch at row={rows[index]}, slope={slopes[g_index]}"
                    )

    require(all(value is not None for value in a), "nonincidence graph disconnected")
    require(
        all(value is not None for value in b_values),
        "nonincidence graph disconnected",
    )
    return clean_locators, saturated_locators, a, b_values, edge_count


def check_packet(packet):
    require(isinstance(packet, dict), "packet must be a JSON object")
    p = packet.get("p")
    e = packet.get("e")
    b = packet.get("b")
    e_star = packet.get("e_star")
    r = packet.get("r")
    require(isinstance(p, int) and p > 2 and p % 2, "p must be an odd integer")
    require(all(isinstance(v, int) for v in (e, b, e_star, r)), "bad degree data")
    require(e > 0 and b >= 0, "expected e>0 and b>=0")
    require(e_star == e - b and e_star > 0, "expected e_star=e-b>0")
    require(r == 2 * e_star + 1, "expected r=2e_star+1")

    slopes, rows, clean_roots, saturated_roots = parse_fibers(
        packet, p, e_star, r
    )
    require(len(slopes) > 2 * e_star, "need #clean slopes > 2e_star")
    require(len(rows) > 2 * r, "need #saturated rows > 2r")

    clean_locators, saturated_locators, a, b_values, edge_count = recover_potentials(
        slopes, rows, clean_roots, saturated_roots, p
    )

    clean_coefficients = [
        [scale * value % p for value in locator]
        for scale, locator in zip(a, clean_locators)
    ]
    basis_slopes = slopes[: e_star + 1]
    for degree in range(r + 1):
        values = [row[degree] for row in clean_coefficients]
        polynomial = interpolate(basis_slopes, values[: e_star + 1], p)
        require(
            all(poly_eval(polynomial, slope, p) == value for slope, value in zip(slopes, values)),
            f"RS parity failure in X coefficient {degree}",
        )

    saturated_coefficients = [
        [scale * value % p for value in locator]
        for scale, locator in zip(b_values, saturated_locators)
    ]
    value_matrix = [
        [
            a[g_index] * poly_eval(clean_locators[g_index], row, p) % p
            for g_index in range(len(slopes))
        ]
        for row in rows
    ]
    ranks = {
        "clean_locator": matrix_rank(clean_coefficients, p),
        "saturated_locator": matrix_rank(saturated_coefficients, p),
        "core_value": matrix_rank(value_matrix, p),
    }
    require(len(set(ranks.values())) == 1, f"rank mismatch: {ranks}")
    rank = ranks["core_value"]
    lower = (e + 1 + b) // (b + 1)
    require(rank >= lower, f"separation rank {rank} below lower bound {lower}")
    if b == 0:
        require(rank == e + 1, f"b=0 requires separation rank {e + 1}")
    expected = packet.get("expected_separation_rank")
    if expected is not None:
        require(isinstance(expected, int), "expected separation rank must be integer")
        require(rank == expected, f"expected separation rank {expected}, got {rank}")

    return {
        "status": "PASS",
        "packet_sha256": canonical_hash(packet),
        "p": p,
        "clean_slopes": len(slopes),
        "saturated_rows": len(rows),
        "nonincidence_edges": edge_count,
        "rs_checks": r + 1,
        "separation_rank": rank,
        "rank_lower_bound": lower,
        "ranks": ranks,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("packet", type=Path)
    args = parser.parse_args()
    try:
        packet = json.loads(args.packet.read_text())
        result = check_packet(packet)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}, sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
