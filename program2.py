const decodeTheRing = function (s, p) {
    const m = s.length;
    const n = p.length;
    const dp = Array(m + 1).fill(false).map(() => Array(n + 1).fill(false));

    // Base case: empty pattern matches empty string
    dp[0][0] = true;

    // Initialize dp for patterns that begin with '*'
    for (let j = 1; j <= n; j++) {
        if (p[j - 1] === '*') {
            dp[0][j] = dp[0][j - 1];
        }
    }

    // Fill the DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (p[j - 1] === '*') {
                // '*' matches zero or more characters
                dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
            } else if (p[j - 1] === '?') {
                // '?' matches exactly one character
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                // Regular character match
                dp[i][j] = dp[i - 1][j - 1] && s[i - 1] === p[j - 1];
            }
        }
    }

    return dp[m][n];
};

module.exports = decodeTheRing;
