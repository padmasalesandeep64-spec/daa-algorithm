0/1 knapsack · parcel selection

# Knapsack Lab

The same set of parcels, solved four ways. Change a weight, a value or the capacity and every method runs again, so you can see which ones find the best answer and how much work each one does.

## Parcels

NameWeightValueValue / kg

Capacity (kg)

Weights are whole kilograms. Up to 16 parcels, because brute force checks every subset.

## Results

## Side by side

Work done counts basic steps in this page's JavaScript version of each method. Time is measured in your browser and is only meaningful when the parcel list gets longer.

## Dynamic programming table

Each cell is the best value using the first *k* parcels with that much capacity. The shaded path is the walk back from the bottom-right cell, and amber cells are where a parcel was taken.

## Python source

These are your four files as written. The page runs matching JavaScript versions of the same logic. Capacity in your brute force file is 17 and the others use 15, so set the capacity above to see them agree.

```

```

Greedy picks by value per kilogram and never goes back, so it can miss the best set. The other three always find it.