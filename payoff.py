class Payoff:
    """Reward and cost values used in every contest between animals."""

    def __init__(self, win=4, loss=0, draw=2, injury=-2):
        self.win    = win     # reward for winning a resource
        self.loss   = loss    # cost of retreating
        self.draw   = draw    # reward for sharing a resource
        self.injury = injury  # extra cost when a fight turns physical
