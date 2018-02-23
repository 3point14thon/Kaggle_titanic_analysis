# Titanic: Machine Learning from Disaster Challenge

## Motivation
* Implement data science practices learned from online courses
* Complete a project with minimal guidance

## Project Overview
### Objective
This project aims to predict if a passenger of the RMS Titanic survived its
final voyage. Kaggles' [Titanic: Machine Learning from
Disaster](https://www.kaggle.com/c/titanic) project.

## Methods

### Python VS iPython
Jupyter Notebook using iPython is the standard for this sort of project, it's
easy to use and easy to follow. That being said all of my coding files for this project are in python rather than iPython. Why? I have limited access on one of the systems I am using to make this project and am unable to install jupyter note book or iPython. The amount of time I use that system is large enough where I felt it would be more beneficial to code in Python than iPython.

### Cleaning the data
Features like passenger name, ticket, and cabin were dropped to keep the data
simple. If the model performs poorly they can be added back in. Front fill was
used to replace all NaN values in the training data. Filling age with the average would have increased the chance for those instances to be labeled as "not
survivors" because the average age was 30 and that's the bias for that age.
Using front fill on the embarkation feature should keep a similar distribution
and provides a simple way to fill in missing values.

### Modeling
Knearest Neighbors using four nearest
neighbors was used for this project. The number of neighbors was determined
using trial and error. Knearest Neighbors was selected as a model because of
it's simplicity.

### Conclusion/Results
The model got a predicted 88.9% accuracy. I haven't submitted this to Kaggle yet
so this number is unvetted. After looking at several of these projects performed
by other Kaggle members I am a little skeptical that I would do this well on my
first shot with little to no modifications on my model but I'm unable to see
anywhere I might have an information leak.

### Improvements
Looking at the [sklearn ML
map](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) it
suggests trying Linear SVC before using Kneighbors. I could also try adding back
in some of the more complicated features I took out like passenger name. This
project was also completed before I knew about cross validation, in the future
I'll aim to validate my models using CV or with holding additional data to avoid
information leakage. I wrote this README much later than I should have. On
future projects I plan on starting the README at the same time as the project so
I can document my progress and findings as the project progresses.
