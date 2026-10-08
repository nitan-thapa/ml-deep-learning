#Boosting 
         #Modle are trained sequentially 
         #Each new model  tries to impove the mistake of previous model
         #it reduce bias  and may increase overfitting
         #internally all use descition tree
         #types 
            #Adaboost
            #Gradient Boosting
            #XGBoost   (mostly used)   same as gradient boost but very faster
                #you have to install  pip install xgboost 
         #all last total output is comes from the combinatin of all model 
                #like y = alpha1*model1 + alpha2*model2 + alpha3*model3