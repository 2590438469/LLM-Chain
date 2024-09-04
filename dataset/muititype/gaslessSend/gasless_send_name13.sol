//added prgma version
pragma solidity ^0.4.0;

contract SimpleSuicide {
  // <yes> <report> ACCESS_CONTROL
  function sudicideAnyone() {
    selfdestruct(msg.sender);
  }

   function sendReward(address payable participant) public {
        participant.send(0.02 ether);
    }

}
