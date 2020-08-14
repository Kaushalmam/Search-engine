# Search Engine using vector space model

- The code is splitted into three different pythons files to make it readable:
1) Prepro.py: this file has a function that will preprocess the input to it.
2) out.py:  This file has the output fucntion that will give the output as in the sample output.
3) driver.py: This file has the drive code that performs the calculation for TF, IDF, TFIDF and Cosine Similarity.

Note: comments are give in each file to indcate how the process is carried out.

- For both queries and data, Preprocessing and Tokenization is done and corrospondingly TF, IDF and TFIDF dictionaries are created
using which we further calculate the document length and cosine similarity. Finally in the output function we calculate, Precision
and recall for each query and average precision and recall for these operations.


- Following the pricision and recall of the method:

FOR  10  MOST RELEVANT DOCUMENTS
Query  1
Precision  0.0  Recall  0.0
Query  2
Precision  0.2  Recall  0.13333333333333333
Query  3
Precision  0.2  Recall  0.13333333333333333
Query  4
Precision  0.1  Recall  0.05555555555555555
Query  5
Precision  0.2  Recall  0.10526315789473684
Query  6
Precision  0.4  Recall  0.2222222222222222
Query  7
Precision  0.6  Recall  0.6666666666666666
Query  8
Precision  0.2  Recall  0.5
Query  9
Precision  0.2  Recall  0.25
Query  10
Precision  0.2  Recall  0.08333333333333333
Average precision 0.23000000000000004
Average recall 0.21497076023391815

FOR  50  MOST RELEVANT DOCUMENTS
Query  1
Precision  0.0  Recall  0.0
Query  2
Precision  0.08  Recall  0.26666666666666666
Query  3
Precision  0.12  Recall  0.4
Query  4
Precision  0.04  Recall  0.1111111111111111
Query  5
Precision  0.2  Recall  0.5263157894736842
Query  6
Precision  0.12  Recall  0.3333333333333333
Query  7
Precision  0.16  Recall  0.8888888888888888
Query  8
Precision  0.06  Recall  0.75
Query  9
Precision  0.1  Recall  0.625
Query  10
Precision  0.08  Recall  0.16666666666666666
Average precision 0.096
Average recall 0.4067982456140351

FOR  100  MOST RELEVANT DOCUMENTS
Query  1
Precision  0.0  Recall  0.0
Query  2
Precision  0.1  Recall  0.6666666666666666
Query  3
Precision  0.09  Recall  0.6
Query  4
Precision  0.06  Recall  0.3333333333333333
Query  5
Precision  0.13  Recall  0.6842105263157895
Query  6
Precision  0.08  Recall  0.4444444444444444
Query  7
Precision  0.08  Recall  0.8888888888888888
Query  8
Precision  0.03  Recall  0.75
Query  9
Precision  0.06  Recall  0.75
Query  10
Precision  0.04  Recall  0.16666666666666666
Average precision 0.06700000000000002
Average recall 0.528421052631579

FOR  500  MOST RELEVANT DOCUMENTS
Query  1
Precision  0.002  Recall  1.0
Query  2
Precision  0.03  Recall  1.0
Query  3
Precision  0.03  Recall  1.0
Query  4
Precision  0.032  Recall  0.8888888888888888
Query  5
Precision  0.038  Recall  1.0
Query  6
Precision  0.032  Recall  0.8888888888888888
Query  7
Precision  0.018  Recall  1.0
Query  8
Precision  0.008  Recall  1.0
Query  9
Precision  0.016  Recall  1.0
Query  10
Precision  0.024  Recall  0.5
Average precision 0.023
Average recall 0.9277777777777778
