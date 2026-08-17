from time import perf_counter as time
import random 
import AP_03_ordenacao as algoritmo

print(f"Algoritmo \t\t N \t Tempo Médio \t Pior caso\n")

for N in [100, 500, 1000, 5000]:
    medio_selection_sort = 0
    pior_selection_sort = 0
    medio_divide = 0
    pior_divide = 0
    medio_quick = 0
    pior_quick = 0

    for i in range(50):

        caso_medio = random.choices(range(1, 101), k=N)
        pior_caso = sorted(random.choices(range(1, 101), k=N), reverse=True)

        #selection_sort

        i_caso_medio = time()
        algoritmo.selection_sort(caso_medio)
        f_caso_medio = time()
        
        medio_selection_sort += f_caso_medio - i_caso_medio

        i_pior_caso = time()
        algoritmo.selection_sort(pior_caso)
        f_pior_caso = time()

        pior_selection_sort += f_pior_caso - i_pior_caso

        #divide_and_conquer

        i_caso_medio = time()
        algoritmo.divide_and_conquer_sort(caso_medio)
        f_caso_medio = time()
        
        medio_divide += f_caso_medio - i_caso_medio\

        i_pior_caso = time()
        algoritmo.divide_and_conquer_sort(pior_caso)
        f_pior_caso = time()

        pior_divide += f_pior_caso - i_pior_caso

        #quick_sort
\
        i_caso_medio = time()
        algoritmo.quick_sort(caso_medio)
        f_caso_medio = time()
        
        medio_quick += f_caso_medio - i_caso_medio\

        i_pior_caso = time()
        algoritmo.quick_sort(pior_caso)
        f_pior_caso = time()

        pior_quick += f_pior_caso - i_pior_caso
    
    print(f"Selection sort \t\t {N} \t {medio_selection_sort/50:.10f} \t {pior_selection_sort/50:.10f}")
    print(f"Divide and conquer \t {N} \t {medio_divide/50:.10f} \t {pior_divide/50:.10f}")
    print(f"Quick sort \t\t {N} \t {medio_quick/50:.10f} \t {pior_quick/50:.10f}\n")
    