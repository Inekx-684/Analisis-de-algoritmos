def FuerzaBruta(nums):

    #Complejidad temporal: O(n^2)
    #Complejidad espacial: O(1)

    n = len(nums)
    mejorsuma = nums[0]

    for i in range(n):
        sumaactual = 0
        for j in range(i, n):
            sumaactual += nums[j]  
            if sumaactual > mejorsuma:
                mejorsuma = sumaactual

    return mejorsuma


def kadane(nums):


    #Complejidad temporal: O(n)
    #Complejidad espacial: O(1)

    sumaactual = nums[0]
    mejorsuma = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]
        sumaactual = max(num, sumaactual + num)
        mejorsuma = max(mejorsuma, sumaactual)

    return mejorsuma
