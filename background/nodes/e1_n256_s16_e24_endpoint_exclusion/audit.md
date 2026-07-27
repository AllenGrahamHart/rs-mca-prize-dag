# Audit

The verifier pins both dependency statements, requires both dependencies to be
`PROVED`, and checks that they are the only incoming requirement edges.  It
also verifies the six-profile partition and the exact `V<=46` frontier.  This
node introduces no new computation or assumption.
