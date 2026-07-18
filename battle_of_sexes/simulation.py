from battle_of_sexes.coy_female import CoyFemale
from battle_of_sexes.fast_female import FastFemale
from battle_of_sexes.faithful_male import FaithfulMale
from battle_of_sexes.philanderer_male import PhilandererMale


class BattleOfTheSexesSimulation:
    """
    Models the Battle of the Sexes from Dawkins' 'The Selfish Gene'.

    Two independent populations interact only cross-sex:
      • Females: Coy (requires long courtship) or Fast (mates immediately)
      • Males:   Faithful (courts + shares rearing) or Philanderer (deserts)

    Payoff derivation (defaults: B=15, R=20, C=3):
      Coy × Faithful    → each:  B − R/2 − C = 15 − 10 − 3 = +2
      Coy × Philanderer → each:  no mating    = 0
      Fast × Faithful   → each:  B − R/2      = 15 − 10     = +5
      Fast × Philanderer→ female: B − R = −5 (raises alone)
                          male:   B     = +15 (deserts)
    """

    def __init__(self, baby_benefit=15, rearing_cost=20, courtship_cost=3):
        self.B = baby_benefit
        self.R = rearing_cost
        self.C = courtship_cost

    def payoffs(self, female, male):
        """Return (female_payoff, male_payoff) for one encounter."""
        if female.is_coy and male.is_faithful:
            val = self.B - self.R / 2 - self.C
            return (val, val)
        if female.is_coy and male.is_philanderer:
            return (0, 0)                            # no mating — Coy refuses
        if female.is_fast and male.is_faithful:
            val = self.B - self.R / 2
            return (val, val)
        if female.is_fast and male.is_philanderer:
            return (self.B - self.R, self.B)         # female alone: B−R; male deserts: B
        raise ValueError(f"Unknown pairing: {type(female).__name__} × {type(male).__name__}")

    def run(self):
        """Return a dict of scenario → (female_payoff, male_payoff)."""
        f_coy   = CoyFemale()
        f_fast  = FastFemale()
        m_faith = FaithfulMale()
        m_phil  = PhilandererMale()

        return {
            "Coy × Faithful":     self.payoffs(f_coy,  m_faith),
            "Coy × Philanderer":  self.payoffs(f_coy,  m_phil),
            "Fast × Faithful":    self.payoffs(f_fast, m_faith),
            "Fast × Philanderer": self.payoffs(f_fast, m_phil),
        }
