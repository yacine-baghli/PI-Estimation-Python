# Estimation of Pi Using Monte Carlo Simulation

This Python script utilizes a Monte Carlo method to estimate the value of pi and visualizes the estimation process using Matplotlib.

## Code Explanation

### `estimation_pi(n)`

This function estimates the value of pi by generating `n` random points within a square of side length 2 centered at the origin. It counts how many of these points fall inside a unit circle centered at the origin and uses the ratio of points inside the circle to the total points to estimate pi.

### `plot_figures(num_points)`

This function generates `num_points` random points within the square [-1, 1] x [-1, 1]. It separates points that fall inside the unit circle from those outside and creates two figures using Matplotlib:

1. **Figure 1**: Shows the points generated and distinguishes points inside the circle (blue) from points outside (red). It includes a circle outline to represent the boundary of the unit circle.

2. **Figure 2**: Plots the progression of pi estimations as the number of generated points increases. It compares the estimated values of pi against the true value (3.141592653589793) using a line plot.

### `main` Execution

In the main block, the script sets `num_points` to 1000 and calls `plot_figures(num_points)` to execute the visualization process.

## How to Use

1. Ensure you have Python installed on your system.
2. Install required dependencies:
   ```
   pip install matplotlib
   ```
3. Run the script:
   ```
   python estimation_pi.py
   ```
4. The script will output two figures:
   - Figure 1 showing the points inside and outside the circle.
   - Figure 2 showing the estimation of pi as the number of points increases.

## Output

The figures generated will be displayed interactively and saved as `estimation_de_pi.png` in the current directory.
