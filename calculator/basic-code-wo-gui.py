type = input("Enter Reaction Type (Flow or Batch)- ")
conv = float(input("Enter conversion- "))

if type == "Flow":
    reactants = int(input("Enter total number of reactants- "))
    products = int(input("Enter total number of products- "))
    vol_flow = float(input("Enter volumetric flow rate- "))
    reactants_coeff = []
    products_coeff = []
    molar_flow_reactants = []
    molar_flow_products = []

    for i in range(0, reactants):
        a = -int(input("Enter Coefficient of Reactant- "))
        a_v = int(input("Enter molar flow rate of Reactant entering reactor- "))
        reactants_coeff.append(a)
        molar_flow_reactants.append(a_v)

    for n in range(0, products):
        b = int(input("Enter Coefficient of Product- "))
        b_v = int(input("Enter molar flow rate of Product entering reactor- "))
        products_coeff.append(b)
        molar_flow_products.append(b_v)

    reactants_conc = []
    products_conc = []

    for i in range(0, reactants):
        c = molar_flow_reactants[i]/vol_flow
        reactants_conc.append(c)

    for n in range(0, products):
        c = molar_flow_products[i]/vol_flow
        products_conc.append(c)

    theta = []

    for i in range(0, reactants):
        t = reactants_conc[i]/reactants_conc[0]
        theta.append(t)
    
    for n in range(0, products):
        t = products_conc[i]/reactants_conc[0]
        theta.append(t)

    for i in range(0, reactants+products):
        if i < reactants:
            f = molar_flow_reactants[0]*(theta[i] - reactants_coeff[i]*conv/reactants_coeff[0])
        else:
            f = molar_flow_reactants[0]*(theta[i] - products_coeff[i-reactants]*conv/reactants_coeff[0])
        print("F", i, "= ", f)

if type == "Batch":
    reactants = int(input("Enter total number of reactants- "))
    products = int(input("Enter total number of products- "))
    vol = float(input("Enter volume- "))
    reactants_coeff = []
    products_coeff = []
    mole_reactants = []
    mole_products = []

    for i in range(0, reactants):
        a = -int(input("Enter Coefficient of Reactant- "))
        a_v = int(input("Enter mole of Reactant entering reactor- "))
        reactants_coeff.append(a)
        mole_reactants.append(a_v)

    for n in range(0, products):
        b = int(input("Enter Coefficient of Product- "))
        b_v = int(input("Enter mole of Product entering reactor- "))
        products_coeff.append(b)
        mole_products.append(b_v)

    reactants_conc = []
    products_conc = []

    for i in range(0, reactants):
        c = mole_reactants[i]/vol
        reactants_conc.append(c)

    for n in range(0, products):
        c = mole_products[i]/vol
        products_conc.append(c)

    theta = []

    for i in range(0, reactants):
        t = reactants_conc[i]/reactants_conc[0]
        theta.append(t)
    
    for n in range(0, products):
        t = products_conc[i]/reactants_conc[0]
        theta.append(t)

    for i in range(0, reactants+products):
        if i < reactants:
            f = mole_reactants[0]*(theta[i] - reactants_coeff[i]*conv/reactants_coeff[0])
        else:
            f = mole_reactants[0]*(theta[i] - products_coeff[i-reactants]*conv/reactants_coeff[0])
        print("F", i, "= ", f)
