// @ts-check

/**
 * @param {number[][]} matches
 * @return {number[][]}
 */
var findWinners = function(matches) {
    /** @type Set<number> */
    const zeroLost = new Set();
    /** @type Set<number> */
    const oneLost = new Set();
    /** @type Set<number> */
    const moreLost = new Set();

    for (const m of matches) {
        const w = m[0], l = m[1];
        if (!moreLost.has(w) && !oneLost.has(w)) {
            zeroLost.add(w);
        }
        if (zeroLost.has(l)) {
            zeroLost.delete(l);
            oneLost.add(l);
        } else if (oneLost.has(l)) {
            oneLost.delete(l);
            moreLost.add(l);
        } else if (!moreLost.has(l)) {
            oneLost.add(l);
        }
    }
    /** @type number[][] */
    const result = new Array(2);
    result[0] = Array.from(zeroLost).sort((a, b) => a - b);
    result[1] = Array.from(oneLost).sort((a, b) => a - b);
    return result;
};

var result = findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]);
console.log(result);
