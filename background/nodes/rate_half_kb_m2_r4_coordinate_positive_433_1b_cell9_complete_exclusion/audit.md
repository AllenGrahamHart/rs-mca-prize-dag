# Audit

The composition verifier reads every dependency manifest, requires status
`PROVED`, reconstructs the router partition, and checks exact representative
ownership. It rejects duplicate owners, missing or extra representatives,
wrong orbit sizes, or any total other than `30+75=105`.

The cross-audit mutates one owner assignment and one dependency status; both
hostile changes must be detected.
