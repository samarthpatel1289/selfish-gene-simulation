from payoff import Payoff
from bourgeois_intruder.bourgeois import Bourgeois
from bourgeois_intruder.intruder import Intruder


class BourgeoisVsIntruderSimulation:
    """
    Shows every Bourgeois / Intruder matchup and the resulting payoffs.

    Key insight:
      When two Bourgeois agents meet, one is the home owner and one is the visitor.
      The owner wins — no costly fight ever happens between two Bourgeois agents.
      This makes Bourgeois an ESS: Intruders cannot invade because they always lose
      to a home-defending Bourgeois.
    """

    def __init__(self, payoff=None):
        self.payoff = payoff or Payoff()

    def run(self):
        """Return a dict of scenario → payoff for each matchup."""
        b = Bourgeois()
        i = Intruder()
        return {
            "Bourgeois (home) vs Bourgeois (away)": b.compete(b, self.payoff, is_at_home=True),
            "Bourgeois (away) vs Bourgeois (home)": b.compete(b, self.payoff, is_at_home=False),
            "Bourgeois (home) vs Intruder":         b.compete(i, self.payoff, is_at_home=True),
            "Bourgeois (away) vs Intruder":         b.compete(i, self.payoff, is_at_home=False),
            "Intruder vs Bourgeois (home)":         i.compete(b, self.payoff),
            "Intruder vs Intruder":                 i.compete(i, self.payoff),
        }
