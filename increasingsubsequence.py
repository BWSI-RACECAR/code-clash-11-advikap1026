class Solution:
    def find_longest_increasing_subsequence(self, arr):
            #type arr: list of int
            #return type: int
            
            #TODO: Write code below to return an int with the solution to the prompt.
            #arr = arr.sort()
            answer = 1
            max = 0
            max = arr[0]
            for i in range(len(arr)):
                if arr[i] > max:
                     max = arr[i]
                     answer = answer + 1
            return answer 
            pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.find_longest_increasing_subsequence(array)
    print(ans)

if __name__ == "__main__":
    main()