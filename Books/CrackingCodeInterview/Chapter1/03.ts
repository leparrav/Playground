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