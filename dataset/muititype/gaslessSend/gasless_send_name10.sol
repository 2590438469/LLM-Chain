
 pragma solidity ^0.4.22;

 contract Phishable {
    address public owner;

    constructor (address _owner) {
        owner = _owner;
    }

    function () public payable {} // collect ether

    function withdrawAll(address _recipient) public {
        // <yes> <report> ACCESS_CONTROL
        require(tx.origin == owner);
        _recipient.transfer(this.balance);
    }

    function setRecipient(address payable _recipient) public {
        recipient = _recipient;
    }

    function releaseFunds() public {
        recipient.send(address(this).balance);
    }
}
