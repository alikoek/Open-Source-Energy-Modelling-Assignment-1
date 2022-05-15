import pandas as pd

def balance_sup_dem(supply_data_py:pd.DataFrame, demand_data_py:pd.DataFrame):
    new_cap = []
    if supply_data_py.cap.sum() > demand_data_py.cap.sum():
        for i in supply_data_py.cap:
            z = i
            diff = supply_data_py.cap.sum() - demand_data_py.cap.sum()
            share = z / supply_data_py.cap.sum()
            z = z - (diff * share)
            new_cap.append(z)
        supply_data_py.cap = new_cap
    elif supply_data_py.cap.sum() < demand_data_py.cap.sum():
        for i in demand_data_py.cap:
            z = i
            diff = demand_data_py.cap.sum() - supply_data_py.cap.sum()
            share = z / demand_data_py.cap.sum()
            z = z - (diff * share)
            new_cap.append(z)
        demand_data_py.cap = new_cap
    else:
        print(f"supply capacity:{supply_data_py.cap.sum()} == demand capacity:{demand_data_py.cap.sum()}\nNo need to adapt capacities!")
    return supply_data_py, demand_data_py