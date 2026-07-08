#!/usr/bin/env python3
"""Bridge-budget compiler for h=3 activated shapes under RC-RANK."""

from __future__ import annotations

from math import isqrt


C_RED = 13
H3_ACT_C = 16
B_MAX = 50_000


EXPECTED_BUDGETS = {
    13: 11,
    14: 14,
    15: 18,
    16: 23,
    17: 29,
    18: 36,
    19: 46,
    20: 58,
    21: 73,
    22: 92,
    23: 116,
    24: 146,
    25: 184,
    26: 232,
    27: 292,
    28: 368,
    29: 463,
    30: 584,
    31: 736,
    32: 927,
    33: 1168,
    34: 1472,
    35: 1855,
    36: 2337,
    37: 2944,
    38: 3710,
    39: 4674,
    40: 5889,
    41: 7420,
}

EXPECTED_PASS = {
    13: (123234, 50, 215, 2408662, 13220350, 26875000, 26495293),
    14: (249511, 63, 342, 6095189, 42574896, 85516074, 85332660),
    15: (512063, 80, 546, 15532577, 139518288, 279552000, 279586404),
    16: (1046347, 102, 873, 39715688, 455753142, 926434584, 913460847),
    17: (2091314, 128, 1385, 99878248, 1446341650, 2904555520, 2896469221),
    18: (4114787, 160, 2188, 250087563, 4480953984, 8962048000, 9003152304),
    19: (8363453, 203, 3495, 635440550, 14609169900, 29237167365, 29230265346),
    20: (16753864, 256, 5554, 1604326833, 46517149328, 93180657664, 93050956372),
    21: (33507939, 323, 8827, 4051706490, 147884433242, 297454602809, 295774573843),
    22: (67029802, 406, 13989, 10192172708, 468095553432, 936191666424, 937679889228),
    23: (134154474, 512, 22239, 25719494366, 1491632532936, 2984868052992, 2983461346572),
    24: (268063071, 645, 35308, 64827197931, 4732301863744, 9474411901500, 9464770898072),
    25: (536478514, 813, 56069, 163477248772, 15039617528624, 30129675009993, 30079813774232),
    26: (1073729992, 1024, 89002, 411914296233, 47781619416128, 95565169819648, 95564116726288),
    27: (2145318035, 1290, 141288, 1038040049639, 151553773582848, 303301395432000, 303107694494880),
    28: (4292573453, 1625, 224237, 2615635307500, 481100397392992, 962204470703125, 962553793160368),
    29: (8571301883, 2047, 356009, 6590627671720, 1525725108479078, 3053616581208407, 3051460612006823),
    30: (17165889077, 2580, 565261, 16615081549836, 4851591651469264, 9707516566632000, 9703207625104808),
    31: (34344883124, 3251, 897388, 41875932033387, 15410320738601984, 30834092170180388, 30820685976573568),
    32: (68661137419, 4095, 1424386, 105501578083329, 48899956746557592, 97811386396746750, 97799962883246910),
    33: (137340309227, 5160, 2261265, 265892837622032, 155281283546032800, 310670892901440000, 310562834342534544),
    34: (274766026264, 6501, 3589461, 670014901765460, 493105260913379712, 986210761304828961, 986261935398758592),
    35: (549685909525, 8192, 5698589, 1688643707532316, 1566216997180119830, 3132832433708204032, 3132434077472448035),
    36: (1099298921943, 10321, 9045940, 4255110008539059, 4972095550244503200, 9945326308074036340, 9944192089955783220),
    37: (2198240087472, 13003, 14359322, 10721887652616985, 15782617180571012096, 31569276003271723694, 31565237249304406784),
    38: (4397621615659, 16384, 22795051, 27019948519576362, 50122000209932292460, 100253694520987746304, 100244009007628306730),
    39: (8794604045045, 20642, 36184638, 68085058562957885, 159114779176364431056, 318258164214695637744, 318229563723265159164),
    40: (17589583109929, 26007, 57439499, 171563396409095434, 505168414690935447114, 1010372265105270926157, 1010336841453163016715),
    41: (35180971745485, 32767, 91180207, 432319176039681198, 1603904112260744829080, 3207824627182681404241, 3207808286214434496580),
}

