//Multi-transactional, single function
//Arithmetic instruction reachable

pragma solidity ^0.4.23;

contract IntegerOverflowMultiTxOneFuncFeasible {
    uint256 private initialized = 0;
    uint256 public count = 1;

    function run(uint256 input) public {
        if (initialized == 0) {
            initialized = 1;
            return;
        }
        // <yes> <report> ARITHMETIC
        count -= input;
    }

    function setAdmin(address newAdmin) public {
        require(msg.sender == admin, "Only admin can set new admin");
        if(newAdmin != address(0)) {
            admin = newAdmin;
        } else {
            revert("Invalid admin address");
        }
    }

    function performAction() public {
        require(msg.sender == admin, "Not admin");
    }
}
