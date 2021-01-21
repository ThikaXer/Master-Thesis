from Beweis_rank_d import Beweis as Beweis
import pickle

# Non-Pappus
print('Pappus')
P_points = set(range(1, 10))  # Set of all points
P_collinearities = [  # List of collinearities
    {1, 2, 3},
    {4, 5, 6},
    {1, 5, 9},
    {1, 6, 8},
    {2, 4, 9},
    {2, 6, 7},
    {3, 4, 8},
    {3, 5, 7}
]
P_integer = Beweis(3,P_points, P_collinearities, 'Pappus')

with open('Pappus/P_integer.pickle', 'wb') as f:
    pickle.dump(P_integer, f)



# Non-Desargues
print('Desargues')
D_points = set(range(10))
D_collinearities = [
    {0, 2, 8},
    {0, 3, 7},
    {0, 4, 6},
    {6, 8, 9},
    {1, 5, 9},
    {2, 4, 9},
    {3, 4, 5},
    {5, 6, 7},
    {7, 8, 1}
]
D_beweis = Beweis(3,D_points, D_collinearities, 'Desargues')

with open('Desargues/P_integer.pickle', 'wb') as f:
    pickle.dump(D_beweis, f)


# incidence theorem Example4 from JRG Mechanical Theorem Proving [18] in PG S.23
print('Bsp incidence thm')
Bsp_points = set(range(10))
Bsp_collinearities = [
    {0, 1, 8},
    {3, 4, 8},
    {9, 5, 8},
    {6, 7, 8},
    {0, 3, 6},
    {1, 4, 7},
    {2, 5, 7},
    {2, 6, 9},
    {0, 2, 4},
    {4, 5, 6},
    {3, 7, 9}
]
Bsp_beweis = Beweis(3,Bsp_points, Bsp_collinearities, 'Mech_Thm_proving_incidence_thm')

with open('Mech_Thm_proving_incidence_thm/P_integer.pickle', 'wb') as f:
    pickle.dump(Bsp_beweis, f)



# 10-3-configurations that is non realizable from Meditation on Cevas theorem [21] S.6
print('non-realizable 10-3-configuration')
nr_points = set(range(10))
nr_collinearities = [
    {1,3,6},
    {1,4,8},
    {2,3,5},
    {2,4,7},
    {1,2,9},
    {6,8,9},
    {5,7,9},
    {3,4,0},
    {5,6,0},
    {7,8,0}
]
nr_beweis = Beweis(3,nr_points, nr_collinearities, 'non_realizable_10_3_config')

with open('non_realizable_10_3_config/P_integer.pickle', 'wb') as f:
    pickle.dump(nr_beweis, f)



# Vamos matroid
print('Vamos')
P_points = set(range(1, 9))  # Set of all points
P_collinearities = [  # List of collinearities
    {1,2,5,6},
    {1,3,5,7},
    {1,4,5,8},
    {2,3,6,7},
    {3,4,7,8}
]
P_integer = Beweis(4,P_points, P_collinearities, 'Vamos')

with open('Vamos/P_integer.pickle', 'wb') as f:
    pickle.dump(P_integer, f)

