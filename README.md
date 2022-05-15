# Open Source Energy Modelling - Summer Term 2022

## Assignment 1

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright 2022 Ali Kök

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Overview

In this repository, a function called `balance_sup_dem()` is created, and automatic unittests are defined using GitHub actions. unittest are defined using built-in python module `unittest` and executed using `pytest` package.

The function is created based on a code block used in [GIS Module](https://github.com/Emb3rs-Project/p-gis) of EMB3RS project. GIS Module's purpose within the EMB3RS platform is to analyze the network dimension and bring in the spatial dimension between sources and sinks. The application of the GIS is tailored for looking into the option of reusing the excess heat/cold at a certain distance within a District Heating and Cooling system. It calculates a network solution between a particular set of sources and sinks among the Open Street Map road network. The related investment costs into the grid and the corresponding heat/cold losses are calculated based on that network solution.

## Details of the function

`balance_sup_dem()` function's aim is to balance the total supply and the total demand. This is required because of the balanced network assumption of the optimization model. In other words, `balance_sup_dem()` function is a preprocessing step needed for network optimization. If this balanced network assumption is not met, optimazation will fail, hence this step is critical.

`balance_sup_dem()` function has two inputs which are pandas dataframes:
1. `supply_data_py` consist of `coords` and `cap` columns. It contains information about heat/cold sources.
    - `coords` is the coordinates (lat, lon) of the sources, and `cap` is the maximum supply capacity of a source in MW.
2. `demand_data_py` consist of `coords` and `cap` columns. It contains information about heat/cold sinks.
    - `coords` is the coordinates (lat, lon) of the sinks, and `cap` is the maximum demand capacity of a sink in MW.

Note: `coords` are not used within the scope of this function.

The output of the function is another pandas dataframe with the same structure.

## Unittests

`balance_sup_dem()` function has two main features:
1. It calculates total supply and demand and check if they are equal or not. If they are equal, it does nothing and just returns the original values. If they are not equal, the function decreases the one with the higher value to balance them. Therefore, the resulting total supply and demand values must be equal.
2. It is significant to preserve the ratio of each source's/sink's capacity to total capacity of sources/sinks. So, all sources and sinks must have the same share of capacity within their own class after balancing operation.

The unittests are designed to test these two main features where
- it is checked whether supply is equal to demand in the resulting dataframe,
- it is checked whether the shares of supply and demand capacities are preserved in the resulting dataframe.

For these main features, three test functions are defined:
1. `test_supp_gt_dem` is designed to test when total supply is greater then demand.
2. `test_dem_gt_sup` is designed to test when total demand is greater then supply.
3. `test_supp_eq_dem` is designed to test total supply and total demand are equal.

As a results there are six test assertions in total.

