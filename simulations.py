"""
Game Theory Simulations from "The Selfish Gene" by Richard Dawkins.

Folder structure
----------------
payoff.py                          — shared Payoff class
hawk_dove/
    hawk.py                        — Hawk strategy
    dove.py                        — Dove strategy
    simulation.py                  — HawkVsDoveSimulation
bourgeois_intruder/
    bourgeois.py                   — Bourgeois strategy
    intruder.py                    — Intruder strategy
    simulation.py                  — BourgeoisVsIntruderSimulation

Run from the repository root:
    python simulations.py
"""

from hawk_dove.simulation import HawkVsDoveSimulation
from bourgeois_intruder.simulation import BourgeoisVsIntruderSimulation


class SimpleStrategySimulation:
    """Runs both simulations and prints a formatted summary."""

    def __init__(self):
        self.hawk_dove          = HawkVsDoveSimulation()
        self.bourgeois_intruder = BourgeoisVsIntruderSimulation()

    def run_all(self):
        print("=" * 60)
        print("SELFISH GENE SIMULATIONS")
        print("=" * 60)

        print("\n1. HAWK VS DOVE")
        print("-" * 60)
        for scenario, result in self.hawk_dove.run().items():
            print(f"  {scenario}: {result}")

        print("\n2. BOURGEOIS VS INTRUDER")
        print("-" * 60)
        for scenario, result in self.bourgeois_intruder.run().items():
            print(f"  {scenario}: {result}")

        print("\n" + "=" * 60)


if __name__ == "__main__":
    sim = SimpleStrategySimulation()
    sim.run_all()
