/**
 * Chapter 1 - Question 1.4
 * Palindrome Permutation
 */

 /**
  *  Checks if the string is a ...
  * @param str string to test
  */
export function isPermutatedPalindrome(str: string) : boolean {
    let map = new Map();
    for (let i = 0; i < str.length; i++) {
        let char = str[i];
        if (map.has(char)) {
            let elem = map.get(char) as number
            elem++;
            map.set(str[i], elem);
            if (elem >= 3) {
                return false;
            }
        } else {
            
        }
    }
}