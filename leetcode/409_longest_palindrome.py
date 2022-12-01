class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s의 알파벳 조합으로 만들 수 있는 제일 긴 앞으로읽어도 뒤로읽어도 똑같은 단어 길이
        # 숫자를 세서 짝수인건 다 더하고 홀수인거는 하나씩 빼고 다더하고 마지막에 1 더하기(있을때만)
        # ls = list(s)
        # ss = list(set(ls))

        # even = [ls.count(x) for x in ss if ls.count(x) % 2 == 0]
        # odd = [ls.count(x) - 1 for x in ss if ls.count(x) % 2 == 1]

        # return sum(even) + sum(odd) + bool(len(odd)) # 얘도 굳이 len(odd)할필요없다 []는 false니깐,,

# 다른풀이
# 굳이 리스트 두개를 만들 필요가 없다 리스트 요소 개수 - 홀수개인 숫자 + 1 하면 되니깐.........!
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c) # 없으면 넣고 있으면 뺀다 -> 홀수개면 마지막에 남아있을것
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)

# 아래 풀이 다시 보고 이해하기
# 왜 128개를 만드는건지?, ord()는 무엇...
# https://leetcode.com/problems/longest-palindrome/discuss/791646/C%2B%2BPythonJava-It-is-only-easy-when-you-think-really-hard-to-spot-the-built-in-nature
# collections
# https://leetcode.com/problems/longest-palindrome/discuss/89587/What-are-the-odds-(Python-and-C%2B%2B)



# s = "abccccdd" # Output: 7
# s = "a" # Output: 1
s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
# 983

a = Solution()
print(a.longestPalindrome(s))
