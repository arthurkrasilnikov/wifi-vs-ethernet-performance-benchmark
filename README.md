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
