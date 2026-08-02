# Row arithmetic for the cascade-ceiling audit.
# Rows pinned as in notes/pilots_20260802/xr_bridge_semantics/REPORT.md (A = k + n/scale + 1).
rows = [
    ("RowC 1/4",  1024, 4,   256),
    ("RowC 1/8",  1024, 8,   256),
    ("RowC 1/16", 1024, 16,  512),
    ("prize 1/4",  2199023255552, 4,  256),
    ("prize 1/8",  2199023255552, 8,  256),
    ("prize 1/16", 2199023255552, 16, 512),
]
print(f"{'row':<12}{'n':>16}{'k':>16}{'A':>16}{'h=t':>14}{'j=n-A':>16}{'3j<=n-k?':>10}")
for name,n,rate,scale in rows:
    k = n//rate
    A = k + n//scale + 1
    t = A-k
    j = n-A
    print(f"{name:<12}{n:>16}{k:>16}{A:>16}{t:>14}{j:>16}{str(3*j<=n-k):>10}")
print()
print("line cap L(w)=floor((n-w)/(A-w)) at the two candidate ceilings")
print(f"{'row':<12}{'L(A-2)':>22}{'L(A-1)':>22}{'ratio':>8}")
for name,n,rate,scale in rows:
    k = n//rate; A = k + n//scale + 1
    l2 = (n-(A-2))//(A-(A-2)); l1 = (n-(A-1))//(A-(A-1))
    print(f"{name:<12}{l2:>22}{l1:>22}{l1/l2:>8.2f}")
print()
print("collapsed-face contradiction  k+2 > kappa   (C1 of the widening cost pass)")
for name,n,rate,scale in rows:
    k = n//rate; A = k + n//scale + 1; h = A-k
    print(f"  {name:<12} h={h:<12} at kappa=A-2: {k+2 > A-2}   at kappa=A-1: {k+2 > A-1}")
print()
print("B_tan slot n-A+1 vs |T| forced by a core-(A-1) cascade  (|T| <= n-(A-1) = n-A+1)")
for name,n,rate,scale in rows:
    k = n//rate; A = k + n//scale + 1
    print(f"  {name:<12} n-A+1 = {n-A+1:<16} |T|_max at core A-1 = {n-(A-1):<16} saturation = {(n-(A-1))/(n-A+1):.4f}")
