require(glmnet)
require(broom)
library(dplyr)
library(car)
hr_xtrain=read.csv(file='C:\\Users\\Guan-Ting Chen\\Desktop\\NCCU course2018\\applied regrssion\\final report\\hr_x_train.csv',header = T)
hr_xtest=read.csv(file='C:\\Users\\Guan-Ting Chen\\Desktop\\NCCU course2018\\applied regrssion\\final report\\hr_x_test.csv',header = T)
hr_ytrain=read.csv(file='C:\\Users\\Guan-Ting Chen\\Desktop\\NCCU course2018\\applied regrssion\\final report\\hr_y_train.csv',header = T)
hr_ytest=read.csv(file='C:\\Users\\Guan-Ting Chen\\Desktop\\NCCU course2018\\applied regrssion\\final report\\hr_y_test.csv',header = T)
hr_training=read.csv(file='C:\\Users\\Guan-Ting Chen\\Desktop\\NCCU course2018\\applied regrssion\\final report\\hr_training.csv',header = T)
hr_testing=read.csv(file='C:\\Users\\Guan-Ting Chen\\Desktop\\NCCU course2018\\applied regrssion\\final report\\hr_testing.csv',header = T)
training_lasso=read.csv(file='C:\\Users\\Guan-Ting Chen\\Desktop\\NCCU course2018\\applied regrssion\\final report\\hr_training_lasso.csv',header = T)
testing_lasso=read.csv(file='C:\\Users\\Guan-Ting Chen\\Desktop\\NCCU course2018\\applied regrssion\\final report\\hr_testing_lasso.csv',header = T)



null=glm(left ~ 1,data=training_lasso,family=binomial)
full=glm(left ~ .,data=training_lasso,family=binomial) 
forward.lm = step(null,scope=list(lower=null, upper=full),direction="forward")
summary(forward.lm)#29

forw=tidy(forward.lm)
forw$term

backward.lm = step(full,scope = list(upper=full),direction="backward")  
summary(backward.lm) #31
back=tidy(backward.lm)
back$term
anova(backward.lm)
formula(backward.lm)
etasq(backward.lm)
both.lm=step(null, scope = list(upper=full), direction="both") #29
summary(both.lm)
both=tidy(both.lm)
both$term
#compare
probabilities <- full%>% predict(testing_lasso[2:33],type = "response")
predicted.classes <- ifelse(probabilities > 0.5, "1", "0")
# Prediction accuracy
observed.classes <- testing_lasso$left
mean(predicted.classes == observed.classes)


# Make predictions
probabilities <- predict(forward.lm, testing_lasso[2:33], type = "response")
predicted.classes <- ifelse(probabilities > 0.5, "1", "0")
# Prediction accuracy
observed.classes <-testing_lasso$left
mean(predicted.classes == observed.classes)


probabilities <- predict(both.lm, testing_lasso[2:33], type = "response")
predicted.classes <- ifelse(probabilities > 0.5, "1", "0")
# Prediction accuracy
observed.classes <-testing_lasso$left
mean(predicted.classes == observed.classes)

