"""
Game Theory Simulations from "The Selfish Gene" by Richard Dawkins
Early chapters focusing on ESS (Evolutionarily Stable Strategy)
"""


class Payoff:
    """Simple payoff matrix for game outcomes"""
    def __init__(self, win=4, loss=0, draw=2, injury=-2):
        self.win = win
        self.loss = loss
        self.draw = draw
        self.injury = injury


class HawkVsDoveSimulation:
    """
    Hawk vs Dove: Classic game theory simulation
    - Hawks: Always fight for the resource (aggressive)
    - Doves: Avoid confrontation (peaceful)
    """
    
    def __init__(self, payoff=None):
        self.payoff = payoff or Payoff()
    
    def hawk_vs_hawk(self):
        """When two hawks fight, one wins and one is injured"""
        return (self.payoff.win + self.payoff.injury) / 2
    
    def hawk_vs_dove(self):
        """Hawk wins, Dove retreats without injury"""
        return (self.payoff.win, self.payoff.loss)
    
    def dove_vs_dove(self):
        """Two doves share the resource"""
        return self.payoff.draw
    
    def run(self):
        """Show payoffs for each matchup"""
        results = {
            "Hawk vs Hawk": self.hawk_vs_hawk(),
            "Hawk vs Dove (Hawk gets)": self.hawk_vs_dove()[0],
            "Hawk vs Dove (Dove gets)": self.hawk_vs_dove()[1],
            "Dove vs Dove": self.dove_vs_dove(),
        }
        return results


class BourgeoisVsIntruderSimulation:
    """
    Bourgeois (Home Defender) vs Intruder (Attacker)
    - Bourgeois: Defend home, retreat if intruding elsewhere
    - Intruder: Always attack
    
    This demonstrates why Bourgeois is an Evolutionarily Stable Strategy (ESS)
    """
    
    def __init__(self, payoff=None):
        self.payoff = payoff or Payoff()
    
    def bourgeois_vs_bourgeois_at_home(self):
        """Both defend: 50% chance to win/lose"""
        return self.payoff.draw
    
    def bourgeois_vs_intruder_at_home(self):
        """Bourgeois wins when defending home"""
        return (self.payoff.win, self.payoff.loss)
    
    def bourgeois_vs_intruder_away(self):
        """Bourgeois retreats when intruding"""
        return (self.payoff.loss, self.payoff.win)
    
    def intruder_vs_intruder(self):
        """Two intruders fight (like hawks)"""
        return (self.payoff.win + self.payoff.injury) / 2
    
    def run(self):
        """Show why Bourgeois is ESS"""
        results = {
            "Bourgeois vs Bourgeois (at home)": self.bourgeois_vs_bourgeois_at_home(),
            "Bourgeois at home vs Intruder": self.bourgeois_vs_intruder_at_home()[0],
            "Intruder vs Bourgeois at home": self.bourgeois_vs_intruder_at_home()[1],
            "Bourgeois intruding vs Intruder": self.bourgeois_vs_intruder_away()[0],
            "Intruder vs Bourgeois intruding": self.bourgeois_vs_intruder_away()[1],
            "Intruder vs Intruder": self.intruder_vs_intruder(),
        }
        return results


class SimpleStrategySimulation:
    """
    Run a simple tournament where strategies compete
    """
    
    def __init__(self):
        self.hawk_dove = HawkVsDoveSimulation()
        self.bourgeois_intruder = BourgeoisVsIntruderSimulation()
    
    def run_all(self):
        """Run all simulations"""
        print("=" * 60)
        print("SELFISH GENE SIMULATIONS")
        print("=" * 60)
        
        print("\n1. HAWK VS DOVE SIMULATION")
        print("-" * 60)
        for scenario, payoff in self.hawk_dove.run().items():
            print(f"{scenario}: {payoff}")
        
        print("\n2. BOURGEOIS (HOME DEFENDER) VS INTRUDER SIMULATION")
        print("-" * 60)
        for scenario, payoff in self.bourgeois_intruder.run().items():
            print(f"{scenario}: {payoff}")
        
        print("\n" + "=" * 60)


if __name__ == "__main__":
    sim = SimpleStrategySimulation()
    sim.run_all()
