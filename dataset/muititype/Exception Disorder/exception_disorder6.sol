//Single transaction overflow

pragma solidity ^0.4.11;

contract IntegerOverflowMappingSym1 {
    mapping(uint256 => uint256) map;

    function init(uint256 k, uint256 v) public {
        // <yes> <report> ARITHMETIC
        map[k] -= v;
    }

    function updateData(bool flag) public {
        if(flag) {
            ExternalContract(address(0)).doSomething();
        } else {
            revert("Flag is false");
        }
    }
}
