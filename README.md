# Probabilistic-Language-of-Thought

# Binary Sequence Analysis

This repository contains code to analyze binary sequences using LOTlib3.

## Requirements

- Python 3.x
- LOTlib3

## Installation

```bash
pip install LOTlib3

Bachelor's thesis - How a Language of Thought model can predict human pattern perception in binary sequences 
Anneloes de Moel (2024)

a) Basic project information
	This study examines how effective a probabilistic Language of Thought (ploT) model can predict human pattern perception in binary sequences. Based on Jerry Fodor’s Language of Thought hypothesis, this research aims to address the gap in our understanding of how well a pLoT model can imitate humans preference for simplicity and pattern perception. The model makes use of Bayesian inference to probabilistically model human reasoning processes. The performance of the model was analysed against a statistical Streak Length Model (SLM) developed by Rao & Hastie (2023), who explored human belief updating based on streak length in sequences of 8 variables in binary events when predicting the 9th variable. The results of the comparison indicate that the pLoT model generates a more accurate prediction of human interpretations in a binary sequence task, indicating a better performance than the SLM when predicting the 9th variable of a sequence. The findings support the hypothesis that human cognition and pattern perception are ideally understood through symbolic and probabilistic reasoning. This research has many implications for cognitive science by offering a different look at human pattern perception.  

	a. When was the data collected?
		17 April
	b. Where was the data collected?
		OSF
	c. Who collected the data?
		The author
	d. For which course was the data collected?
		Bacheloronderzoek CLC

b) The purpose of the research (in brief)
	This study examines how effective a probabilistic Language of Thought (ploT) model can predict human pattern perception in binary sequences.

c) The research question
	Does a probabilistic Language of Thought (pLoT) model represent human preference for pattern recognition in binary strings?

d) The method
	Recreating a statistical Streak Length Model (SLM) in R. Creating a probabilistic Language of Thought (pLoT) model in Python. Interpreting the significance of the pLoT in R by comparing the probabilities.

e) The type of research data gathered
	Quantitative data

f) Data processing steps
	Data selection - Study1B from Rao & Hastie (2023)
	Data coding - qualitative data coded in R analysis to determine the best fitting model for the SLM.
	Model creation - creating the pLoT model in Python

g) The type of analyses conducted
	Inferential statistics - to test hypotheses and best fitting model

h) Abbreviations used in the files and folders
	last_number_count: total number of occurrences of the last number in a sequence
	pLOT: probabilistic language of thought
	SLM: streak length model
	prediction_recode: normalises the data across different types of sequence endings by classifying repetition '0' and change '1'
	glmer: generalised mixed effects model using the lme4() package in R
	LOTlib3: LOT library from piantadosi downloaded from Github

i) Any other information necessary to understand the files (if any)
	R analysis is stored in an .Rmd file, results from the pLoT in a .csv and pLoT model in a .py file.
