#Ejercicio two summ
#Fuerza bruta.
#Complejidad temporal = O(n^2) por los 2 ciclos anidados.
#Complejidad espacial = O(1) porque no se usan listas ni diccionarios.
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
                
#Optimizado
#Complejidad temporal = O(n) porque solo tiene un ciclo for
#Complejidad espacial = O(n) por el diccionario.
class Solution(object):
    def twoSum(self, nums, target):
        vistos = {}

        for i, num in enumerate(nums):
            complemento = target - num

            if complemento in vistos:
                return [vistos[complemento], i]

            vistos[num] = i         
            
            