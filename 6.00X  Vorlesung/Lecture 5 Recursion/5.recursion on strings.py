def isRe(s):
    def toChar(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:#必须将base case 修改成number的形式
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])# 查看头尾 and 对于下一个进行切片

    return isPal(toChar(s))

print(isRe('kyka'))