class Intruder:
    """
    Always attacks, regardless of territory ownership.
    Equivalent to a pure Hawk that ignores the 'owner wins' convention.
    """

    emoji        = "⚔️"
    is_bourgeois = False
    is_intruder  = True

    def compete(self, other, payoff):
        """Return this Intruder's payoff from one contest against 'other'.

        vs Bourgeois: Bourgeois wins at home, so Intruder gets only loss on average.
        vs Intruder:  Both fight — costly battle, expected value is (win + injury) / 2.
        """
        if other.is_bourgeois:
            return payoff.loss                      # Bourgeois defender wins at home
        return (payoff.win + payoff.injury) / 2    # Intruder vs Intruder: costly fight
