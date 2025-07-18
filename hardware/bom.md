# Bill of Materials (BOM) — Lifeline Diagnostic Kit

A detailed list of hardware components, electronics, and consumables needed for a single Lifeline device. Prices are approximate and may vary by region or supplier.

---

## Core Electronics

| Part Name             | Description                                              | Example Supplier / Link                               | Qty | Est. Cost (USD) | Notes                          |
|-----------------------|----------------------------------------------------------|-------------------------------------------------------|-----|-----------------|--------------------------------|
| Raspberry Pi 4 (2GB+) | Single-board computer, main controller                   | [Raspberry Pi](https://www.raspberrypi.com/)          | 1   | $45             | 2GB or 4GB RAM; get heatsink   |
| 32GB microSD Card     | OS & data storage                                        | Amazon, SanDisk, Samsung                              | 1   | $7              | High endurance preferred       |
| 5” DSI Touchscreen    | 800x480 capacitive display                               | Waveshare, Amazon                                     | 1   | $40             | DSI interface for Pi           |
| Raspberry Pi Camera v2| Camera for image analysis                                | [Official Pi Camera](https://www.raspberrypi.com/)    | 1   | $20             | Ribbon cable included          |
| ESP32-WROOM Board     | Wi-Fi/BLE MCU for sensors, ADC                           | HiLetgo, AZDelivery, Amazon                           | 1   | $10             | Micro-USB interface            |
| AMS1117 Regulator     | 3.3V voltage regulator                                   | Amazon, eBay                                          | 2   | $5 (pack)        | For ESP32, sensors             |
| L298N Motor Driver    | Motor controller for pump                                | Amazon, eBay                                          | 1   | $7              | Dual channel                   |
| Peristaltic Pump (12V)| Fluid dosing, sample handling                            | Amazon, OUKANING, Adafruit                            | 1   | $15             | With silicone tubing           |
| Anker Power Bank (10K)| 5V/3A USB power, portable                                | Amazon                                                | 1   | $25             | Or similar                     |

---

## Sensors & Analog Components

| Part Name          | Description                                  | Example Supplier / Link             | Qty | Est. Cost (USD) | Notes                   |
|--------------------|----------------------------------------------|-------------------------------------|-----|-----------------|-------------------------|
| BPW34 Photodiode   | Light/color detection for μPADs              | Amazon, Digi-Key, Mouser            | 2   | $6 (pair)       | Visible/NIR sensitive   |
| LM358 Op-Amp       | EC sensor interface, amplification           | Amazon, eBay, SparkFun              | 2   | $6 (pack)       | DIP package preferred   |
| 0.96” OLED (I2C)   | ESP32-side debugging display                 | Amazon, Adafruit                    | 1   | $7              | SSD1306 compatible      |
| Conductive Ink Pen | Draw μPAD circuits/test strips               | CircuitScribe, Amazon               | 2   | $20 (2-pack)    | Silver or carbon ink    |
| Premium Filter Paper| Microfluidic paper, μPAD base                | Whatman #1, Amazon                  | 1   | $15 (100 sheets)| A4, can be cut to size  |
| Breadboards        | Prototyping                                  | Amazon                              | 2   | $8 (pair)       | 400+ point              |
| Jumper Wires       | Prototyping                                  | Amazon, Elegoo                      | 1   | $7 (120pcs)     | M-M, M-F, F-F           |
| Dupont Cables      | Prototyping                                  | Amazon                              | 1   | $5 (pack)       | For sensor connection   |
| LEDs, Resistors, Caps| Common circuit elements                    | Amazon, eBay                        | 1   | $12 (kit)       | Mixed value pack        |
| Small Screwdriver Set | Assembly/adjustment tools                 | Amazon, iFixit                      | 1   | $10             | Useful for enclosures   |

---

## Consumables & Testing

| Part Name           | Description                           | Example Supplier / Link        | Qty  | Est. Cost (USD) | Notes                    |
|---------------------|---------------------------------------|-------------------------------|------|-----------------|--------------------------|
| Trueplus 28G Lancets| Capillary blood sampling               | Amazon, Walmart               | 50   | $8              | Any 28G compatible brand |
| Alcohol Wipes       | Cleaning sample area                   | Amazon, Walgreens             | 50   | $5              |                          |
| Disposable Gloves   | Safe sample handling                   | Amazon                        | 100  | $9              | Nitrile preferred        |
| Micro-pipettes      | Precision droplet application          | Amazon                        | 5    | $12             | 20–200μL                 |
| Microcentrifuge Tubes| Test/control sample storage           | Amazon                        | 50   | $8              | 1.5 or 2 mL              |
| Double-sided Tape   | Temporary mounting                     | Amazon                        | 1    | $5              |                          |
| Zip Ties/Velcro     | Cable and component management         | Amazon                        | 1    | $4              |                          |

---

## Optional / Advanced

| Part Name              | Description                             | Example Supplier / Link  | Qty | Est. Cost (USD) | Notes                         |
|------------------------|-----------------------------------------|--------------------------|-----|-----------------|-------------------------------|
| ADS1115 or MCP3008 ADC | High-precision analog readout           | Amazon, Adafruit         | 1   | $12             | For EC/analog accuracy         |
| 3D Printer Filament    | For custom enclosure                    | Amazon                   | 1   | $22             | PLA/ABS, or use print service  |
| Blank Project Enclosure| Electronics case                        | Amazon                   | 1   | $15             | Can 3D print or buy ready-made |
| Extension Cord/Power Strip| For demo setup                      | Amazon                   | 1   | $10             |                               |

---

## Total Estimated Cost per Kit: ~$300 (with spares, tools, and extras)

*Many components can be reused or substituted. Prices are for reference only and may change.*

---

## Notes

- For detailed suppliers, see links and resources in `/docs/sourcing.md`
- Consider medical-grade versions for clinical/patent deployment
- Backup/spare units recommended for all critical electronics