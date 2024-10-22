import mpmath
import csv
from matplotlib import pyplot as plt


def calculate_pi_achi(n):
    mpmath.mp.dps = 50
    p_sides = mpmath.mpf(1.0) / mpmath.sqrt(mpmath.mpf(3.0))
    for i in range(0, n):
        p_sides = (mpmath.sqrt(p_sides ** 2 + 1) - 1) / p_sides
    pi = 6 * 2 ** n * p_sides
    return pi


if __name__ == '__main__':
    x = []
    y = []
    ae = []
    re = []

    with open("data_pi.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Loop', 'Sides', 'pi', 'A_error', 'R_error'])

    for i in range(0, 51):
        outcome = calculate_pi_achi(i)
        absolute_error = mpmath.fabs(outcome - mpmath.pi)
        relative_error = mpmath.fabs(outcome - mpmath.pi) / mpmath.pi

        x.append(i)
        y.append(outcome)
        ae.append(absolute_error)
        re.append(relative_error)
        with open("data_pi.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([i, 6 * 2 ** i, outcome, absolute_error, relative_error])

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 6))

    ax1.bar(x, ae, color='red', alpha=0.7)
    ax1.set_xlabel('N-loop')
    ax1.set_ylabel('absolute_error')
    ax1.set_yscale('log')
    ax1.set_title('Value of Absolute Error')

    ax2.bar(x, re, color='red', alpha=0.7)
    ax2.set_xlabel('N-loop')
    ax2.set_ylabel('relative_error')
    ax2.set_yscale('log')
    ax2.set_title('Value of Relative Error')

    ax3.plot(x, y, linestyle='-', color='b', label='Pi')
    ax3.set_xlabel("N-loop")
    ax3.set_ylabel("Pi")
    ax3.set_title("Value of Pi")

    plt.tight_layout()
    plt.show()


