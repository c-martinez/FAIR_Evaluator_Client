# Python Package for FAIR Evaluator Client
### Python client to the FAIR Metrics Evaluator REST interface

#### How to install the package.

Download zip file.

Unzip it in your main folder ~/

Enter in FAIRtools/ where is setup.py

Run "python setup.py install" or with sudo if it's necessary.

Now you're ready to use FAIRtools.

#### Example:
From FAIRtools import collections

From FAIRtools import metrics 

From FAIRtools import evaluations

c = collections.collections(id)

c.title()
