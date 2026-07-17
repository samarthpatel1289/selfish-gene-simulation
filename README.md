# 🧬 selfish-gene-simulation

Interactive 3D game theory simulations from *The Selfish Gene* by Richard Dawkins — **Hawk vs Dove** and **Bourgeois vs Intruder**.

---

## 🌐 Web App (Interactive 3D)

Open **`index.html`** directly in any modern browser — no server or build step needed.

> **GitHub Pages:** To host the site publicly, go to your repo **Settings → Pages → Source → Deploy from branch → `main` / `(root)`**, then visit `https://samarthpatel1289.github.io/selfish-gene-simulation/` after the deployment finishes (~1 min).

### What you'll see
- 🦅🕊️ Emoji agents roaming a 3D arena
- 🗺️ **5 territories** on the outer ring — fewer patches than agents, so there's always a contested fight
- ⏰ **Time-of-day cycle** visible in the top-left HUD:
  - 🌅 **Fight Phase** — agents rush to territories; contested patches glow red
  - ☀️ **Roaming** — agents wander freely between rounds
  - 🌇 **Mate Phase** — agents with enough energy reproduce in the green centre zone
  - 🌙 **Night** — weak or old agents die off
- 📊 **Live population chart** on the right updates every round
- 🎛️ Sliders for speed, starting population, and payoff values

---

## 🗂️ Folder Structure

Each simulation lives in its own folder. Each strategy is its own file.

```
selfish-gene-simulation/
│
├── payoff.py                    ← shared Payoff class (win / loss / draw / injury)
│
├── hawk_dove/
│   ├── hawk.py                  ← class Hawk  — always fights aggressively
│   ├── dove.py                  ← class Dove  — always retreats peacefully
│   └── simulation.py            ← class HawkVsDoveSimulation
│
├── bourgeois_intruder/
│   ├── bourgeois.py             ← class Bourgeois — defends home, retreats away
│   ├── intruder.py              ← class Intruder  — always attacks
│   └── simulation.py            ← class BourgeoisVsIntruderSimulation
│
├── simulations.py               ← main runner (imports from both packages above)
└── index.html                   ← 3D web app (Three.js + Chart.js, no build needed)
```

---

## 🐍 Python Simulations

Run from the repository root:

```bash
python simulations.py
```

---

## 📖 Simulations Explained

### Hawk vs Dove
| Matchup        | What happens                              |
|----------------|-------------------------------------------|
| Hawk vs Hawk   | Both risk injury — costly fight           |
| Hawk vs Dove   | Dove retreats; Hawk wins                  |
| Dove vs Dove   | Both display and share the resource       |

The **ESS** depends on payoff values. If injury is cheap, Hawks dominate. If injury is costly, a mixed population is stable.

### Bourgeois vs Intruder
| Matchup                     | What happens                              |
|-----------------------------|-------------------------------------------|
| Bourgeois (home) vs anyone  | Owner always wins — no fight needed       |
| Bourgeois (away) vs Intruder| Retreats — avoids costly battle           |
| Intruder vs Intruder        | Both fight — costly, like Hawk vs Hawk    |

Bourgeois is typically the **ESS** because the "owner wins" convention eliminates injuries entirely.

