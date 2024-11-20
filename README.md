# 3D-Bin-Packing-Problem
This project aims at solving 3D-Bin-Packing problem, a combinatorial NP-hard problem.
The whole 3D Packing implementation based on the following two papers:
- Li, Xueping & Zhao, Zhaoxia & Zhang, Kaike. (2014). [A genetic algorithm for the three-dimensional bin packing problem with heterogeneous bins](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/Reference/3DBPP_ISERC_Final.revHEAD.pdf). IIE Annual Conference and Expo 2014. 
- Dube, Erick & Kanavathy, Leon & K@i, Leon & Za, Owave. (2006). [Optimizing Three-Dimensional Bin Packing Through Simulation](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/Reference/erick_dube_507-034.pdf). 

The code based on (https://github.com/Janet-19/3d-bin-packing-problem) and some improvement to visualize the items placement in bins

**Basic parameters of items and bins:**

Here are some basic parameters that need your setup towards items and bins:
- Bin(name, length, width, height, capacity)
  - For each bin, you need to enter its name, length, width, height, and capacity (the maximum weight it can hold).
- Item(name, length, width, height, weight)
  - For each item, you need to enter its name, length, width, height, and weight.

**Basic usage of Packer class:**
1. Create a variable of Packer() class. Click [here](https://github.com/Janet-19/3d-bin-packing-problem/blob/master/main_model/packer.ipynb) to see Packer() definition.
2. Use *packer.add_bin()* and *packer.add_item()* to add items that needed packing and optional box types. Then, use *packer.pack()* to perform the whole packing process.
3. After packing, fitted and unfitted items in each bin and the bin with the highest packing rate will be printed.

**The objective is to maximize the packing rate of the variable bin:**

Basic Logic of 3D-Bin-Packing Model:
---------------------

The core logic of 3D-bin-packing model based on heuristic algorithm. To be specific:
- From a list of items, items are sorted from the biggest to the smallest and be placed in such ordering into a list of bins simultaneously.
- Orientation selection module: 
  - Each item has 1-6 orientations to choose when it can be placed into a certain bin. Orientation selection module can choose the best orientation type when facing several optinal orientations.
- Placement selection module: 
  - Here a pivot point is used to determine item's position. The pivot is an (x, y, z) coordinate which represents a point in a particular 3D bin at which an attempt to pack an item will be made. The back lower left corner of the item will be placed at the pivot. If the item cannot be packed at the pivot position then it is rotated until it can be packed at the pivot point or until we have tried all 6 possible rotation types. If after rotating it, the item still cannot be packed at the pivot point, then we move on to packing another item and add the unpacked item to a list of items that will be packed after an attempt to pack the remaining items is made. The first pivot in an empty bin is always (0,0,0). When one item can be placed into multiple optinal pivot point, placement selection module can help make a choice.
- Item stacking module:
  - Here I tried item stacking module when one item is being placed into a certain box. Item stacking module helps determin whether to stack similar items before placement action.
  - Since stacking module did not significantly increase the packing rate, I deleted it in the end.
- After all items in item list are placed into bins in bin list, the bin size with the highest packing rate will be chosen as final decision.




