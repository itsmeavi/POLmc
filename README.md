# POLmc

Implementation of Word fragment of the POL model checking in the paper: https://arxiv.org/abs/2205.00784
Also published in THE 31ST INTERNATIONAL JOINT CONFERENCE ON ARTIFICIAL INTELLIGENCE (IJCAI-ECAI 22)
By Sourav Chakraborty, Avijeet Ghosh, Sujata Ghosh, Francois Schwarzentruber


Prerequisite packge:
pip install automathon

*If after installing automathon, running word.py on Python3 still gives error: FileNotFoundError for file or directory 'dot', using the following command can help:*
sudo apt install graphviz





The file has the drone model and the plan verification formula in the paper as input and the function wordMC has been called on it.

Formula Syntax:

\phi = p  |  AND(\phi,\phi)  |  OR(\phi,\phi)   |   KP(a,\phi)   |   DIM(w,\phi)    |   NOT(\phi)

Here p is a proposition, a is an agent, w is a word on an alphabet, DIM(w,\phi) is actually <w>\phi in POL syntax in paper, KP(a,\phi) is \hat{K_a}\phi, rest is self-explanatory.
Note: No Space to be given between commas.


The syntax to be followed for NFA in expectations and model can be found in the file.
