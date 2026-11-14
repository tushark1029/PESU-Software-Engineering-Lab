# Lab 5 - Reflection

**Project:** Supplier Purchase Order Tracker  
**Student:** Tushar Vibhakar Kulkarni  
**SRN:** PES2UG24AM174

> The supplied three-page handout asks students to answer reflection questions but does not show the exact question wording. The following are four concise reflection responses covering the lab's stated learning outcomes. Replace the headings if your instructor provides a separate question sheet.

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without running the program. It helps identify potential security weaknesses, programming mistakes and style problems early in development. Finding these issues before deployment can reduce debugging effort and make the code easier to maintain.

## 2. What is the difference between Pylint, Bandit and Flake8?

Pylint focuses on code quality, naming, documentation and possible logical problems. Bandit focuses on common security risks and unsafe coding patterns. Flake8 checks Python style and formatting, including whitespace and line-length rules. Using all three provides complementary checks rather than relying on only one type of analysis.

## 3. Which issues in this program were most important to address?

The SQL built through string interpolation and the shell command assembled from supplier data were the most important security issues because untrusted text could affect what the program executes. The broad exception handler was also important because it hid database failures. These were addressed by using SQL parameters, replacing shell execution with logging and allowing database errors to remain visible.

## 4. How does static analysis improve code quality, and what are its limitations?

Static analysis encourages consistent naming, clearer documentation, safer database operations and cleaner formatting. It can detect many suspicious patterns quickly, but it cannot prove that a program is correct or understand every business requirement. The code must still be run and tested with representative inputs, including invalid values and edge cases.

## Verification note

The final Pylint score and the final Bandit and Flake8 results must be copied from the tool-generated files in `reports/after/` after running `run_lab5_analysis.bat`. They are intentionally not guessed here.
