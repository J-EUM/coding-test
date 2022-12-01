class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s의 알파벳 조합으로 만들 수 있는 제일 긴 앞으로읽어도 뒤로읽어도 똑같은 단어 길이
        # 숫자를 세서 짝수인건 다 더하고 홀수인거는 하나씩 빼고 다더하고 마지막에 1 더하기(있을때만)
        ls = list(s)
        ss = list(set(ls))

        even = [ls.count(x) for x in ss if ls.count(x) % 2 == 0]
        odd = [ls.count(x) - 1 for x in ss if ls.count(x) % 2 == 1]

        return sum(even) + sum(odd) + bool(len(odd))




# s = "abccccdd" # Output: 7
# s = "a" # Output: 1
s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
# 983

a = Solution()
print(a.longestPalindrome(s))
