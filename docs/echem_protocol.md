# Electrochemical Assay Notes

Protocols, tips, and setup for running electrochemical assays with the Lifeline system.

## Hardware Setup

- ESP32-WROOM microcontroller
- LM358 op-amp circuit (see /hardware/schematics/)
- Electrochemical test strip or probe
- ADC (optionally ADS1115/MCP3008 for high precision)

## Assay Types Supported

- Amperometric (current-based)
- Voltammetric (voltage sweep)
- Potentiometric (potential measurement)

## General Procedure

1. **Connect EC test strip to op-amp circuit.**
2. **Configure ESP32 for analog readout (ADC input).**
3. **Calibrate using known standards or blank samples.**
4. **Collect sample data, stream to Raspberry Pi for analysis.**
5. **Analyze signal for target biomarker detection.**

## Safety & Calibration

- Always calibrate with blank and known control solutions.
- Clean or replace electrodes between runs.
