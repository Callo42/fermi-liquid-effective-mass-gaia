"""cross_paper -- cross-paper operators for the He-3 effective-mass package.

The formal Gaia graph is intentionally limited to the chain-backed He-3 root.
External LKM match probes found related support and boundary-condition checks,
but no direct same-condition contradiction suitable for a contradiction() edge.
"""

from gaia.lang import contradiction, equivalence, support

from .paper_alvesalo1979 import gcn_800070efac5e476d


# Imported names keep this module ready for future audited cross-paper operators.
_ROOT_SCOPE = gcn_800070efac5e476d
_AVAILABLE_OPERATORS = (contradiction, equivalence, support)
