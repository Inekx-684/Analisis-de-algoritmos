#Fuerza bruta
class Solution:
    def eraseOverlapIntervals(self, intervals):
        
        # Complejidad temporal: O(2^n * n)
        # Se generan todos los subconjuntos posibles (2^n)
        # y cada uno puede requerir hasta O(n) para verificar solapamientos
        
        # Complejidad espacial: O(n)
        # debido a la recursión y al almacenamiento temporal del subconjunto
        
        n = len(intervals)
        max_no_solapados = [0]

        def no_se_solapan(subconjunto):
            subconjunto.sort(key=lambda x: x[0])

            for i in range(1, len(subconjunto)):
                if subconjunto[i][0] < subconjunto[i - 1][1]:
                    return False
            return True

        def backtrack(i, actual):

            if i == n:
                copia = actual[:]
                if no_se_solapan(copia):
                    max_no_solapados[0] = max(max_no_solapados[0], len(actual))
                return

            # no incluir intervalo
            backtrack(i + 1, actual)

            # incluir intervalo
            actual.append(intervals[i])
            backtrack(i + 1, actual)
            actual.pop()

        backtrack(0, [])

        return n - max_no_solapados[0]
    
    
    
    
#optimizado
class Solution:
    def eraseOverlapIntervals(self, intervals):
        
        # Complejidad temporal: O(n log n)
        # por el ordenamiento de los intervalos
        
        # Complejidad espacial: O(1)
        # no se usan estructuras adicionales, solo variables auxiliares
        
        if not intervals:
            return 0

        # ordenar por el final del intervalo
        intervals.sort(key=lambda x: x[1])

        eliminados = 0
        fin_actual = intervals[0][1]

        for i in range(1, len(intervals)):
            inicio, fin = intervals[i]

            # si se solapa, se elimina este intervalo
            if inicio < fin_actual:
                eliminados += 1
            else:
                # si no se solapa, actualizamos el fin
                fin_actual = fin

        return eliminados