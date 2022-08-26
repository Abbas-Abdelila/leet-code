class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        list_1 = list(map(int, str(n)))
        counter_1 = collections.Counter(list_1)
        i = 0
        while True:
            val = 2 ** i
            list_2 = list(map(int, str(val)))
			# If the len of both number are same
            if len(list_2) == len(list_1):
			    # check if values are also exactly same, return True
                if collections.Counter(list_2) == counter_1:
                    return True
            else:
			    # if len exceeds the n value, return False
                if len(list_2) > len(list_1):
                    return False
            i += 1