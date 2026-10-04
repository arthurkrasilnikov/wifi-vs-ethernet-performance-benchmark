# wifi-vs-ethernet-performance-benchmark
Empirical performance evaluation of 802.11n/ac vs Fast Ethernet using automated iperf3 benchmarks.
# Empirical Evaluation of 802.11n/ac Wireless Performance vs Fast Ethernet Baseline

## Overview
This study provides an empirical benchmark evaluating transport-layer performance metrics (TCP throughput, UDP capacity, jitter, and packet loss) across IEEE 802.11n (2.4 GHz) and IEEE 802.11ac (5.0 GHz) compared against a 100BASE-TX Fast Ethernet wired baseline.

Measurements were gathered using an automated CLI workflow (`iperf3`, Windows Native WLAN API) under controlled spatial variations, structural wall penetration, and intentional non-Wi-Fi ISM band interference.

## Hardware & Environment Setup
* **Access Point / L2 Switch:** TP-Link Archer C20 v5.0 (Dual-Band, 4× 100BASE-TX MII Fast Ethernet LAN ports).
* **Client Interface:** Realtek 8821AE Wireless LAN 802.11ac PCIe Adapter (1×1 SISO configuration).
* **RF Parameters:**
  * **2.4 GHz:** Channel 10, 20/40 MHz bandwidth, 802.11n standard (PHY rate: 150.0 Mbps).
  * **5.0 GHz:** Channel 44 (UNII-1), 80 MHz bandwidth, 802.11ac standard (PHY rate: 433.3 Mbps).
* **Wired Reference:** Cat 5e direct patch cable operating at 100BASE-TX Full Duplex.

## Methodology & Reproducibility
* **RSSI Telemetry:** Polled via `netsh wlan show interfaces` and normalized using:
  $$\text{RSSI (dBm)} = \frac{\text{Signal Strength (\%)}}{2} - 100$$
* **UDP Benchmarks:** Three independent 20-second runs per scenario at 50 Mbps and 100 Mbps target load to quantify jitter and frame drop rate.
* **TCP Benchmarks:** 15-second socket streams to measure peak transport-layer saturation throughput.
* **Automation:** Managed via PowerShell/batch scripts (`scripts/run_benchmarks.bat`), with analytical figures rendered via Matplotlib (`scripts/plot_results.py`).

### Reproduce Figures
```bash
pip install matplotlib numpy
python scripts/plot_results.py
Benchmark ResultsTest IDMedium / StandardPhysical Location / ConditionRSSI (dBm)Avg Jitter (ms)Packet Loss (%)Actual UDP (Mbps)Peak TCP (Mbps)ETH_01Fast Ethernet (Cat 5e)Baseline (1m from AP, Wired)00.0210.02%95.5092.70W50_A802.11ac (5.0 GHz)Point A (1m, Line-of-Sight)-500.6014.31%95.5089.10W24_A802.11n (2.4 GHz)Point A (1m, Line-of-Sight)-500.1568.38%70.1052.20W50_B802.11ac (5.0 GHz)Point B (5m, Single Interior Wall)-500.23211.98%87.4786.90W24_B802.11n (2.4 GHz)Point B (5m, Single Interior Wall)-505.4280.01%57.5052.70W50_C802.11ac (5.0 GHz)Point C (10m, Multiple Walls)-680.2840.32%61.6344.40W24_C802.11n (2.4 GHz)Point C (10m, Multiple Walls)-500.3440.01%30.3323.60W24_INT802.11n (2.4 GHz)Point C + Active RF Interference-51.51.6200.00%31.3320.70VisualizationsThroughput ComparisonLatency Jitter ProfileKey Technical FindingsPhysical Switching Bottleneck: In Point A, 5.0 GHz 802.11ac reached 95.50 Mbps UDP / 89.10 Mbps TCP, matching the wired baseline. Despite a 433.3 Mbps PHY air link rate, application throughput was strictly bounded by the AP's physical 100BASE-TX Fast Ethernet MII interface.Frequency Attenuation & Path Loss: 5.0 GHz suffered substantial RF attenuation through multiple interior walls (-50 dBm to -68 dBm, forcing lower MCS index states), resulting in a 50.1% decrease in TCP throughput. Conversely, 2.4 GHz maintained RSSI stability (-50 dBm) due to longer wavelength propagation, but provided lower overall throughput due to narrower spectral bandwidth.Interference & CSMA/CA Backoff: Under 2.4 GHz non-Wi-Fi ISM band noise (W24_INT), average jitter increased nearly fivefold (0.344 ms to 1.620 ms, with peak spikes at 3.89 ms), dropping TCP throughput to 20.70 Mbps due to link-layer frame retransmissions and channel contention.
