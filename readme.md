# LLM-Chain
LLM-Chain is a fuzz testing tool that leverages LLMs to generate test cases prior to the fuzz testing process.

We compiled each step of the method into separate Python files to help readers better understand the implementation details. 

For example, conductP1.py is responsible for reading the contract source code, assembling the P1 prompts, and saving them to the prompt folder; refineTask.py requests the LLM to optimize the P1 prompts and saves the results in the same folder; requestTask.py then uses the generated prompts to request the LLM and saves the responses in the stageResult folder.


## Run

```
make
```
The script will store the generated initial test case set in the stageResult folder.

If you use ItyFuzz as the fuzz testing tool, you can use the interface provided in convert.py to convert the test case set into a seed set that can be loaded by ItyFuzz.

## Result

The three numbers in the metrics column represent TP (True Positives), FP (False Positives), and the total number of vulnerabilities, respectively. The method proposed in paper shows a 1.5% improvement in average instruction coverage.The F1-score also increased by 0.072.
![image](https://github.com/user-attachments/assets/65bbaed3-9bdb-461e-ae76-a6b8db566967)
