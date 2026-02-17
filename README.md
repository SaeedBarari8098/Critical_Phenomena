Sandpile Model Simulation (Normal vs Mana)

This project simulates and compares two sandpile models:

Normal (Deterministic) Sandpile Model

Mana (Stochastic) Sandpile Model

The simulation visualizes:

The spatial evolution of the sandpile grid

The average height of the system over time

A side-by-side comparison between deterministic and stochastic dynamics

The animation helps illustrate self-organized criticality (SOC) behavior in both models.

📌 Description

This code implements a 2D lattice sandpile system where grains are added sequentially and sites topple when their height exceeds a threshold.

Two models are compared:

1️⃣ Normal Sandpile (Deterministic Toppling)

A site topples when height > threshold.

It loses 4 grains.

Each of its four nearest neighbors receives exactly 1 grain.

Fully deterministic dynamics.

2️⃣ Mana Sandpile (Stochastic Toppling)

A site topples when height > threshold.

It loses 2 grains.

Each grain is randomly distributed to one of the four neighbors.

Stochastic redistribution introduces randomness in avalanche dynamics.

⚙️ Parameters

You can modify the following parameters at the top of the script:

grid_size = 50        # Size of lattice (NxN)
threshold = 4         # Critical height for toppling
grain_number = 35000  # Number of grains added
input_type = "center" # "center" or "random"
Parameter Explanation
Parameter	Description
grid_size	Size of square lattice
threshold	Critical height triggering toppling
grain_number	Total grains added during simulation
input_type	Grain injection location ("center" or "random")
📊 Output

The program produces:

🔹 Animation Window (2×2 layout)

Top-left: Normal sandpile grid evolution

Top-right: Average height (Normal)

Bottom-left: Mana sandpile grid evolution

Bottom-right: Average height (Mana)

🔹 Final State Plot

After animation ends, a static figure shows:

Final grid configuration

Full time evolution of average height

🧠 Scientific Background

The sandpile model is a classic example of Self-Organized Criticality (SOC), originally introduced in:

Bak, Tang, and Wiesenfeld (1987)

SOC systems naturally evolve into a critical state without parameter tuning.

This project compares:

Deterministic critical dynamics

Stochastic critical dynamics

The Mana model introduces randomness and belongs to a different universality class than the classical BTW model.

▶️ How to Run

Make sure you have:

pip install numpy matplotlib

Then run:

python your_script_name.py
📁 Code Structure
Function	Purpose
topple_normal()	Deterministic toppling rule
topple_mana()	Stochastic toppling rule
calculate_average_height()	Computes mean lattice height
run_normal()	Runs full simulation
update()	Updates animation frame
🔬 Possible Extensions

You can extend this project by:

Measuring avalanche size distribution

Studying power-law behavior

Computing critical exponents

Comparing boundary conditions

Increasing lattice size

Adding periodic boundary conditions

Exporting animation as MP4 or GIF

📈 Performance Note

Large grain_number values require:

High memory (stores full time evolution)

Longer computation time

For faster testing, reduce:

grain_number = 5000
