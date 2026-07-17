# selfish-gene-simulation

An interactive exploration of game theory concepts from *The Selfish Gene* by Richard Dawkins — **Hawk vs Dove** and **Bourgeois vs Intruder** simulations.

## 🌐 Web App (Interactive)

Open **`index.html`** directly in any browser, or visit the live GitHub Pages site:

👉 **https://samarthpatel1289.github.io/selfish-gene-simulation/**

Features:
- 📱 Mobile-friendly, works on any screen size
- 🎛️ Adjust payoff parameters (Win, Draw, Loss, Injury) with live sliders
- 📊 Real-time payoff matrix tables + bar charts
- 📈 Population dynamics charts showing Evolutionarily Stable Strategies (ESS)
- 🔬 Auto-calculated ESS analysis for both simulations

## 🐍 Python Simulations

Run the original class-based Python simulations from the terminal:

```bash
python simulations.py
```

This prints payoff results for Hawk vs Dove and Bourgeois vs Intruder matchups.

## 📖 Simulations Explained

### Hawk vs Dove
- **🦅 Hawk** always fights aggressively; risks injury when meeting another Hawk
- **🕊️ Dove** displays and retreats; shares peacefully with other Doves
- The ESS depends on whether injury costs outweigh the resource value

### Bourgeois vs Intruder
- **🏠 Bourgeois** defends home, retreats when intruding elsewhere
- **⚔️ Intruder** always attacks, ignoring ownership
- Bourgeois is typically the ESS because the "owner wins" rule eliminates costly battles
