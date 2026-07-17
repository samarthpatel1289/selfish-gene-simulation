from payoff import Payoff
from hawk_dove.hawk import Hawk
from hawk_dove.dove import Dove


class HawkVsDoveSimulation:
    """
    Runs every possible Hawk / Dove matchup and returns the payoffs.

    Interpretation:
      Hawk vs Hawk  — both risk injury; expected value is (win + injury) / 2
      Hawk vs Dove  — Hawk wins; Dove retreats without a fight
      Dove vs Hawk  — Dove retreats; Hawk wins
      Dove vs Dove  — both display; they share the resource
    """

    def __init__(self, payoff=None):
        self.payoff = payoff or Payoff()

    def run(self):
        """Return a dict of scenario → payoff for each matchup."""
        h = Hawk()
        d = Dove()
        return {
            "Hawk vs Hawk": h.compete(h, self.payoff),
            "Hawk vs Dove": h.compete(d, self.payoff),
            "Dove vs Hawk": d.compete(h, self.payoff),
            "Dove vs Dove": d.compete(d, self.payoff),
        }
