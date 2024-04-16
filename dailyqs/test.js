// @ts-check
const size = 100_000;

function prepArray() {
    var arr = new Array(size);
    for(var i = 0; i < size; i++) {
        arr[i] = i;
    }
    return arr;    
}

/**
 * @param {any[]} arr
 */
function testShift(arr) {
    for (var i = 0; i < arr.length; i++) {
        arr.shift();
    }
}

/**
 * @param {any[]} arr
 */
function testPop(arr) {
    for (var i = 0; i < arr.length; i++) {
        arr.pop();
    }
}

function testUnshift() {
    const arr = new Array(size);
    for (var i = 0; i < size; i++) {
        arr.unshift(i);
    }
}

function testPush() {
    const arr = new Array(size);
    for (var i = 0; i < size; i++) {
        arr.push(i);
    }
}

var arr = prepArray();
var start = new Date().getTime();
testShift(arr);
var duration = new Date().getTime() - start;
console.log("Duration of shift is " + duration);

arr = prepArray();
start = new Date().getTime();
testPop(arr);
duration = new Date().getTime() - start;
console.log("Duration of pop is " + duration);

start = new Date().getTime();
testUnshift();
duration = new Date().getTime() - start;
console.log("Duration of unshift is " + duration);

start = new Date().getTime();
testPush();
duration = new Date().getTime() - start;
console.log("Duration of push is " + duration);
