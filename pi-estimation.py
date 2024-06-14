import random
import matplotlib.pyplot as plt

def estimation_pi(n):

    # On initialise notre variable :
    points_cercle = 0

    for i in range(n):

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # L'equation de notre cercle
        eq_cercle = x**2 + y**2

        if eq_cercle <= 1:
            points_cercle += 1

    # S_disque/S_domaine=n_disque/S_domaine donc 2*pi*r=n avec r=2 donc :
    pi_estimation = 2*2* (points_cercle / n)

    return pi_estimation

def plot_figures(num_points):

    inside_circle_x = []
    inside_circle_y = []

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        eq_cercle = x**2 + y**2

        if eq_cercle <= 1:
            inside_circle_x.append(x)
            inside_circle_y.append(y)

    plt.figure(figsize=(12, 6))

    # Figure 1
    plt.subplot(1, 2, 1)
    plt.scatter(inside_circle_x, inside_circle_y, color='blue', label='Points à l intérieur du cercle')
    plt.scatter([x for x in range(num_points) if x not in inside_circle_x],[y for y in range(num_points) if y not in inside_circle_y],color='red', label='Points à l\'extérieur du cercle')
    circle = plt.Circle((0, 0), 1, color='red', fill=False, linewidth=2)
    plt.gca().add_patch(circle)
    plt.title('Estimation de pi (Etape 1)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # Figure 2 :

    pi_valeurs = [estimation_pi(i) for i in range(1, num_points + 1)]
    plt.subplot(1, 2, 2)
    plt.plot(range(1, num_points + 1), pi_valeurs, color='green')
    plt.axhline(y=3.141592653589793, color='red', linestyle='--', label='Valeur réelle de pi')
    plt.title('Estimation de pt (Etape 2)')
    plt.xlabel('Nombre de points tirés (n)')
    plt.ylabel('Estimation de pi')
    plt.legend()

    plt.tight_layout()

    # Il faut sauvegarder la figure avant de l'afficher
    plt.savefig('estimation de pi.png', format='png', dpi=200)

    plt.show()



if __name__ == "__main__":

    # Nombre de points tirés :
    num_points= 1000
    plot_figures(num_points)

