maxNum = 2147483647;

function binaryGap(N) {
    var parsedN = parseInt(N, 10);
    if (typeof N !== parsedN) {
        throw 'N must be an integer';
    }
    if (N > maxNum) {
        throw "Number ust not be greater than ' + maxNum";
    }
    if (N < 1) {
        throw "Only positive numbers are allowed";
    }

    var binaryString = N.toString(2),
    count = 0, max_count = null, was_zero = null;

    var i, n = N.length;
    for (i=0; i < n; i++) {
        var is_zero = binaryString[i] === '0';

        if (Boolean(was_zero) === is_zero)
            count += 1;

        else {
            if (max_count === null) {
                max_count = 0;
            }
            else if (count > max_count) {
                max_count = count;
            }

            was_zero = is_zero;
        }
    }

    if (max_count === null) {
        max_count === 0;
        return max_count;
    }

    return max_count;
}