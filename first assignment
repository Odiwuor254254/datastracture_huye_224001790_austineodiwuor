import array

# -------------------------------
#  Integers: Quantities & Costs
# -------------------------------
quantities = [10, 5, 8, 12]  # Laptops, Printers, Routers, Monitors
unit_costs = [500, 1200, 750, 300]  # USD per item

# Calculate total value per asset type
total_values = [q * c for q, c in zip(quantities, unit_costs)]

print(" Integer Operations")
print(f"Total Value: {sum(total_values)} USD")
print(f"Average Value: {sum(total_values)/len(total_values):.2f} USD")
print(f"Minimum Value: {min(total_values)} USD")
print(f"Maximum Value: {max(total_values)} USD\n")

# -------------------------------
#  Strings: Formatted Report
# -------------------------------
report = f"""
 IT Asset Register Summary
----------------------------
Asset Types: Laptop, Printer, Router, Monitor
Total Quantity: {sum(quantities)} items
Total Value: {sum(total_values)} USD
Average Asset Value: {sum(total_values)/len(total_values):.2f} USD
"""
print(report)

# -------------------------------
#  Booleans: Threshold Check
# -------------------------------
threshold = 6000
average_value = sum(total_values)/len(total_values)

if average_value > threshold and max(total_values) > threshold:
    print(" Status Check: Above Standard\n")
else:
    print(" Status Check: Below Standard\n")

# -------------------------------
#  Lists: Asset Names & Sorting
# -------------------------------
assets = ["Laptop", "Printer", "Router", "Monitor"]
new_asset = "Scanner"

if new_asset not in assets:
    assets.append(new_asset)

print(" Asset List Before Sort:", assets)
assets.sort()
print(" Asset List After Sort:", assets, "\n")

# -------------------------------
#  Arrays: Numeric Subset Ops
# -------------------------------
asset_array = array.array('i', total_values)
print("array Arithmetic")
print("Original Array:", asset_array.tolist())

added_array = array.array('i', [x + 100 for x in asset_array])
print("Array After Adding 100 to Each:", added_array.tolist(), "\n")

# -------------------------------
#  Dictionaries: Asset Records
# -------------------------------
asset_records = [
    {"id": 101, "value": 5000, "location": "HQ"},
    {"id": 102, "value": 6000, "location": "Branch A"},
    {"id": 103, "value": 3000, "location": "Branch B"}
]

# Update Branch A value
asset_records[1]["value"] = 6500

# Delete Branch B record
del asset_records[2]

# Compute total value from records
total_record_value = sum(record["value"] for record in asset_records)

print(" Dictionary Operations")
print("Updated Records:", asset_records)
print("Total Value from Records:", total_record_value, "USD")
