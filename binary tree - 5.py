
class BinaryTree:

    def __init__(self, values:list):
        assert isinstance(values, list), 'Values must in in list format.'
        self.values = sorted(values)
        self.tree = self.construct_tree(self.values)


    @staticmethod
    def construct_tree(dataset, depth=0):
        if len(dataset) == 0:
            return
        
        mid = len(dataset) // 2
        root = dataset[mid] # the middle term
        smaller = tuple(dataset[:mid])
        larger = tuple(dataset[mid+1:])
        depth += 1
        return (BinaryTree.construct_tree(smaller, depth), root, BinaryTree.construct_tree(larger, depth))
        
    def display_tree(self):
        return

    def search(self, item): # testing for item membership
        array = self.tree
        midpoint = array[1]
        while True:
            try:
                if not (array[0] or array[2]):
                    break
            except:
                break
            if midpoint == item:
                return True
            elif midpoint > item:
                array = array[0]
                if not isinstance(array, tuple): # array is number or 'Nonetype'
                    continue
                else:
                    midpoint = array[1]
            elif midpoint < item:
                array = array[2]
                if not isinstance(array, tuple):
                    continue
                else:
                    midpoint = array[1]
        return False

    def insert(self, item):
        return

    def delete(self, item):
        return

    def __repr__(self):
        return 'Binary Tree:\n{}\n{}\n'.format(self.values, self.tree)


b1 = BinaryTree([1, 2, 3, 4, 5])
print(b1.construct_tree([1, 2, 3, 4, 5]))
print(b1)
print(b1.search(1))

    
