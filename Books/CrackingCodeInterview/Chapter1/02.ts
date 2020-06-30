/**
 * Check if a ....  Run time: 0(N)
 * @param str1 
 * @param str2 
 */
export function isPermutation(str1: string, str2: string): boolean {
    if (str1.length != str2.length) {
        return false;
    }

    let HmObj: Map<string, number> = new Map();
    let HmaTarget: Map<string, number> = new Map();
    for (let i = 0; i < str1.length; ++i) {
        increaseHashMap(HmObj, str1[i]);
        increaseHashMap(HmaTarget, str2[i]);
    }
    
    for (let key of HmObj.keys()) {
        console.log(key);
        if (!HmaTarget.has(key) ||(HmObj.get(key) != HmaTarget.get(key))) {
            return false;
        }
    }

    return true;
}

function increaseHashMap(hashMap: Map<string, number>, char: string): void {
    if (hashMap.has(char)) {
        let val = hashMap.get(char) as number;
        hashMap.set(char, val++);
    }
    else {
        hashMap.set(char, 1);
    }
}


console.log(isPermutation('hola', 'cato'));
console.log(isPermutation('hola', 'hoax'));
console.log(isPermutation('hola', 'loah'));
console.log(isPermutation('hola', 'lo4ah'));
