# Artificial-Intelligence---k-Nearest-Neighbour
k Nearest Neighbour code example

-Assumption: You already understand the concept of k Nearest Neighbour

-Given: Given a set of data containing 4000 news on sheet DataTrain and 1000 news on sheet DateTest with four attributes: Like, Provoke, Comment and Emotion with value 0 to 100, and the Hoax class attribute that is 1 for yes and 0 for no. It's on Dataset.xlsx file. Use 4000 news from DataTrain sheet to find good value of k. Then use the value of k you got from DataTrain for to identify 1000 data on DataTest

-Hint:
1. File knnTrain.py only for finding the good value of k, you can change the value of k on line 7 of it
2. File knnTrain.py only for observe the value of k and it accuracy
3. File knnTest.py to identify data from sheet DataTest base on sheet DataTrain
4. File kknTrain.py and kknTest.py are not related, it can run without the other one
5. In a nutshell, knnTrain.py for found good value of k and knnTest.py to implement value of k that has been observed before
6. In many case, people use cross validation for optimum accuracy. In this code i don't use it. this code only show you how k Nearest Neighbour work.
7. Important, read the Guide.txt before run the code