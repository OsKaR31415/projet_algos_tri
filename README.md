
# Répartition des tâches

 - [Classe Node](src/node.py) : Maximilien Poncet
 - [Classe List](src/linked_list.py)
    - Constructeur, initialisation : Oscar Plaisant
    - Accesseurs et mutateurs de base : Oscar Plaisant
    - Fonctions d'affichage (`__str__` et `__repr__`) : Oscar Plaisant
    - Accesseurs avancés (`car`, `cdr`, `last`, ...) : Maximilien Poncet
    - Mutateurs avancés (`append`, `prepend`, `extend`, ...) : Maximilien Poncet
 - [tri par insertion](src/insertion_sort.py) : Maximilien Poncet
 - [tri à bulles](src/bubble_sort.py)
    - Tri à bulles récursif (`bubble_sort`) : Maximilien Poncet
    - Tri à bulles itératif en place (`in_place_bubble_sort`) : Oscar Plaisant
 - [tri par éclatement-fusion](src/merge_sort.py) : Maximilien Poncet
 - [tri rapide](src/quick_sort.py) : Oscar Plaisant
 - [tri par seaux](src/bucket_sort.py) : Oscar Plaisant
 - [fonction utilitaires](src/utils.py)
    - fonctions de génération de listes (`iota`, `random_list`, ...) : Maximilien Poncet
    - fonctions de manipulation de listes (`List_reduce`, `is_sorted`) : Maximilien Poncet
    - fonctions statistiques (`average`, `std_dev`, `avg_dev`) : Oscar Plaisant
    - fonctions de profilage (`execution_time`, `return_execution_time`) : Maximilien Poncet
    - fonction de sampling (`test execution times`) : Oscar Plaisant
 - [manipulation et enregistrement des donnés](src/statistics.py) : Oscar Plaisant
 - [Affichage des données](src/plotting.py) : Oscar Plaisant
 - Rédaction du [compte rendu](compte_rendu.pdf) : Oscar Plaisant

# Roadmap

 - [ ] méthode expérimentale
 - [x] classes `Node` et `LinkedList`
 - [x] fonctions pour tester l'efficacité des algorithmes de tri (architecture modulaire)
 - [x] algorithmes de tri
    - [x] tri par insertion (récursif et itératif) ([insertion_sort.py](src/insertion_sort.py))
    - [x] tri à bulles (récursif et itératif en-place) ([bubble_sort.py](src/bubble_sort.py))
    - [x] tri par seaux ([bucket_sort.py](src/bucket_sort.py))
    - [x] tri par éclatement-fusion
    - [x] tri rapide
 - [ ] visualisation des données



