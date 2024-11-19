from packer import Packer
from bin import Bin
from item import Item

packer = Packer()


if __name__ == '__main__':

    #Add bin
    packer.add_bin(Bin('pallet2', 11.0, 8.5, 5.5, 70.0))

    #Add items
    packer.add_item(Item('50g [powder 1]', 3.9370, 1.9685, 1.9685, 1))
    packer.add_item(Item('50g [powder 2]', 3.9370, 1.9685, 1.9685, 2))
    packer.add_item(Item('50g [powder 3]', 3.9370, 1.9685, 1.9685, 3))
    packer.add_item(Item('50g [powder 4]', 3.9370, 1.9685, 1.9685, 3))
    packer.add_item(Item('50g [powder 5]', 3.9370, 1.9685, 1.9685, 3))
    packer.add_item(Item('50g [powder 6]', 3.9370, 1.9685, 1.9685, 3))
    packer.add_item(Item('50g [powder 7]', 5.1240, 1.1350, 1.5435, 3))
    packer.add_item(Item('250g [powder 8]', 7.8740, 3.9370, 1.9685, 4))
    packer.add_item(Item('250g [powder 9]', 7.8740, 3.9370, 1.9685, 5))
    packer.add_item(Item('250g [powder 10]', 7.8740, 3.9370, 1.9685, 6))
    packer.add_item(Item('250g [powder 11]', 7.8740, 3.9370, 1.9685, 7))
    packer.add_item(Item('250g [powder 12]', 7.8740, 3.9370, 1.9685, 8))
    packer.add_item(Item('250g [powder 13]', 7.8740, 3.9370, 1.9685, 9))

    packer.pack()