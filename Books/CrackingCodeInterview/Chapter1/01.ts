// Test cases
const testStrings = new Array(1000);
for(let i=0; i < testStrings.length;i++) {
    testStrings[i] = Math.random().toString(36).substring(7);
}

/**
 * Without Datastructures. Run time O(n^2)
 * @param testString 
 */
function isUniqueWOD(testString: string): boolean {
    for(let i = 0; i < testString.length; i++) {
        let currentChar = testString[i];
        for(let j = i+1; j < testString.length; j++) {
            if (currentChar == testString[j]) {
                return false;
            }
        }
    }

    return true;
}

/**
 * Test if a string is... Using hashmaps O(n)
 * @param testString 
 */
function isUnique(testString){
    let hm = [];
    for (let i = 0; i < testString.length; i++) {
        if (hm.indexOf(testString[i]) != -1) {
            return false;
        }
        hm[i] = testString[i];
    }
    return true;
}

console.time("profiler");
console.log('Test without Data structures')
for (let item of testStrings)
{
    isUniqueWOD(item);
}
console.timeEnd("profiler");

console.time("profiler");
console.log('Test with Data structures')
for (let item of testStrings)
{
    isUnique(item);
}
console.timeEnd("profiler");
