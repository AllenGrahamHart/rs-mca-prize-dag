#!/usr/bin/env python3
"""Retain the reduced M0, M1, M2 bracket arrays before final convolution."""


BRACKET_LAYOUT = (("M0", "m0c", 5), ("M1", "m1c", 5), ("M2", "m2c", 4))
FINAL_MARKER = "poly raw_y76c0="


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def build(packet_row, graph_payload, raw_core, progressive_core):
    built = progressive_core.build(packet_row, graph_payload, raw_core)
    source_program = built.pop("program")
    require(source_program.count(FINAL_MARKER) == 1, "final marker")
    prefix = source_program[:source_program.index(FINAL_MARKER)]
    output = []
    for family, stem, count in BRACKET_LAYOUT:
        for index in range(count):
            value = f"{stem}{index}"
            output.extend((
                f'print("BRACKET={family},INDEX={index},DEG="'
                f'+string(deg({value}))+",SIZE="+string(size({value})));',
                f'print("{family}_{index}_BEGIN"); print({value}); '
                f'print("{family}_{index}_END");',
            ))
    program = prefix + "\n".join((*output, 'print("END"); quit;')) + "\n"
    return {
        **built,
        "program": program,
        "relation": "exact reduced R76 bracket bank",
        "source_progressive_relation": built["relation"],
        "bracket_layout": [
            {"family": family, "count": count}
            for family, _, count in BRACKET_LAYOUT
        ],
        "bracket_count": 14,
        "expected_zero_brackets": [
            {"family": "M0", "index": 2},
            {"family": "M1", "index": 0},
        ],
    }


if __name__ == "__main__":
    require(sum(count for _, _, count in BRACKET_LAYOUT) == 14,
            "bracket count")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_FFF_R76_BRACKETS_PROGRAM_PASS "
          "brackets=14 intermediates=61")
