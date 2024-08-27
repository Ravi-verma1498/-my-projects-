import tkinter as tk
from tkinter import ttk

def calculate_reaction():
    reactor_type = reactor_type_var.get()
    conv = float(conv_entry.get())

    if reactor_type == "Flow":
        reactants = int(reactants_entry.get())
        products = int(products_entry.get())
        vol_flow = float(vol_flow_entry.get())
        reactants_coeff = []
        products_coeff = []
        molar_flow_reactants = []
        molar_flow_products = []

        for i in range(0, reactants):
            a = -int(reactant_coeff_entries[i].get())
            a_v = int(reactant_molar_flow_entries[i].get())
            reactants_coeff.append(a)
            molar_flow_reactants.append(a_v)

        for n in range(0, products):
            b = int(product_coeff_entries[n].get())
            b_v = int(product_molar_flow_entries[n].get())
            products_coeff.append(b)
            molar_flow_products.append(b_v)

        reactants_conc = [molar_flow_reactants[i] / vol_flow for i in range(reactants)]
        products_conc = [molar_flow_products[i] / vol_flow for i in range(products)]

        theta = [reactants_conc[i] / reactants_conc[0] for i in range(reactants)]
        theta += [products_conc[i] / reactants_conc[0] for i in range(products)]

        for i in range(reactants + products):
            if i < reactants:
                f = molar_flow_reactants[0] * (theta[i] - reactants_coeff[i] * conv / reactants_coeff[0])
            else:
                f = molar_flow_reactants[0] * (theta[i] - products_coeff[i - reactants] * conv / reactants_coeff[0])
            result_label = tk.Label(root, text=f"F{i} = {f}")
            result_label.grid(row=i + 6, column=0, padx=10, pady=5)

    elif reactor_type == "Batch":
        reactants = int(reactants_entry.get())
        products = int(products_entry.get())
        vol = float(vol_entry.get())
        reactants_coeff = []
        products_coeff = []
        mole_reactants = []
        mole_products = []

        for i in range(0, reactants):
            a = -int(reactant_coeff_entries[i].get())
            a_v = int(reactant_mole_entries[i].get())
            reactants_coeff.append(a)
            mole_reactants.append(a_v)

        for n in range(0, products):
            b = int(product_coeff_entries[n].get())
            b_v = int(product_mole_entries[n].get())
            products_coeff.append(b)
            mole_products.append(b_v)

        reactants_conc = [mole_reactants[i] / vol for i in range(reactants)]
        products_conc = [mole_products[i] / vol for i in range(products)]

        theta = [reactants_conc[i] / reactants_conc[0] for i in range(reactants)]
        theta += [products_conc[i] / reactants_conc[0] for i in range(products)]

        for i in range(reactants + products):
            if i < reactants:
                f = mole_reactants[0] * (theta[i] - reactants_coeff[i] * conv / reactants_coeff[0])
            else:
                f = mole_reactants[0] * (theta[i] - products_coeff[i - reactants] * conv / reactants_coeff[0])
            result_label = tk.Label(root, text=f"F{i} = {f}")
            result_label.grid(row=i + 6, column=0, padx=10, pady=5)


root = tk.Tk()
root.title("Reactant Calculator")

# Create reactor type dropdown
reactor_type_label = tk.Label(root, text="Select Reactor Type:")
reactor_type_label.grid(row=0, column=0, padx=10, pady=5)
reactor_type_var = tk.StringVar()
reactor_type_dropdown = ttk.Combobox(root, textvariable=reactor_type_var, values=["Flow", "Batch"])
reactor_type_dropdown.grid(row=0, column=1, padx=10, pady=5)

# Reactant and Product Entry
reactants_label = tk.Label(root, text="Enter total number of reactants:")
reactants_label.grid(row=1, column=0, padx=10, pady=5)
reactants_entry = tk.Entry(root)
reactants_entry.grid(row=1, column=1, padx=10, pady=5)

products_label = tk.Label(root, text="Enter total number of products:")
products_label.grid(row=2, column=0, padx=10, pady=5)
products_entry = tk.Entry(root)
products_entry.grid(row=2, column=1, padx=10, pady=5)

# Reactant and Product Coefficient Entries
reactant_coeff_labels = []
reactant_molar_flow_labels = []
reactant_coeff_entries = []
reactant_molar_flow_entries = []
product_coeff_labels = []
product_molar_flow_labels = []
product_coeff_entries = []
product_molar_flow_entries = []

for i in range(3, 3 + int(reactants_entry.get())):
    label = tk.Label(root, text=f"Enter Coefficient of Reactant {i - 2}:")
    label.grid(row=i, column=0, padx=10, pady=5)
    reactant_coeff_labels.append(label)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    reactant_coeff_entries.append(entry)

    label = tk.Label(root, text=f"Enter molar flow rate of Reactant {i - 2}:")
    label.grid(row=i, column=2, padx=10, pady=5)
    reactant_molar_flow_labels.append(label)
    entry = tk.Entry(root)
    entry.grid(row=i, column=3, padx=10, pady=5)
    reactant_molar_flow_entries.append(entry)

for i in range(3 + int(reactants_entry.get()), 3 + int(reactants_entry.get()) + int(products_entry.get())):
    label = tk.Label(root, text=f"Enter Coefficient of Product {i - 2 - int(reactants_entry.get())}:")
    label.grid(row=i, column=0, padx=10, pady=5)
    product_coeff_labels.append(label)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    product_coeff_entries.append(entry)

    label = tk.Label(root, text=f"Enter molar flow rate of Product {i - 2 - int(reactants_entry.get())}:")
    label.grid(row=i, column=2, padx=10, pady=5)
    product_molar_flow_labels.append(label)
    entry = tk.Entry(root)
    entry.grid(row=i, column=3, padx=10, pady=5)
    product_molar_flow_entries.append(entry)

# Define vol_flow_entry
vol_flow_label = tk.Label(root, text="Enter volumetric flow rate:")
vol_flow_label.grid(row=4, column=0, padx=10, pady=5)
vol_flow_entry = tk.Entry(root)
vol_flow_entry.grid(row=4, column=1, padx=10, pady=5)

# Define vol_entry
vol_label = tk.Label(root, text="Enter volume:")
vol_label.grid(row=4, column=2, padx=10, pady=5)
vol_entry = tk.Entry(root)
vol_entry.grid(row=4, column=3, padx=10, pady=5)

# Define reactant_mole_entries
reactant_mole_entries = []
for i in range(3, 3 + int(reactants_entry.get())):
    entry = tk.Entry(root)
    entry.grid(row=i, column=3, padx=10, pady=5)
    reactant_mole_entries.append(entry)

# Define product_mole_entries
product_mole_entries = []
for i in range(3 + int(reactants_entry.get()), 3 + int(reactants_entry.get()) + int(products_entry.get())):
    entry = tk.Entry(root)
    entry.grid(row=i, column=3, padx=10, pady=5)
    product_mole_entries.append(entry)

# Conversion Entry
conv_label = tk.Label(root, text="Enter conversion:")
conv_label.grid(row=3 + int(reactants_entry.get()) + int(products_entry.get()), column=0, padx=10, pady=5)
conv_entry = tk.Entry(root)
conv_entry.grid(row=3 + int(reactants_entry.get()) + int(products_entry.get()), column=1, padx=10, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_reaction)
calculate_button.grid(row=4 + int(reactants_entry.get()) + int(products_entry.get()), column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
