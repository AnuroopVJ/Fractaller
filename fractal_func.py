import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from math import sin,tan,pi,log

iter_c = 0
#z = 0
#zn+1 = zn^2 + p

def mandelbrot(n_rows, n_columns, iterations, cmap_ch, x_min=-2, x_max=1, y_min=-1.5, y_max=1.5, escape_radius=2):
    r = np.linspace(x_min, x_max, n_rows)  # real
    i = np.linspace(y_min, y_max, n_columns)  # imaginary
    r, i = np.meshgrid(r, i)
    p = r + 1j * i
    z = np.zeros_like(p, dtype=complex)
    iter_count = np.zeros_like(p, dtype=int)
    for _ in range(iterations):
        mask = np.abs(z) < escape_radius
        z[mask] = z[mask]**2 + p[mask]
        iter_count[mask] += 1
    plt.imshow(iter_count.T, cmap=cmap_ch, extent=[x_min, x_max, y_min, y_max])
    plt.axis("off")
    plt.show()
    return iter_count


def juila_set(range_, max_iterations, linear_resolution, cmap, center=-0.05 - 0.66j, power=2, x1=-1.5, x2=1.5, y1=-1, y2=1):
    if range_ is None:
        range_ = 0.9 + abs(center)

    M, N = int((y2 - y1) * linear_resolution), int((x2 - x1) * linear_resolution)
    xcoordinates = [(x1 + ((x2 - x1) / N) * i) for i in range(N)]
    ycoordinates = [(y1 + ((y2 - y1) / M) * i) for i in range(M)]

    julia_set = [[None for _ in xcoordinates] for _ in ycoordinates]

    for y in range(len(ycoordinates)):
        for x in range(len(xcoordinates)):
            z = complex(xcoordinates[x], ycoordinates[y])
            iteration = 0
            while abs(z) < range_ and iteration < max_iterations:
                iteration += 1
                z = z**power + center

            if iteration == max_iterations:
                julia_set[y][x] = 0
            else:
                julia_set[y][x] = iteration

    ax = plt.axes()
    ax.set_aspect('equal')
    plot = ax.pcolormesh(xcoordinates, ycoordinates, julia_set, cmap=cmap)
    plt.colorbar(plot)
    plt.title(f'Julia-set \ncenter = {center}, range = {range_:.3f}, max-iterations = {max_iterations}, power = {power}')
    plt.show()



#Buddhabrot
def make_non_mandelbrot_set(nsamples: int, max_iterations: int) -> np.ndarray:
    """Generate a set of complex numbers that are not in the Mandelbrot set.
    This employs some of the optimizations from this page,
    http://en.wikipedia.org/wiki/Mandelbrot_set#Optimizations
    In order to minimize run time, we are trying to reduce the number of points
    that we already know that are in the mandelbrot set. Points inside the within the
    cardioid and in the period-2 bulb can be eliminiated.
    Args:
        nsamples (int): Number of samples to generate.
        max_iterations (int): Maximum number of iterations to perform.
    Returns:
        np.ndarray: Array of complex numbers that are not in the Mandelbrot set.
    """

    non_mandels = np.zeros(nsamples, dtype=np.complex128)
    n_non_mandels = 0

    cardioid = (
        np.random.random(nsamples) * 4 - 2 + (np.random.random(nsamples) * 4 - 2) * 1j
    )

    p = (((cardioid.real - 0.25) ** 2) + (cardioid.imag ** 2)) ** 0.5
    cardioid = cardioid[cardioid.real > p - (2 * p ** 2) + 0.25]

    cardioid = cardioid[((cardioid.real + 1) ** 2) + (cardioid.imag ** 2) > 0.0625]

    z = np.copy(cardioid)

    for _ in range(max_iterations):
        z = z ** 2 + cardioid

        mask = np.abs(z) < 2
        new_non_msets = cardioid[~mask]
        non_mandels[n_non_mandels : n_non_mandels + len(new_non_msets)] = new_non_msets
        n_non_mandels += len(new_non_msets)

        cardioid = cardioid[mask]
        z = z[mask]

    return non_mandels[:n_non_mandels]


def generate_buddhabrot(non_mandelbrot: np.ndarray, size: int) -> np.ndarray:
    """Generate buddhabrot image array
    Args:
        non_manderlbrot (np.ndarray): Array of non-mandelbrot points on the complex plane
        size (int): Size of the image array
    Returns:
        np.ndarray: Image array containing buddhabrot trajectories
    """
    img_array = np.zeros([size, size], int)
    z = np.copy(non_mandelbrot)

    while len(z):

        # Mapping the complex plane to the image array
        x = np.array((z.real + 2.0) / 4 * size, int)
        y = np.array((z.imag + 2.0) / 4 * size, int)

        img_array[x, y] += 1

        z = z ** 2 + non_mandelbrot

        mask = np.abs(z) < 2
        non_mandelbrot = non_mandelbrot[mask]
        z = z[mask]
    print(f"Var containing Trajectory values: {img_array.ndim}D")
    plt.imshow(img_array, cmap='viridis')
    plt.colorbar() # Add a colorbar to show the mapping of values to colors
    plt.show()

