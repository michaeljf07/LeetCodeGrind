function clearDigits(s: string): string {
    let arr = [];

    for (let i = 0; i < s.length; i++) {
        if (!('0' <= s[i] && s[i] <= '9')) {
            arr.push(s[i]);
        } else {
            arr.pop();
        }
    }

    return arr.join('')
};