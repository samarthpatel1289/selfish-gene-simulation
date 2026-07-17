class Hawk:
    """
    Always fights aggressively for every resource.
    Wins big against Doves but risks injury against other Hawks.
    """

    emoji    = "🦅"
    is_hawk  = True
    is_dove  = False

    def compete(self, other, payoff):
        """Return this Hawk's payoff from one contest against 'other'."""
        if other.is_dove:
            return payoff.win              # Dove retreats — Hawk takes the resource
        # Hawk vs Hawk: 50 % chance to win, 50 % chance of injury
        return (payoff.win + payoff.injury) / 2