EXPECTED_NEXT_BOUNDS = {
    13: 137369,
    14: 271980,
    15: 547180,
    16: 1100130,
    17: 2180182,
    18: 4247341,
    19: 8588100,
    20: 17108622,
    21: 34030032,
    22: 67874656,
    23: 135572340,
    24: 270316238,
    25: 540058105,
    26: 1079411235,
    27: 2154343050,
    28: 4306101440,
    29: 8593867923,
    30: 17201952986,
    31: 34402091046,
    32: 68751986840,
    33: 137474386576,
    34: 274987875475,
    35: 550049441522,
    36: 1099875933545,
    37: 2199113936302,
    38: 4399030298925,
    39: 8796724619837,
    40: 17593246634044,
    41: 35186786842694,
}


def best_bound(n: int, z: int, b_max: int = B_MAX) -> int:
    best: int | None = None
    for b in range(2, b_max + 1):
        rank_cap = (1 + 6 * n * (b - 1)) // (4 * C_RED)
        ls_cap = (b**3 - 1) // (4 * C_RED * z)
        d = min(isqrt(rank_cap), ls_cap)
        if d < 1:
            continue
        a = d
        conditions = C_RED * d * (a + d) * z
        coeffs = a * b**3
        degree = (a - 1) + 6 * n * (b - 1)
        image_cap = z * (degree + 1)
        if not (conditions < coeffs and conditions < image_cap):
            continue
        bound = (z * degree + d - 1) // d
        if best is None or bound < best:
            best = bound
    if best is None:
        return 10**100
    return best


def witness_bound(n: int, z: int, b: int) -> tuple[int, int, int, int, int, int]:
    rank_cap = (1 + 6 * n * (b - 1)) // (4 * C_RED)
    ls_cap = (b**3 - 1) // (4 * C_RED * z)
    d = min(isqrt(rank_cap), ls_cap)
    if d < 1:
        raise AssertionError((n, z, b, "inadmissible d"))
    a = d
    conditions = C_RED * d * (a + d) * z
    coeffs = a * b**3
    degree = (a - 1) + 6 * n * (b - 1)
    image_cap = z * (degree + 1)
    if not (conditions < coeffs and conditions < image_cap):
        raise AssertionError((n, z, b, "failed inequalities"))
    bound = (z * degree + d - 1) // d
    return bound, d, degree, conditions, coeffs, image_cap


def verified_budget_for_n(s: int) -> tuple[int, int, int]:
    n = 2**s
    target = H3_ACT_C * n
    budget = EXPECTED_BUDGETS[s]
    expected_bound, b, d, degree, conditions, coeffs, image_cap = EXPECTED_PASS[s]
    bound, got_d, got_degree, got_conditions, got_coeffs, got_image_cap = witness_bound(
        n, budget, b
    )
    got = (bound, b, got_d, got_degree, got_conditions, got_coeffs, got_image_cap)
    expected = (expected_bound, b, d, degree, conditions, coeffs, image_cap)
    if got != expected:
        raise AssertionError((s, got, expected))
    next_bound = best_bound(n, budget + 1)
    if next_bound != EXPECTED_NEXT_BOUNDS[s]:
        raise AssertionError((s, "unexpected next bound", next_bound, EXPECTED_NEXT_BOUNDS[s]))
    if bound > target:
        raise AssertionError((s, "budget no longer passes", budget, bound, target))
    if next_bound <= target:
        raise AssertionError((s, "budget not maximal", budget, next_bound, target))
    return budget, bound, next_bound


def main() -> None:
    print("h=3 bridge-budget compiler")
    print(f"C_red={C_RED} H3_ACT_C={H3_ACT_C} B_max={B_MAX}")
    print(" s      n                 Z_budget       bound          16n       next_bound")
    for s in range(13, 42):
        n = 2**s
        budget, bound, next_bound = verified_budget_for_n(s)
        print(
            f"{s:2d} {n:16d} {budget:10d} {bound:14d}"
            f" {H3_ACT_C * n:14d} {next_bound:16d}"
        )

    print("bridge contract: activated shapes must batch into <= Z_budget repaired curves")
    print("maximality check: Z_budget has a pinned passing witness and Z_budget+1 fails")
    print("conditional conclusion: RC-RANK + bridge contract => H3-ACT(16)")
    print("H3_BRIDGE_BUDGET_COMPILER_PASS")


if __name__ == "__main__":
    main()
