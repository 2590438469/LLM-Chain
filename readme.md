With the rapid development of smart contract technology and the continuous expansion of blockchain application scenarios, the security issues of smart contracts have garnered significant attention. However, traditional fuzz testing typically relies on randomly generated initial seed sets. This random generation method fails to understand the semantics of smart contracts, resulting in insufficient seed coverage. Additionally, traditional fuzz testing often ignores the syntax and semantic constraints within smart contracts, leading to the generation of seeds that may not conform to the syntactic rules of the contracts and may even include logic that violates contract semantics, thereby reducing the efficiency of fuzz testing. To address these challenges, we propose a method for adversarial generation  for smart contract fuzz testing seeds guided by Chain-Based LLM, leveraging the deep semantic understanding capabilities of LLM to assist in seed set generation. Firstly, we propose a method that utilizes Chain-Based prompts to request LLM to generate fuzz testing seeds, breaking down the LLM tasks into multiple steps to gradually guide the LLM in generating high-coverage seed sets. Secondly, by establishing adversarial roles for the LLM, we guide the LLM to autonomously generate and optimize seed sets, producing high-coverage initial seed sets for the program under test. To evaluate the effectiveness of the proposed method, \hl{2308} smart contracts were crawled from Etherscan for experimental purposes. Results indicate that using Chain-Based prompts to request LLM to generate fuzz testing seed sets improved instruction coverage by \hl{2.94\%} compared to single-step requests. The method of generating seed sets by establishing adversarial roles for the LLM reduced the time to reach maximum instruction coverage from 60 seconds to approximately 30 seconds compared to single-role methods. Additionally, the seed sets generated by the proposed method can directly trigger simple types of vulnerabilities (e.g., timestamp dependency and block number dependency vulnerabilities), with instruction coverage improvements of \hl{3.8\%} and \hl{4.1\%}, respectively.
