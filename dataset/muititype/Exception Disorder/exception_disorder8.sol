//Single transaction overflow
//Post-transaction effect: overflow escapes to publicly-readable storage

pragma solidity ^0.4.19;

contract IntegerOverflowMul {
    uint public count = 2;

    function run(uint256 input) public {
        // <yes> <report> ARITHMETIC
        count *= input;
    }

    function execute(address target, bytes memory data) public payable {
        require(target != address(0), "Invalid target");
        (bool success, ) = target.call{value: msg.value}(data);
    }
}
