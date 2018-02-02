# PyBoss
## Goal
In this exercise, the chief linguist, is responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, he/she has come up with a fairly simple set of metrics for assessing complexity.

The Python script `main.py` automates the analysis of any such passage using these metrics. It does the following:

* Imports a text file filled with a paragraph of text.
* Assess the passage for each of the following:
  * Approximate word count
  * Approximate sentence count
  * Approximate letter count (per word)
  * Average sentence length (in words)

## Input
The script assumes the following about the input data:
* The input file that the user provides is in a folder called "raw_data" which is in the folder from where the script is run
* The input file is a text file containing the paragraph to be analyzed

### Sample Input csv files
> “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”

## Output
The Analysis of the passage is printed to the screen.

### Sample output
```
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.56557377049
Average Sentence Length: 24.4
```