# System Architecture and Workflow

This document provides a high-level overview of the Lifeline Diagnostic Kit's architecture and operational workflow.

## System Overview

- **Hardware Components:** Raspberry Pi 4, ESP32-WROOM, Pi Camera, Touchscreen, Peristaltic Pump, Photodiodes, LM358 Op-amp, and custom μPAD test strips.
- **Core Functions:** Image-based μPAD analysis, electrochemical sensing, real-time AI feedback, technician and patient UI.
- **Data Flow:** Blood sample -> μPAD/EC input -> Sensor/camera readout -> Data processing on Pi -> Local AI analysis -> User feedback via dashboard.

## Operational Workflow

1. **Sample Collection:** Capillary blood via lancet onto μPAD or EC test strip.
2. **Sensing:** Pi camera captures μPAD, ESP32 reads analog EC signals.
3. **Data Transmission:** ESP32 sends sensor data via serial/Wi-Fi to Pi.
4. **Processing:** Pi runs OpenCV and analysis scripts, interfaces with local LLM.
5. **Feedback:** Results shown on touchscreen dashboard, optional patient summary.

## Block Diagram

*(Insert block diagram or schematic image here)*

## Expandability

- Modular design for additional tests, sensors, or communication protocols.
