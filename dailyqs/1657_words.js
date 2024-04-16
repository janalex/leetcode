// @ts-check

/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
function closeStrings(word1, word2) {
    if (word1.length !== word2.length) {
        return false;
    }

    /** @type Map<string, number> */
    const l1 = new Map()
    /** @type Map<string, number> */
    const l2 = new Map();

    for (var i = 0; i < word1.length; i++) {
        const c1 = word1[i], c2 = word2[i];
        l1.set(c1, (l1.get(c1) ?? 0) + 1);
        l2.set(c2, (l2.get(c2) ?? 0) + 1);
    }
    if (l1.size !== l2.size) {
        // number of unique letters differs between two words
        return false;
    }

    // we need same letters in both words
    for (const c of l1.keys()) {
        if (!l2.has(c)) {
            return false;
        }
    }

    // sort occurences and compare, we need same occurences in 
    // both strings after sorting by number of occurences
    var occs1 = Array.from(l1.values()).sort((a, b) => a - b);
    var occs2 = Array.from(l2.values()).sort((a, b) => a - b);
    return occs1.every((value, index) => value === occs2[index]);
};

const testCases = [
    ["abc", "bca"],
    ["a", "aa"],
    ["cabbba", "abbccc"],
    ["asa", "ssx"]
];

for (const words of testCases) {
    console.log(words[0] + " and " + words[1] + ": " + closeStrings(words[0], words[1]));
}
