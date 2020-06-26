// Test cases
const testStrings: string[] = new Array(1000);
for(let i=0; i < testStrings.length; ++i) {
    testStrings[i] = Math.random().toString(36).substring(7);
}

/**
 * Without Datastructures. Run time O(n^2)
 * @param testString 
 */
export function isUniqueWOD(testString: string): boolean {
    for(let i = 0; i < testString.length; ++i) {
        for(let j = i+1; j < testString.length; ++j) {
            if (testString[i] == testString[j]) {
                return false;
            }
        }
    }
    return true;
}

/**
 * Test if a string is... Using hashmaps O(n) from ES5
 * @param testString 
 */
export function isUnique(testString: string){
    let chars = new Set();
    for (let i = 0; i < testString.length; ++i) {
        if (chars.has(testString[i])) {
            return false;
        }
        chars.add(testString[i]);
    }
    return true;
}

console.time("Test without Data structures");
for (let item of testStrings)
{
    isUniqueWOD(item);
}
console.timeEnd("Test without Data structures");

console.time("Test with Data structures");
for (let item of testStrings)
{
    isUnique(item);
}
console.timeEnd("Test with Data structures");