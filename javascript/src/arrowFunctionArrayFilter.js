/**
 * Created by Andre on 3/6/2018.
 */
// Arrow function
module.exports = function arrowFunctionArrayFilter(arr){
    let largestVal = arr.filter(number => number > 70);

    return largestVal;
};

//regular function
module.exports = function func_FunctionArrayFilter(arr){
    let largestVal = arr.filter(function(number){
        return number > 70;
    });

    return largestVal;
};