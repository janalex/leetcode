// @ts-check

/**
 * @param {number} n
 */
function climbStairs(n) {
    const steps = new Array(45);
    steps[0] = 0, steps[1] = 1, steps[2] = 2;

    if (n < 3) { 
        return steps[n]; 
    }

    for (var i = 3; i <= n; i++) {
        steps[i] = steps[i-2] + steps[i-1]; // (n)ways = ((n-1)ways + 1) + ((n-2)ways + 2)
    }
    return steps[n];
}

console.log("2 steps: " + climbStairs(2));
console.log("3 steps: " + climbStairs(3));
console.log("4 steps: " + climbStairs(4));
console.log("5 steps: " + climbStairs(5));
