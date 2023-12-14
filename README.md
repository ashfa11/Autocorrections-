# Autocorrections-
Artificial intelligence module project 
The spelling corrector in Python supports Tamil Language.
Based on:https://github.com/filyp/autocorrect

Installation
pip install autocorrect

Run this code to extract words from zip file into JSON file.
tar -zcvf autocorrect/data/ru.tar.gz word_count.json

Examples
>>> from autocorrect import Speller
>>> spell = Speller('ta')
>>> spell("பல்கலைக்கலகம்")

