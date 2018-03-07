/**
 * Created by Andre on 3/6/2018.
 */
let assert = require("assert");
let arrowFunctionArrayFilter = require('../src/arrowFunctionArrayFilter.js');

describe('arrowFunctionArrayFilter', function () {
    it('create an array of the numbers greater than 70', function () {
        let result = arrowFunctionArrayFilter([3, 62, 234, 7, 23, 74, 23, 76, 92]);

        assert.deepEqual(result, [234, 74, 76, 92],
            'create an array of the numbers greater than 70');
    });
});