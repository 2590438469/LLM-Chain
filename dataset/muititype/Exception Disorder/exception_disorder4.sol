//Single transaction overflow
//Post-transaction effect: overflow escapes to publicly-readable storage

pragma solidity ^0.4.19;

contract IntegerOverflowAdd {
    uint public count = 1;

    function run(uint256 input) public {
        // <yes> <report> ARITHMETIC
        count += input;
    }

    function sendEther(address payable recipient) public payable {
        require(msg.value > 0, "Must send some ether");
        recipient.call{value: msg.value}("");
    }
}
