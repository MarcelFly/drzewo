class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def sum_tree(self, data):
        sum = self.data
        if self.right != None:
            sum += self.right.sum_tree(self.right.data)
        if self.left != None:
            sum += self.left.sum_tree(self.left.data)
        return sum

    def sum_nodes_tree(self, data):
        nodes = 1
        if self.right != None:
            nodes += self.right.sum_nodes_tree(self.right.data)
        if self.left != None:
            nodes += self.left.sum_nodes_tree(self.left.data)
        return nodes

    def list_to_median(self, data):
        list_tree = [int(self.data)]
        if self.right != None:
            list_tree.extend(self.right.list_to_median(self.right.data))
        if self.left != None:
            list_tree.extend(self.left.list_to_median(self.left.data))
        return list_tree


values = [
    int(5),
    int(3),
    int(7),
    int(2),
    int(5),
    int(1),
    int(0),
    int(2),
    int(8),
    int(5),
]
W = [i for i in range(10)]
for z, values in enumerate(values):
    W[z] = Node()
    W[z].data = values
W[0].right, W[0].left = W[2], W[1]
W[1].right, W[1].left = W[4], W[3]
W[2].right, W[2].left = W[6], W[5]
W[6].right, W[6].left = W[8], W[7]
W[8].right = W[9]

print(
    "Dla jakiego numeru wezla policzyc sume, srednia i mediane w poddrzewie? Wezly sa ponumerowane w zakresie od 0-9"
)
x = input()
print("suma wartosci poddrzewa wynosi; ")
print(W[int(x)].sum_tree(W[int(x)].data))
print("srednia wartosc to: ")
print(W[int(x)].sum_tree(W[int(x)].data) / W[int(x)].sum_nodes_tree(W[int(x)].data))
print("mediana wynosi")
list_sorted = sorted(W[int(x)].list_to_median(W[int(x)].data))
a = len(list_sorted)
if a % 2 == 1:
    median = list_sorted[int(a / 2)]
else:
    median = (list_sorted[int(a / 2) - 1] + list_sorted[int(a / 2)]) / 2
print(median)




