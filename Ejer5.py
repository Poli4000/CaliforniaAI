import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree


def plot_decision_tree(X, y, max_depth=None):
    # Validar max_depth
    if max_depth is None or max_depth > 10:
        max_depth = 5

    # Entrenar el árbol
    arbol = DecisionTreeRegressor(max_depth=max_depth, random_state=42)
    arbol.fit(X, y)

    # Dibujar el árbol
    plt.figure(figsize=(12, 8))
    plot_tree(arbol, filled=True)
    plt.show()
