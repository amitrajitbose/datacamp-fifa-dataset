Exploratory Data Analysis of **FIFA Soccer Data-set :**

###### Overview
This dataset contains details of over 8800 football players and various attributes like ratings, defence, speed and other skills. We need to implement a relationship between the rating with another attribute on which the ratings of a football player depends.

| Data Source | Language | Libraries Used | ipython Notebook | .html Report |
|-------------|----------|----------------|------------------|-------------|
| [DataCamp](https://www.datacamp.com/courses/intro-to-python-for-data-science) | Python | pandas, matplotlib, numpy, sklearn | [EDA.ipynb](https://github.com/amitrajitbose/datacamp-fifa-dataset/blob/master/EDA.ipynb) | [EDA.html](https://rawgit.com/amitrajitbose/datacamp-fifa-dataset/master/EDA.html) |


###### Result
A pseudo-model which,

Given a new football player's positioning, predicts the rating of the player.

```Python

# Pseudo Model :

def predict(pos):
    
    '''This function returns:
       The estimated rating given the positioning is entered as a parameter
    '''
    return round((model.predict(pos)).tolist()[0][0])
```

###### Usage
Pass the positioning variable to the **predict()** method and obtain the estimated value of rating as an integer. <br>
An example has been shown in the last shell of the notebook.
