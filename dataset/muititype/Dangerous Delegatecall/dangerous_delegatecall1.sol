pragma solidity ^0.4.10;

contract Caller {
    function callAddress(address a) {
        // <yes> <report> UNCHECKED_LL_CALLS
        a.call();
    }

    function execute(bytes memory data) public {
        (bool success, ) = callee.delegatecall(data);
        require(success, "Delegatecall failed");
    }
}