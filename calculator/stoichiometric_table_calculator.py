import tkinter as tk

def calculate():
    result_text.delete(1.0, tk.END)
    result_matrix = []
    conv = float(conv_entry.get())

    # Check if conversion input is less than or equal to 1
    if conv > 1:
        result_text.insert(tk.END, "Error: Invalid conversion value. Conversion value should be less than or equal to 1.")
        return

    if reaction_type.get() == "Flow":
        reactants = int(reactants_entry.get())
        products = int(products_entry.get())
        vol_flow = float(vol_flow_entry.get())
        reactants_coeff = []
        products_coeff = []
        molar_flow_reactants = []
        molar_flow_products = []

        for i in range(0, reactants):
            a = -int(reactant_coeff_entries[i].get())
            a_v = int(molar_flow_reactants_entries[i].get())
            reactants_coeff.append(a)
            molar_flow_reactants.append(a_v)

        for n in range(0, products):
            b = int(product_coeff_entries[n].get())
            b_v = int(molar_flow_products_entries[n].get())
            products_coeff.append(b)
            molar_flow_products.append(b_v)

        reactants_conc = []
        products_conc = []

        for i in range(0, reactants):
            c = molar_flow_reactants[i] / vol_flow
            reactants_conc.append(c)

        for n in range(0, products):
            c = molar_flow_products[n] / vol_flow
            products_conc.append(c)

        conc_ratio = []

        for i in range(0,reactants):
            ratio = reactants_conc[i]/reactants_coeff[i]
            conc_ratio.append(ratio)
        
        max_ratio = max(conc_ratio)
        max_index = conc_ratio.index(max_ratio)

        theta = []

        for i in range(0, reactants):
            t = reactants_conc[i] / reactants_conc[max_index]
            theta.append(t)
        
        for n in range(0, products):
            t = products_conc[n] / reactants_conc[max_index]
            theta.append(t)

        result_text.insert(tk.END, "Results:\n")
        result_text.insert(tk.END, "| Initial | Change | Remaining |\n")
        for i in range(0, reactants+products):
            if i < reactants:
                int_ = reactants_conc[i]
                change = - reactants_coeff[i]*conv*reactants_conc[max_index]/reactants_coeff[max_index]
                remain = int_ + change
                list_ = [int_, change, remain]
                result_matrix.append(list_)
            else:
                int_ = products_conc[i - reactants]
                change = - products_coeff[i - reactants]*conv*reactants_conc[max_index]/reactants_coeff[max_index]
                remain = int_ + change
                list_ = [int_, change, remain]
                result_matrix.append(list_)
            result_text.insert(tk.END, f"| {int_} | {change} | {remain} |\n")

    elif reaction_type.get() == "Batch":
        reactants = int(reactants_entry.get())
        products = int(products_entry.get())
        vol = float(vol_entry.get())
        reactants_coeff = []
        products_coeff = []
        mole_reactants = []
        mole_products = []

        for i in range(0, reactants):
            a = -int(reactant_coeff_entries[i].get())
            a_v = int(mole_reactants_entries[i].get())
            reactants_coeff.append(a)
            mole_reactants.append(a_v)

        for n in range(0, products):
            b = int(product_coeff_entries[n].get())
            b_v = int(mole_products_entries[n].get())
            products_coeff.append(b)
            mole_products.append(b_v)

        reactants_conc = []
        products_conc = []

        for i in range(0, reactants):
            c = mole_reactants[i] / vol
            reactants_conc.append(c)

        for n in range(0, products):
            c = mole_products[n] / vol
            products_conc.append(c)
        
        conc_ratio = []

        for i in range(0,reactants):
            ratio = reactants_conc[i]/reactants_coeff[i]
            conc_ratio.append(ratio)
        max_ratio = max(conc_ratio)
        max_index = conc_ratio.index(max_ratio)

        theta = []

        for i in range(0, reactants):
            t = reactants_conc[i] / reactants_conc[max_index]
            theta.append(t)
        
        for n in range(0, products):
            t = products_conc[n] / reactants_conc[max_index]
            theta.append(t)

        result_text.insert(tk.END, "Results:\n")
        result_text.insert(tk.END, "Reaction Matrix:\n")
        result_text.insert(tk.END, "| Initial | Change | Remaining |\n")
        for i in range(0, reactants+products):
            if i < reactants:
                int_ = reactants_conc[i]
                change = - reactants_coeff[i]*conv*reactants_conc[max_index]/reactants_coeff[max_index]
                remain = int_ + change
                list_ = [int_, change, remain]
                result_matrix.append(list_)
            else:
                int_ = products_conc[i - reactants]
                change = - products_coeff[i - reactants]*conv*reactants_conc[max_index]/reactants_coeff[max_index]
                remain = int_ + change
                list_ = [int_, change, remain]
                result_matrix.append(list_)
            result_text.insert(tk.END, f"| {int_} | {change} | {remain} |\n")

