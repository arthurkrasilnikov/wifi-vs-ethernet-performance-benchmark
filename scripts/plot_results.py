import matplotlib.pyplot as plt
import numpy as np
import os

# Create figures directory if it doesn't exist
os.makedirs('../figures', exist_ok=True)

# Empirical benchmark data
scenarios = ['ETH_01', 'W50_A', 'W24_A', 'W50_B', 'W24_B', 'W50_C', 'W24_C', 'W24_INT']
labels = [
    'Ethernet\n(Baseline)', 
    '5GHz (A)\n(1m LOS)', 
    '2.4GHz (A)\n(1m LOS)', 
    '5GHz (B)\n(5m 1-wall)', 
    '2.4GHz (B)\n(5m 1-wall)', 
    '5GHz (C)\n(10m 2-walls)', 
    '2.4GHz (C)\n(10m 2-walls)', 
    '2.4GHz (INT)\n(Interference)'
]

tcp_throughput = [92.7, 89.1, 52.2, 86.9, 52.7, 44.4, 23.6, 20.7]
udp_throughput = [95.5, 95.5, 70.1, 87.5, 57.5, 61.6, 30.3, 31.3]
jitter = [0.021, 0.601, 0.156, 0.232, 5.428, 0.284, 0.344, 1.620]

x = np.arange(len(scenarios))
width = 0.35

# 1. Throughput Comparison Plot
fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width/2, tcp_throughput, width, label='Peak TCP Throughput (Mbps)', color='#1f77b4')
rects2 = ax.bar(x + width/2, udp_throughput, width, label='Actual UDP Throughput (Mbps)', color='#2ca02c')

ax.set_ylabel('Throughput (Mbps)', fontsize=12)
ax.set_title('Network Throughput Comparison: Wi-Fi (802.11n/ac) vs Fast Ethernet Baseline', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9)
ax.legend(fontsize=11)
ax.set_ylim(0, 110)
ax.grid(axis='y', linestyle='--', alpha=0.7)

for rect in rects1 + rects2:
    height = rect.get_height()
    ax.annotate(f'{height}',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('../figures/throughput_benchmark.png', dpi=300)
plt.close()

# 2. Jitter Comparison Plot
fig, ax2 = plt.subplots(figsize=(10, 5))
bars = ax2.bar(labels, jitter, color='#d62728', width=0.5)
ax2.set_ylabel('Average Jitter (ms)', fontsize=12)
ax2.set_title('Packet Jitter Across Test Scenarios', fontsize=14, fontweight='bold')
ax2.set_xticklabels(labels, fontsize=9)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval:.3f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('../figures/jitter_benchmark.png', dpi=300)
plt.close()