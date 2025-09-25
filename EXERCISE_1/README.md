
---

# IT Asset Management Summary - Python Project

## Overview

This Python project demonstrates the use of **basic data types and data structures**—integers, strings, booleans, lists, arrays, and dictionaries—for managing IT asset information. The script calculates asset values, generates reports, performs checks, and manipulates data efficiently.

---

## Features

1. **Integer Operations**

   * Calculate total, average, minimum, and maximum values of IT assets.
   * Handles computations for multiple asset types.

2. **String Operations**

   * Generates a formatted **IT Asset Register Summary**.
   * Displays asset types, total quantity, total value, and average asset value.

3. **Boolean Checks**

   * Compares asset values against a threshold.
   * Determines if the IT assets are **above or below standard**.

4. **List Operations**

   * Maintains a list of asset types.
   * Allows adding new asset types.
   * Sorts the list alphabetically for better readability.

5. **Array Operations**

   * Uses the `array` module for numeric calculations.
   * Performs arithmetic operations on asset values efficiently.

6. **Dictionary Operations**

   * Stores detailed asset records with IDs, values, and locations.
   * Updates and deletes records dynamically.
   * Computes total value from structured records.

---

## Project Structure

* **quantities**: A list of quantities for each asset type.
* **unit\_costs**: The cost per asset.
* **total\_values**: Computed total value per asset.
* **report**: A formatted string showing asset summary.
* **assets**: List of asset names with dynamic updates and sorting.
* **asset\_array**: Array storing numeric values for computation.
* **asset\_records**: List of dictionaries representing detailed asset records.

---

## How to Run

1. Ensure you have Python installed (Python 3.x recommended).
2. Save the script as `it_asset_management.py`.
3. Open a terminal or command prompt.
4. Run the script using:

```bash
python it_asset_management.py
```

5. Observe outputs for:

   * Total, average, min, max asset values
   * Formatted IT asset summary
   * Status checks
   * Updated asset lists
   * Array arithmetic results
   * Updated asset records

---

## Example Output

```
Integer Operations
Total Value: 16100 USD
Average Value: 4025.00 USD
Minimum Value: 2400 USD
Maximum Value: 6000 USD

IT Asset Register Summary
----------------------------
Asset Types: Laptop, Printer, Router, Monitor
Total Quantity: 35 items
Total Value: 16100 USD
Average Asset Value: 4025.00 USD

Status Check: Below Standard

Asset List Before Sort: ['Laptop', 'Printer', 'Router', 'Monitor', 'Scanner']
Asset List After Sort: ['Laptop', 'Monitor', 'Printer', 'Router', 'Scanner']

array Arithmetic
Original Array: [5000, 6000, 6000, 3600]
Array After Adding 100 to Each: [5100, 6100, 6100, 3700]

Dictionary Operations
Updated Records: [{'id': 101, 'value': 5000, 'location': 'HQ'}, {'id': 102, 'value': 6500, 'location': 'Branch A'}]
Total Value from Records: 11500 USD
```

---

## Dependencies

* Python Standard Library only (`array` module used).

---

## Author

**Austine Odiwuor**
Kilimo Asilia Africa LTD.

---
