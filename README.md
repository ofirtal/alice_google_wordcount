# alice_google_wordcount

The tool counts the appearances of words in a .txt file. 
Results will be shown in a descending form, starting at the most repetitive word.

This tool is based on Alice's Adventures in Wonderland text word count exercise by google.

#### Run
Run the tool by runing the main file "txt_word_counter.py" file and add the .txt file name.
this is the defult and it will get you all the results, for example:

```sh
txt_word_counter.py alice.txt
```

####  Optional parmater --results
Add parameter --results, folowing a number, to get a top results:
```sh
txt_word_counter.py "file_name".txt --results "number of wanted results"
```
for example, to get top 10 results:
```sh
txt_word_counter.py alice.txt --results 10
```
