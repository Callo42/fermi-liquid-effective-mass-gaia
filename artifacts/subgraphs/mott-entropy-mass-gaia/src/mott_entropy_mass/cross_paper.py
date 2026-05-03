"""cross_paper -- audited open-problem hooks for the Mott entropy package.

The formal claim graph is intentionally limited to the chain-backed Capone 2001
root. Existing Brinkman-Rice, NiS2, and Kondo-lattice context was used only for
the contradiction/open-problem audit recorded under artifacts/lkm-discovery.
"""

from gaia.lang import contradiction, equivalence, question, support

from .paper_capone2001 import gcn_e4ecd721edd14d3f


open_problem_br_entropy_escape_routes = question(
    "When Brinkman-Rice-like mass enhancement is replaced by other Mott routes "
    "such as a finite-mass spinon-Fermi-surface scenario, pressure-tuned NiS2 "
    "heavy-Fermi-liquid behavior, or Kondo-lattice Brinkman-Rice liquids, which "
    "assumptions in the Capone-Fabrizio-Tosatti entropy-mismatch argument still "
    "apply, and which provide genuine escape routes from an intervening "
    "instability?",
    audit_origin="open-problem hunt versus existing Brinkman-Rice/NiS2/Kondo context",
    scoped_root="gcn_e4ecd721edd14d3f",
)


_ROOT_SCOPE = gcn_e4ecd721edd14d3f
_OPEN_PROBLEM_SCOPE = open_problem_br_entropy_escape_routes
_AVAILABLE_OPERATORS = (contradiction, equivalence, support)
