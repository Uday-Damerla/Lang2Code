# Lang2Code

The Lang2Code leverages two primary techniques to generate code from natural language 
queries. First, it employs code generation models that use machine learning algorithms to 
create code based on a given query. These models learn from large datasets of human-written 
code and natural language descriptions to produce accurate and relevant code snippets. 


<br>



## [Dataset Stats]()


| Parameter | Statistics |
| -------- | ----------- | 
| Total Number of Users Queries | 525 |
| Total Number of Unique Intents | 20 |
| Total Number of  Unique Entity | 10 |
| Total Number of  Unique Python Code Snippets | 100 |



## [Custom-NER-using-Spacy](https://github.com/Elysian01/Custom-NER-using-Spacy)
Custom Named Entity Recognition annotated using NER Annotated by tecoholic and Spacy for training the model

## Get Started

[Download](https://drive.google.com/drive/folders/1-gWCai8P_kkcuBMKd4WyTVPI0drsV6rP?usp=sharing) glove embeddings folder and place it inside "./Lang2Code/intent_word_emb" folder

[Download](https://drive.google.com/drive/folders/1khbEs2sj4a3tKqCpH-AvN1siFkYdEhYX?usp=sharing) entity recognition model folder and place it inside "./Lang2Code/models" folder



## Credits

* NER Annotator -  https://github.com/tecoholic/ner-annotator
* `spacy` - https://github.com/explosion/spaCy
* Custom NER for Extracting Disease Entities Blog - https://medium.com/analytics-vidhya/custom-ner-for-extracting-disease-entities-c620aca2e1bb
