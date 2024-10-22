import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_class_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))

    # Boundary Classes
    boundary_classes = {
        "LoginForm": (1, 8),
        "ClientForm": (1, 6),
        "ProductForm": (1, 4),
        "SalesForm": (1, 2)
    }

    # Control Classes
    control_classes = {
        "LoginController": (6, 7),
        "ClientController": (6, 5),
        "ProductController": (6, 3),
        "SalesController": (6, 1)
    }

    # Entity Classes
    entity_classes = {
        "User": (11, 7),
        "Client": (11, 5),
        "Product": (11, 3),
        "Sale": (11, 1)
    }

    # Draw Boundary Classes
    for class_name, position in boundary_classes.items():
        rect = patches.FancyBboxPatch((position[0], position[1]), 4, 1.5, boxstyle="round,pad=0.3", edgecolor='blue', facecolor='lightblue')
        ax.add_patch(rect)
        ax.text(position[0] + 2, position[1] + 0.75, class_name, ha='center', va='center', fontsize=10)

    # Draw Control Classes
    for class_name, position in control_classes.items():
        rect = patches.FancyBboxPatch((position[0], position[1]), 4, 1.5, boxstyle="round,pad=0.3", edgecolor='green', facecolor='lightgreen')
        ax.add_patch(rect)
        ax.text(position[0] + 2, position[1] + 0.75, class_name, ha='center', va='center', fontsize=10)

    # Draw Entity Classes
    for class_name, position in entity_classes.items():
        rect = patches.FancyBboxPatch((position[0], position[1]), 4, 1.5, boxstyle="round,pad=0.3", edgecolor='red', facecolor='lightcoral')
        ax.add_patch(rect)
        ax.text(position[0] + 2, position[1] + 0.75, class_name, ha='center', va='center', fontsize=10)

    # Draw Associations (simple lines for simplicity)
    associations = [
        (boundary_classes["LoginForm"], control_classes["LoginController"]),
        (boundary_classes["ClientForm"], control_classes["ClientController"]),
        (boundary_classes["ProductForm"], control_classes["ProductController"]),
        (boundary_classes["SalesForm"], control_classes["SalesController"]),
        (control_classes["LoginController"], entity_classes["User"]),
        (control_classes["ClientController"], entity_classes["Client"]),
        (control_classes["ProductController"], entity_classes["Product"]),
        (control_classes["SalesController"], entity_classes["Sale"]),
    ]

    for start, end in associations:
        ax.plot([start[0] + 4, end[0]], [start[1] + 0.75, end[1] + 0.75], 'k--')

    # Setting limits and removing axes
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')

    plt.show()

draw_class_diagram()