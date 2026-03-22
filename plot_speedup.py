import matplotlib.pyplot as plt

# Data
processes = [1, 2, 4, 8, 16, 32, 64, 128, 256]
times = [909.229, 458.488, 225.016, 129.616, 107.743, 111.964, 108.812, 108.443, 108.598]

plt.figure(figsize=(9,5))

plt.plot(processes, times,
         marker='o',
         linewidth=2,
         markersize=7)

# log schaal voor betere spreiding
plt.xscale("log", base=2)

# labels
plt.title("Execution time vs Number of MPI processes")
plt.xlabel("Number of MPI processes")
plt.ylabel("Execution time (seconds)")

plt.grid(True, which="both", linestyle="--", alpha=0.6)

# exact de punten op de x-as
plt.xticks(processes, processes)

plt.tight_layout()
plt.savefig("mpi_performance.png", dpi=300)

plt.show()