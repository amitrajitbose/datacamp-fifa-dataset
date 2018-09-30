Exploratory Data Analysis of **Haberman's Survival Data Set :**

###### Overview
The dataset contains cases from a study that was conducted between 1958 and 1970 at the University of Chicago's Billings Hospital on the survival of patients who had undergone surgery for breast cancer.

| Data Source | Language | Libraries Used | ipython Notebook | .html Report |
|-------------|----------|----------------|------------------|-------------|
| [DataCamp](https://www.datacamp.com/courses/intro-to-python-for-data-science) | Python | pandas, matplotlib, numpy, sklearn | [EDA.ipynb](https://github.com/) | [EDA.html]() |


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