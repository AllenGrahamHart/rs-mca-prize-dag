#!/usr/bin/env python3
"""Build one deterministic term-block square pilot for R76[0]."""

import re


PRIME = 2130706433
BLOCK_SIZE = 128


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def split_terms(polynomial):
    terms = re.findall(r"[+-]?[^+-]+", polynomial)
    require(terms and "".join(terms) == polynomial, "canonical term split")
    return terms


def build(graph_payload, bracket_payload):
    graph = graph_payload["row"]
    require(graph_payload["collection_complete"] is True and
            graph["status"] == "COMPLETE" and graph["unit"] is False and
            graph["basis_size"] == 48 and len(graph["basis"]) == 48,
            "graph basis")
    brackets = bracket_payload["row"]
    require(bracket_payload["collection_complete"] is True and
            brackets["status"] == "COMPLETE" and
            len(brackets["brackets"]) == 14, "bracket bank")
    source = next(
        value for value in brackets["brackets"]
        if value["family"] == "M0" and value["index"] == 0
    )
    stage = next(
        value for value in brackets["bracket_stages"]
        if value["family"] == "M0" and value["index"] == 0
    )
    terms = split_terms(source["polynomial"])
    require(len(terms) == stage["term_count"] == 1152, "source term count")
    start, end = 0, min(BLOCK_SIZE, len(terms))
    block = "".join(terms[start:end]).lstrip("+")
    require(block and len(split_terms(block)) == end-start, "block ledger")
    basis_definitions = tuple(
        f"poly g{index}={value};" for index, value in enumerate(graph["basis"])
    )
    program = f"""
ring R={PRIME},(x,t,r,c,b),dp;
option(redSB);
{chr(10).join(basis_definitions)}
ideal G={','.join(f'g{index}' for index in range(48))};
attrib(G,"isSB",1);
poly p={block};
print("INPUT_TERMS="+string(size(p)));
poly raw=p*p;
print("RAW_DEG="+string(deg(raw))+",RAW_SIZE="+string(size(raw)));
poly n=reduce(raw,G);
print("NORMAL_DEG="+string(deg(n))+",NORMAL_SIZE="+string(size(n)));
print("NORMAL_BEGIN"); print(n); print("NORMAL_END");
print("END"); quit;
"""
    return {
        "program": program,
        "relation": "exact R76[0] block-square pilot",
        "target_coefficient": 0,
        "source_family": "M0",
        "source_index": 0,
        "source_polynomial_sha256": source["polynomial_sha256"],
        "source_term_count": len(terms),
        "block_size": BLOCK_SIZE,
        "block_index": 0,
        "term_start": start,
        "term_end": end,
        "input_term_count": end-start,
        "product_multiplier": 1,
        "graph_basis_size": 48,
        "graph_basis_sha256": graph["basis_sha256"],
    }


if __name__ == "__main__":
    require(split_terms("x2-2xy+y2") == ["x2", "-2xy", "+y2"],
            "splitter self-test")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_R0_BLOCK_PILOT_PROGRAM_PASS "
          "block_size=128 product=square")