def update_entries(*args):
    if reaction_type.get() == "Flow":
        vol_flow_label = tk.Label(frame, text="Enter volumetric flow rate:")
        vol_flow_label.pack()
        global vol_flow_entry
        vol_flow_entry = tk.Entry(frame, width=20)
        vol_flow_entry.pack()
        for i in range(int(reactants_entry.get())):
            reactant_coeff_label = tk.Label(frame, text=f"Enter Coefficient of Reactant {i+1}:")
            reactant_coeff_label.pack()
            reactant_coeff_entry = tk.Entry(frame, width=20)
            reactant_coeff_entry.pack()
            reactant_coeff_entries.append(reactant_coeff_entry)

            molar_flow_reactants_label = tk.Label(frame, text=f"Enter molar flow rate of Reactant {i+1} entering reactor:")
            molar_flow_reactants_label.pack()
            molar_flow_reactants_entry = tk.Entry(frame, width=20)
            molar_flow_reactants_entry.pack()
            molar_flow_reactants_entries.append(molar_flow_reactants_entry)

        for i in range(int(products_entry.get())):
            product_coeff_label = tk.Label(frame, text=f"Enter Coefficient of Product {i+1}:")
            product_coeff_label.pack()
            product_coeff_entry = tk.Entry(frame, width=20)
            product_coeff_entry.pack()
            product_coeff_entries.append(product_coeff_entry)

            molar_flow_products_label = tk.Label(frame, text=f"Enter molar flow rate of Product {i+1} entering reactor:")
            molar_flow_products_label.pack()
            molar_flow_products_entry = tk.Entry(frame, width=20)
            molar_flow_products_entry.pack()
            molar_flow_products_entries.append(molar_flow_products_entry)

    elif reaction_type.get() == "Batch":
        vol_label = tk.Label(frame, text="Enter volume:")
        vol_label.pack()
        global vol_entry
        vol_entry = tk.Entry(frame, width=20)
        vol_entry.pack()
        for i in range(int(reactants_entry.get())):
            reactant_coeff_label = tk.Label(frame, text=f"Enter Coefficient of Reactant {i+1}:")
            reactant_coeff_label.pack()
            reactant_coeff_entry = tk.Entry(frame, width=20)
            reactant_coeff_entry.pack()
            reactant_coeff_entries.append(reactant_coeff_entry)

            mole_reactants_label = tk.Label(frame, text=f"Enter mole of Reactant {i+1} entering reactor:")
            mole_reactants_label.pack()
            mole_reactants_entry = tk.Entry(frame, width=20)
            mole_reactants_entry.pack()
            mole_reactants_entries.append(mole_reactants_entry)

        for i in range(int(products_entry.get())):
            product_coeff_label = tk.Label(frame, text=f"Enter Coefficient of Product {i+1}:")
            product_coeff_label.pack()
            product_coeff_entry = tk.Entry(frame, width=20)
            product_coeff_entry.pack()
            product_coeff_entries.append(product_coeff_entry)

            mole_products_label = tk.Label(frame, text=f"Enter mole of Product {i+1} entering reactor:")
            mole_products_label.pack()
            mole_products_entry = tk.Entry(frame, width=20)
            mole_products_entry.pack()
            mole_products_entries.append(mole_products_entry)

def reset_entries():
    result_text.delete(1.0, tk.END)
    reactant_coeff_entries.clear()
    product_coeff_entries.clear()
    molar_flow_reactants_entries.clear()
    molar_flow_products_entries.clear()
    mole_reactants_entries.clear()
    mole_products_entries.clear()

    for widget in frame.winfo_children():
        if widget not in [conv_label, conv_entry, reactants_label, reactants_entry, products_label, products_entry, reaction_type_label, reaction_type_dropdown, calculate_button, result_text, reset_button]:
            widget.destroy()

def _on_mouse_wheel(event):
    canvas.yview_scroll(-1*(event.delta//120), "units")

root = tk.Tk()
root.title("Reaction Type Calculator")
root.attributes("-fullscreen", True)  # Open the window in full screen

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor="nw")

conv_label = tk.Label(frame, text="Enter conversion:")
conv_label.pack()
conv_entry = tk.Entry(frame, width=20)
conv_entry.pack()

reactants_label = tk.Label(frame, text="Enter total number of reactants:")
reactants_label.pack()
reactants_entry = tk.Entry(frame, width=20)
reactants_entry.pack()

products_label = tk.Label(frame, text="Enter total number of products:")
products_label.pack()
products_entry = tk.Entry(frame, width=20)
products_entry.pack()

reaction_type_label = tk.Label(frame, text="Select Reactor Type:")
reaction_type_label.pack()
reaction_type = tk.StringVar()
reaction_type_dropdown = tk.OptionMenu(frame, reaction_type, "Flow", "Batch")
reaction_type_dropdown.pack()

reaction_type.trace_add("write", update_entries)

reactant_coeff_entries = []
molar_flow_reactants_entries = []
product_coeff_entries = []
molar_flow_products_entries = []
mole_reactants_entries = []
mole_products_entries = []

calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.pack()

result_text = tk.Text(frame, height=20, width=80) 
result_text.pack()

reset_button = tk.Button(frame, text="Reset", command=reset_entries)
reset_button.pack()

canvas.bind("<MouseWheel>", _on_mouse_wheel)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=canvas.yview)

root.mainloop()
