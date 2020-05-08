package main

func isMatch(s string, p string) bool {
	if p == "" {
		return s == ""
	}
	memo := make([][]int, len(s)+1)
	for i := 0; i <= len(s); i++ {
		memo[i] = make([]int, len(p)+1)
	}
	var dp func(int, int) bool
	dp = func(i int, j int) bool {
		if memo[i][j] != 0 {
			return memo[i][j] == 1
		}
		if j == len(p) {
			return i == len(s)
		}
		firstMatch := i < len(s) && (s[i] == p[j] || p[j] == '.')
		res := false
		if len(p)-j > 1 && p[j+1] == '*' {
			res = dp(i, j+2) || firstMatch && dp(i+1, j)
		} else {
			res = firstMatch && dp(i+1, j+1)
		}
		memo[i][j] = -1
		if res {
			memo[i][j] = 1
		}
		return res
	}
	return dp(0, 0)
}

func main() {
	res := isMatch("a", ".*")
	println(res)

}
