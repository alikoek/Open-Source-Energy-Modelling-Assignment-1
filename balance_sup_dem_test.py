import pandas as pd
import unittest
from functions.balance_sup_dem import balance_sup_dem

### Create test data
## Test data 1: supply > demand
supply_data1 = {
    "coords": {
        1: (39.397222, 22.804167),
        2: (39.393056, 22.803611),
        0: (39.397014, 22.808333249999997),
    },
    "cap": {1: 15, 2: 10, 0: 35},
}
supply_data1 = pd.DataFrame.from_dict(supply_data1)

demand_data1 = {
    "coords": {
        7: (39.398056,22.804167),
        8: (39.397222,22.809444),
        9: (39.396667,22.813889),
        10: (39.396111,22.805833),
    },
    "cap": {7: 5, 8: 10, 9: 12, 10: 8},
}
demand_data1 = pd.DataFrame.from_dict(demand_data1)

## Test data 2: supply < demand
supply_data2 = {
    "coords": {
        1: (39.397222, 22.804167),
        2: (39.393056, 22.803611),
        0: (39.397014, 22.808333249999997),
    },
    "cap": {1: 15, 2: 10, 0: 5},
}
supply_data2 = pd.DataFrame.from_dict(supply_data2)

demand_data2 = {
    "coords": {
        7: (39.398056, 22.804167),
        8: (39.397222, 22.809444),
        9: (39.396667, 22.813889),
        10: (39.396111, 22.805833),
    },
    "cap": {7: 5, 8: 10, 9: 12, 10: 28},
}
demand_data2 = pd.DataFrame.from_dict(demand_data2)

## Test data 3: supply = demand
supply_data3 = {
    "coords": {
        1: (39.397222, 22.804167),
        2: (39.393056, 22.803611),
        0: (39.397014, 22.808333249999997),
    },
    "cap": {1: 15, 2: 10, 0: 5},
}
supply_data3 = pd.DataFrame.from_dict(supply_data3)

demand_data3 = {
    "coords": {
        7: (39.398056, 22.804167),
        8: (39.397222, 22.809444),
        9: (39.396667, 22.813889),
        10: (39.396111, 22.805833),
    },
    "cap": {7: 5, 8: 5, 9: 12, 10: 8},
}
demand_data3 = pd.DataFrame.from_dict(demand_data3)


class test_balance_sup_dem(unittest.TestCase):
    def test_supp_gt_dem(self):
        supply_balanced, demand_balanced = balance_sup_dem(supply_data1, demand_data1)
        # check if the supply and demand is balanced
        self.assertEqual(supply_balanced.cap.sum(), demand_balanced.cap.sum() + 1 )

        # check if the original shares of supply and demand values protected
        self.assertEqual(
            list(supply_data1.cap / supply_data1.cap.sum()),
            list(supply_balanced.cap / supply_balanced.cap.sum()),
        )
        self.assertEqual(
            list(demand_data1.cap / demand_data1.cap.sum()),
            list(demand_balanced.cap / demand_balanced.cap.sum()),
        )

    def test_dem_gt_sup(self):
        supply_balanced, demand_balanced = balance_sup_dem(supply_data2, demand_data2)
        # check if the supply and demand is balanced
        self.assertEqual(supply_balanced.cap.sum(), demand_balanced.cap.sum())

        # check if the original shares of supply and demand values protected
        self.assertEqual(
            list(supply_data2.cap / supply_data2.cap.sum()),
            list(supply_balanced.cap / supply_balanced.cap.sum()),
        )
        self.assertEqual(
            list(demand_data2.cap / demand_data2.cap.sum()),
            list(demand_balanced.cap / demand_balanced.cap.sum()),
        )

    def test_supp_eq_dem(self):
        supply_balanced, demand_balanced = balance_sup_dem(supply_data3, demand_data3)
        # check if the supply and demand is balanced
        self.assertEqual(supply_balanced.cap.sum(), demand_balanced.cap.sum())

        # check if the original shares of supply and demand values protected
        self.assertEqual(
            list(supply_data3.cap / supply_data3.cap.sum()),
            list(supply_balanced.cap / supply_balanced.cap.sum()),
        )
        self.assertEqual(
            list(demand_data3.cap / demand_data3.cap.sum()),
            list(demand_balanced.cap / demand_balanced.cap.sum()),
        )
