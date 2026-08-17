#!/usr/bin/env python3
"""String compiler for cached O0b split cells-3/6 outside ideals."""


PRIME = 2130706433
EDGE_SPECS = {
    "S0": (
        (0, 3, 1), (1, 4, 1),
        (2, 3, 1), (2, 3, -1),
        (2, 4, 1), (2, 4, -1),
        (3, 4, 0),
    ),
    "SDE": (
        (0, 3, 1), (1, 4, 1),
        (2, 3, 1), (2, 3, 1),
        (2, 4, 1), (2, 4, -1),
        (3, 4, 0),
    ),
    "SDF": (
        (0, 3, 1), (1, 4, 1),
        (2, 3, 1), (2, 3, -1),
        (2, 4, 1), (2, 4, 1),
        (3, 4, 0),
    ),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


def edge(left, right, sign):
    require(sign in (-1, 1), "edge sign")
    product = f"{left}*{right}" if sign == 1 else f"-{left}*{right}"
    squared_sum = f"({left}+{right})^2" if sign == 1 else f"({left}-{right})^2"
    return product, squared_sum


def evaluate_kernel(names, label):
    return f"({names[0]})+({names[1]})*({label})+({names[2]})*({label})^2"


def compile_case(case, packet):
    cell, lane, sigma_o, epsilon_1, epsilon_2, xi_index, pairing_index = case
    require(cell == 3, "canonical cell-3 representative")
    require(lane in EDGE_SPECS and sigma_o in (-1, 1), "lane/sign domain")
    require(epsilon_1 in (-1, 1) and epsilon_2 in (-1, 1), "source signs")
    require(0 <= xi_index < 7 and 0 <= pairing_index < 15, "outside label")
    require(packet["variables"] == ["t", "r", "c", "b"], "packet variables")
    require(len(packet["common_equations"]) == 3, "common equation count")
    require(len(packet["kernel"]) == 8, "kernel width")
    require(len(packet["route_guards"]) == 16, "route guard count")
    require(len(packet["rank_cofactors"]) == 6, "rank cofactor count")

    definitions = []
    equations = []
    for index, expression in enumerate(packet["common_equations"]):
        name = f"q{index}"
        definitions.append(f"poly {name}={expression};")
        equations.append(name)
    for index, expression in enumerate(packet["kernel"]):
        definitions.append(f"poly k{index}={expression};")

    definitions.extend((
        "poly lm=-t^2;",
        "poly a2m=k0+k1*lm+k2*lm^2;",
        "poly a0m=k3+k4*lm+k5*lm^2;",
        "poly bm=k6+k7*lm;",
    ))
    target_values = ("b", "c", "d", "e", "f")
    signed_edges = tuple(
        edge(
            target_values[left],
            target_values[right],
            sigma_o if sign == 0 else sign,
        )
        for left, right, sign in EDGE_SPECS[lane]
    )
    for index, (product, squared_sum) in enumerate(signed_edges):
        definitions.append(f"poly rec{index}={product};")
        definitions.append(f"poly sum{index}={squared_sum};")

    definitions.append(f"poly q3=rec{xi_index}*a2m-a0m;")
    equations.append("q3")
    residual = tuple(index for index in range(7) if index != xi_index)
    matching = tuple(pairings(range(6)))[pairing_index]
    for offset, (left, right) in enumerate(matching, start=4):
        y_record = residual[left]
        z_record = residual[right]
        prefix = f"m{offset}"
        definitions.extend((
            f"poly {prefix}p0=k3-rec{y_record}*k0;",
            f"poly {prefix}p1=k4-rec{y_record}*k1;",
            f"poly {prefix}p2=k5-rec{y_record}*k2;",
            f"poly {prefix}q0=k3-rec{z_record}*k0;",
            f"poly {prefix}q1=-k4+rec{z_record}*k1;",
            f"poly {prefix}q2=k5-rec{z_record}*k2;",
            f"poly q{offset}=({prefix}p2*{prefix}q0-{prefix}p0*{prefix}q2)^2"
            f"-({prefix}p2*{prefix}q1-{prefix}p1*{prefix}q2)"
            f"*({prefix}p1*{prefix}q0-{prefix}p0*{prefix}q1);",
        ))
        equations.append(f"q{offset}")
    definitions.append(f"poly q7=lm*bm^2-sum{xi_index}*a2m^2;")
    equations.append("q7")
    require(len(equations) == 8, "complete equation ledger")

    guards = list(packet["route_guards"])
    guards.extend(target_values)
    full_target = ("1", *target_values)
    guards.extend(
        f"({full_target[left]})^2-({full_target[right]})^2"
        for left in range(6) for right in range(left + 1, 6)
    )
    a2_names = ("k0", "k1", "k2")
    guards.extend(
        evaluate_kernel(a2_names, label)
        for label in ("t^2", "1", "-1", "r^2", "-r^2")
    )
    guards.append("a2m")
    unique_guards = []
    seen = set()
    for guard in guards:
        compact = "".join(guard.split())
        if compact not in seen:
            seen.add(compact)
            unique_guards.append(guard)
    return {
        "variables": ("t", "r", "c", "b", "d", "e", "f"),
        "definitions": tuple(definitions),
        "equations": tuple(equations),
        "guards": tuple(unique_guards),
        "rank_cofactors": tuple(packet["rank_cofactors"]),
        "common_equation_count": 3,
        "outside_equation_count": 5,
    }


def verify_edge_table(edge_table=EDGE_SPECS):
    require(set(edge_table) == {"S0", "SDE", "SDF"}, "lane cover")
    require(all(len(rows) == 7 for rows in edge_table.values()), "record count")
    require(len(tuple(pairings(range(6)))) == 15, "matching count")
    require(edge_table["S0"][2:6] == (
        (2, 3, 1), (2, 3, -1), (2, 4, 1), (2, 4, -1)
    ), "S0 signed pairs")
    require(edge_table["SDE"][2] == edge_table["SDE"][3], "SDE duplicate")
    require(edge_table["SDF"][4] == edge_table["SDF"][5], "SDF duplicate")
    return 3, 21, 15


if __name__ == "__main__":
    lanes, records, matchings = verify_edge_table()
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_CACHED_CORE_PASS "
          f"lanes={lanes} signed_records={records} matchings={matchings}")
