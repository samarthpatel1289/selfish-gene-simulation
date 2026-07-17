class Bourgeois:
    """
    Plays the 'owner wins' convention:
      • Defends territory aggressively when at home  → wins
      • Retreats peacefully when intruding elsewhere → loses

    This avoids all costly injuries because both sides agree on the rule.
    """

    emoji          = "🏠"
    is_bourgeois   = True
    is_intruder    = False

    def compete(self, other, payoff, is_at_home=True):
        """Return this Bourgeois agent's payoff.

        Args:
            other:       the opponent (Bourgeois or Intruder instance)
            payoff:      Payoff object with win/loss/draw/injury values
            is_at_home:  True if this agent owns the contested territory
        """
        if is_at_home:
            return payoff.win   # home defender wins
        return payoff.loss      # intruder retreats
