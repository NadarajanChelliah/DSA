class solution(object):
    def isOneBitCharacter(self, bits):
        pointer = 0
        while(pointer<len(bits)-1):
            if bits[pointer] == 1:
                pointer += 2
            else:
                pointer +=1

        if pointer >= len(bits):
            return False
        else:
            True


bits = [1,1,1,0]
# Sample: bits = [1,0,0]
sol = solution()
print(sol.isOneBitCharacter(bits))