# Lifeline Diagnostic Kit

A low-cost, modular diagnostic system for blood analysis at the point of care. Lifeline leverages Raspberry Pi and ESP32 hardware to analyze capillary blood samples using both μPAD (microfluidic paper-based analytical device) colorimetric sensing and electrochemical detection, powered by on-device AI for real-time health insights. Designed for accessible, scalable, and secure diagnostic testing in a portable format.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Hardware Components](#hardware-components)
- [Software Stack](#software-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Bill of Materials](#bill-of-materials)
- [Documentation](#documentation)
- [Patent & Research Notes](#patent--research-notes)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

**Lifeline** is a hybrid hardware-software diagnostic kit designed for rapid, point-of-care blood analysis. The system combines disposable microfluidic paper-based strips for colorimetric testing with electrochemical assay capabilities, using affordable and widely available electronics. All sample analysis and AI-powered interpretation are performed *locally* on-device, ensuring privacy, speed, and resilience in any setting.

---

## Features

- **μPAD colorimetric sensing:** Rapid color-based analysis using custom test strips and Pi Camera + OpenCV
- **Electrochemical detection:** High-sensitivity analog readings via ESP32 and LM358 op-amp circuits
- **On-device AI analysis:** Private, real-time feedback using a local language model (Gemma 3n or similar)
- **Modern dashboard UI:** Flask or Streamlit web interface for technicians and users
- **Modular and open hardware:** Easy to modify, scale, or adapt to new tests
- **Portable and battery-powered:** Runs for hours from a standard USB power bank

---

## Hardware Components

- **Raspberry Pi 4** (2GB+ RAM) with 5” capacitive touchscreen
- **Raspberry Pi Camera Module v2**
- **ESP32-WROOM** microcontroller for sensor interfacing
- **Peristaltic dosing pump** with L298N motor driver
- **Premium filter paper** for μPADs (microfluidic paper-based analytical devices)
- **Conductive ink pen** for custom circuit/test strip fabrication
- **LM358 op-amp** for electrochemical sensor interface
- **Photodiodes** (BPW34 or similar) for light-based color detection
- **0.96” OLED display** (optional, for debugging ESP32 firmware)
- **Breadboards, jumper wires, power bank, and other basic electronics**

---

## Software Stack

- **Python 3.9+** (for main control, image analysis, dashboard)
- **Flask** or **Streamlit** (for local UI/dashboard)
- **OpenCV** (image processing for μPAD analysis)
- **pySerial** (Pi-to-ESP32 communication)
- **Ollama** or **local LLM runner** (for AI-powered feedback)
- **ESP32 Arduino firmware** (sensor readout, serial comms)
- **Optional:** Jetson Nano for accelerated inference

---

## Repository Structure
/hardware/         # Schematics, PCB files, BOM, hardware photos
/software/         # Raspberry Pi, ESP32, and analysis scripts
/dashboards/       # UI code (Flask/Streamlit/PyQt)
/docs/             # Design docs, protocol notes, research, provisional patent
/images/           # Demo/build images, UI screenshots
/tests/            # Sensor/data test scripts and datasets
README.md
---

## Getting Started

**Requirements:**
- Raspberry Pi 4 (2GB+ RAM), running Raspberry Pi OS 64-bit
- ESP32-WROOM dev board
- Camera module, touchscreen, and all core hardware (see [Bill of Materials](#bill-of-materials))
- Python 3.9+ with pip (see `/software/requirements.txt`)
- Arduino IDE for ESP32 firmware

**Quick Start:**
1. Assemble hardware as described in `/hardware/assembly.md`
2. Flash Raspberry Pi OS, enable camera, and install dependencies (`pip install -r requirements.txt`)
3. Upload ESP32 firmware from `/software/esp32_firmware/`
4. Run `python /software/main.py` to start the local dashboard and connect devices
5. Begin sample analysis via dashboard UI

---

## Bill of Materials

See [`/hardware/bom.md`](hardware/bom.md) for detailed part numbers, suppliers, and estimated costs.

---

## Documentation

- System architecture and workflow: `/docs/overview.md`
- μPAD fabrication protocols: `/docs/mupad_protocol.md`
- Electrochemical assay notes: `/docs/echem_protocol.md`
- Provisional patent notes and research: `/docs/patent-notes.md`
- User and technician instructions: `/docs/user_guide.md`

---

## Patent & Research Notes

All novel aspects, including device workflow, test cartridge design, and on-device analysis methods, are documented for potential intellectual property filings. For more, see `/docs/patent-notes.md`.

---

## License

This project is released under the MIT License unless otherwise stated.  
See [`LICENSE`](LICENSE) for details.

---

## Acknowledgements

- Hardware, software, and research contributors (see `/docs/contributors.md`)
- Open-source toolchains and component libraries  
- Medical device design and diagnostics literature

---

*For questions, collaboration, or media inquiries, please contact the repository maintainer.*
