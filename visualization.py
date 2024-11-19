import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def draw_cuboid(ax, position, size, color='blue', alpha=0.7, edge=True):
    """
    Draws a cuboid (3D rectangle) at a given position with the specified size.

    Args:
        ax: Matplotlib 3D axis to draw on.
        position: Tuple of (x, y, z) representing the starting position of the cuboid.
        size: Tuple of (length, width, height) representing the size of the cuboid.
        color: Color of the cuboid (default is 'blue').
        alpha: Transparency level (default is 0.7).
        edge: Whether to draw the edges (default is True).
    """
    x, y, z = map(float, position)
    dx, dy, dz = map(float, size)

    vertices = np.array([
        [x, y, z],
        [x + dx, y, z],
        [x + dx, y + dy, z],
        [x, y + dy, z],
        [x, y, z + dz],
        [x + dx, y, z + dz],
        [x + dx, y + dy, z + dz],
        [x, y + dy, z + dz]
    ])

    faces = [
        [vertices[j] for j in [0, 1, 2, 3]],
        [vertices[j] for j in [4, 5, 6, 7]],
        [vertices[j] for j in [0, 3, 7, 4]],
        [vertices[j] for j in [1, 2, 6, 5]],
        [vertices[j] for j in [0, 1, 5, 4]],
        [vertices[j] for j in [2, 3, 7, 6]]
    ]

    # Create the cuboid as a Poly3DCollection
    poly3d = Poly3DCollection(faces, color=color, edgecolor='k' if edge else None, alpha=alpha)
    ax.add_collection3d(poly3d)


def visualize_bin_3d(bin_name, bin_size, fitted_items, views=None, wireframe=True):
    """
    Visualizes a bin in 3D with optional rotations and transparency adjustments.

    Args:
        bin_name (str): Name of the bin.
        bin_size (tuple): Dimensions of the bin (length, width, height).
        fitted_items (list): List of items to be visualized, with positions and dimensions.
        views (list): List of angles to visualize the bin from different perspectives.
        wireframe (bool): If True, applies a wireframe to overlapping objects for better depth.
    """
    if views is None:
        views = [(20, -60), (20, 60), (20, 135)]  # Three different angles

    bin_size = tuple(map(float, bin_size))
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan']

    # Sort items by their z-coordinate (height) to render from bottom to top
    fitted_items_sorted = sorted(fitted_items, key=lambda item: item['pos'][2])

    for i, (elev, azim) in enumerate(views):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title(f"3D View {i + 1}: Bin {bin_name} (elev={elev}, azim={azim})")

        ax.set_xlim([0, bin_size[0]])
        ax.set_ylim([0, bin_size[1]])
        ax.set_zlim([0, bin_size[2]])

        # Draw the bin boundary with transparency to allow visibility of contents
        draw_cuboid(ax, position=(0, 0, 0), size=bin_size, color='lightgrey', alpha=0.15, edge=False)

        # Draw each fitted item with specified transparency
        for j, item in enumerate(fitted_items_sorted):
            pos = tuple(map(float, item['pos']))
            dims = tuple(map(float, item['dimension']))
            color = colors[j % len(colors)]

            # If wireframe is True, the cuboid will be outlined to avoid hidden perspectives
            draw_cuboid(ax, position=pos, size=dims, color=color, alpha=0.8, edge=wireframe)
            ax.text(
                pos[0] + dims[0] / 2,
                pos[1] + dims[1] / 2,
                pos[2] + dims[2] / 2,
                item['name'], color='black', ha='center'
            )

        # Set view angle
        ax.view_init(elev=elev, azim=azim)

        # Labels
        ax.set_xlabel("Length")
        ax.set_ylabel("Width")
        ax.set_zlabel("Height")

        plt.show()
