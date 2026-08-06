# Node payload ownership

Generated proof payloads belong to the narrowest DAG node whose claim they
certify. A reduction node may expose a small shared atlas used by several
children, but it must not serve as a storage directory for downstream census,
norm, or audit packets.

For a generated packet, keep the production source, launcher, result,
independent audit, and source pin together in the owning node. Cross-node
references are reserved for genuine theorem dependencies or deliberately
shared atlases. This keeps each node independently reviewable and prevents an
umbrella directory from silently accumulating unrelated proof obligations.
