#!/usr/bin/env python3
"""ccd_mutation_control: prove the stage-2/3 battery counters are LIVE.

Three deliberate mutations at (32,16,p=97,geom5), each must trip its counter:
  MUT-A: corrupt the quotient word u1 at one petal point before the census
         (members then disagree with the true official word: LIFT_SEMANTICS
         and/or agreement-set mismatches must fire).
  MUT-B: lift with the WRONG split point x_{nf+1} instead of x_nf
         (C1-analog breaks: lifted member's official agreement not fiberwise).
  MUT-C: inject a fake member (random poly with its true small agreement set
         forced through) into the battery (A_THRESH / ESCAPE / NOT_FULL_PETAL
         must fire).
"""
import sys, importlib.util, random
spec = importlib.util.spec_from_file_location("s3", sys.argv[1] if len(sys.argv) > 1
                                              else "ccd_stage3.py")
s3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(s3)

n, k, p = 32, 16, 97
dom = s3.order_n_domain(p, n)
half = n//2; nf = (k-1)//2; kp = k//2
scal = s3.make_scalars("geom5", n, k, p, dom)
values, core, petals, bg, nf, locZ = s3.build_word(n, k, p, dom, scal)
u1v = s3.u1_of_word(n, p, dom, values)
dom2 = [dom[i]*dom[i] % p for i in range(half)]

# MUT-A: corrupted u1
u1_bad = u1v[:]
u1_bad[kp+2] = (u1_bad[kp+2] + 1) % p
mem_bad, _ = s3.config_census(half, kp, p, dom2, u1_bad, kp-1)
viol, _ = s3.battery_m2(n, k, p, dom, values, petals, nf, mem_bad, "MUT-A")
print("MUT-A tripped:", len(viol) > 0, f"({len(viol)} violations)")

# MUT-B: wrong split point in lift — emulate by shifting domain used in lift.
mem, _ = s3.config_census(half, kp, p, dom2, u1v, kp-1)
orig_lift = s3.lift
def bad_lift(g, x_nf_arg, k_arg, p_arg):
    return orig_lift(g, dom[nf+1], k_arg, p_arg)
s3.lift = bad_lift
viol, _ = s3.battery_m2(n, k, p, dom, values, petals, nf, mem, "MUT-B")
s3.lift = orig_lift
print("MUT-B tripped:", len(viol) > 0, f"({len(viol)} violations)")

# MUT-C: fake member with junk agreement set
rng = random.Random(2)
gfake = tuple(rng.randrange(p) for _ in range(kp))
fake_agr = frozenset(range(kp+1))   # claims agreement on zero region + 1
mem_fake = dict(mem)
mem_fake[gfake] = fake_agr
viol, _ = s3.battery_m2(n, k, p, dom, values, petals, nf, mem_fake, "MUT-C")
print("MUT-C tripped:", len(viol) > 0, f"({len(viol)} violations)")
