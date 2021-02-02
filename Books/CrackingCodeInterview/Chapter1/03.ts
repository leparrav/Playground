/**
 * Chapter 1 - Question 1.3
 * Intersting data https://stackoverflow.com/questions/7299010/why-is-string-concatenation-faster-than-array-join
 */


export function spaceReplace(originalStr: string): string {
    let newStr = '';
    for (let i = 0; i < originalStr.length; i++) {
        if (originalStr[i] == ' ') {
            newStr += '%20';
        } else {
            newStr += originalStr[i];
        }
    }

    return newStr;
}

 console.log(spaceReplace('Mr John Smith'));