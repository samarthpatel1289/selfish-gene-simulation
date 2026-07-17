class Dove:
    """
    Always displays peacefully — shares with other Doves, retreats from Hawks.
    Never risks physical injury.
    """

    emoji   = "🕊️"
    is_hawk = False
    is_dove = True

    def compete(self, other, payoff):
        """Return this Dove's payoff from one contest against 'other'."""
        if other.is_hawk:
            return payoff.loss   # Dove retreats rather than risk a fight
        return payoff.draw       # Two Doves share the resource equally
