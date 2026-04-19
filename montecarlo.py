import random
import math

def random_point_on_sphere(a):
    """
    Generates a uniform distribution of points on a sphere
    using the Archimedes Projection Method.
    """
    # z is chosen uniformly between -radius and radius
    z = random.uniform(-a, a)

    # theta is the azimuthal angle around the z-axis
    theta = random.uniform(0, 2 * math.pi)

    # Calculate the radius of the circle at height z
    # Since x^2 + y^2 + z^2 = r^2, then x^2 + y^2 = r^2 - z^2
    r_at_z = math.sqrt(a ** 2 - z ** 2)

    x = r_at_z * math.cos(theta)
    y = r_at_z * math.sin(theta)

    return x, y, z

def monte_carlo_sphere_cylinder(a, num_points=1_000_000):
    n = 0  # points inside cylinder
    m = 0  # total points

    for _ in range(num_points):
        x, y, z = random_point_on_sphere(a)
        # Cylinder: x^2+y^2-ax = 0
        if x**2 + y**2 - a*x <= 0:
            n += 1
        m += 1

    ratio = n / m
    return ratio


def expected_sphere_cylinder(a):
    SA_calculated = a ** 2 * (2 * math.pi - 4)
    SA_sphere = (4 * math.pi * a ** 2)
    expected = SA_calculated / SA_sphere

    return expected

# Run simulation

a = 1

num_points = 1_000_000
ratio_sim = monte_carlo_sphere_cylinder(a, num_points)
ratio_exp = expected_sphere_cylinder(a)
print(f"Monte Carlo ratio (n/m): {ratio_sim:.6f}")
print(f"Expected ratio:          {ratio_exp:.6f}")
print(f"Relative error:          {(abs(ratio_sim - ratio_exp) / ratio_exp) * 100:.3f}%")