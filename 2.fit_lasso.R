require(glmnet)
require(broom)
library(dplyr)
hr=read.csv(file='C:\\Users\\Guan-Ting Chen\\Desktop\\NCCU course2018\\applied regrssion\\final report\\hr_final.csv',header = T)
#lasso
lasso=glmnet(x=as.matrix(hr[2:182]),y=hr$left,alpha = 1,family = "binomial")

#plot 
plot(lasso, xvar='lambda', main="Lasso")

#find best lambda
cv.lasso = cv.glmnet(x=as.matrix(hr[2:182]),y=hr$left,alpha = 1,family = "binomial")
best.lambda = cv.lasso$lambda.min
best.lambda

#under best lambda the coefficient and plot
plot(lasso, xvar='lambda', main="Lasso")
abline(v=log(cv.lasso$lambda.min), col="blue", lty=5.5 )
coef(cv.lasso, s = "lambda.min")

#lasso
select.ind = which(coef(cv.lasso, s = "lambda.min") != 0)
select.ind = select.ind[-1]-1
select.varialbes = colnames(hr[2:182])[select.ind]
select.varialbes


filogit=glm(left~satisfaction_level+
              last_evaluation                    
            +number_project+average_montly_hours+time_spend_company+
          Work_accident+satisfaction_level.2+satisfaction_level.3+
          last_evaluation.2+last_evaluation.3+number_project.2+
          number_project.3+average_montly_hours.2+average_montly_hours.3+
          time_spend_company.2+time_spend_company.3+position_IT+
position_RandD.position_accounting+position_management+
position_product_mng+position_sales+position_support+salary_low+
salary_medium+satisfaction_level.last_evaluation+
satisfaction_level.number_project+satisfaction_level.average_montly_hours+
satisfaction_level.time_spend_company+satisfaction_level.Work_accident+
satisfaction_level.promotion_last_5years+satisfaction_level.position_IT+
satisfaction_level.position_RandD+satisfaction_level.position_hr+
satisfaction_level.position_management+satisfaction_level.position_marketing+
satisfaction_level.position_sales+satisfaction_level.position_support+
satisfaction_level.salary_low+satisfaction_level.salary_medium+
last_evaluation.number_project+last_evaluation.average_montly_hours+
last_evaluation.time_spend_company+last_evaluation.Work_accident+
last_evaluation.position_IT+last_evaluation.position_RandD+
last_evaluation.position_accounting+last_evaluation.position_management+
last_evaluation.position_product_mng+last_evaluation.position_sales+
last_evaluation.position_support+last_evaluation.salary_low+
last_evaluation.salary_medium+number_project.average_montly_hours+
number_project.time_spend_company+number_project.promotion_last_5years+
number_project.position_IT+number_project.position_RandD+
number_project.position_accounting+number_project.position_hr+
number_project.position_management+number_project.position_marketing+
number_project.position_product_mng+number_project.position_sales+
number_project.position_support+number_project.salary_low+
number_project.salary_medium+average_montly_hours.time_spend_company+
average_montly_hours.promotion_last_5years+average_montly_hours.position_IT+
average_montly_hours.position_RandD+average_montly_hours.position_accounting+
average_montly_hours.position_hr+average_montly_hours.position_management+
average_montly_hours.position_marketing+average_montly_hours.position_product_mng+
average_montly_hours.position_sales+average_montly_hours.position_support+
average_montly_hours.salary_low+average_montly_hours.salary_medium+
time_spend_company.Work_accident+time_spend_company.promotion_last_5years+
time_spend_company.position_IT+time_spend_company.position_RandD+
time_spend_company.position_accounting+time_spend_company.position_hr+
time_spend_company.position_management+time_spend_company.position_marketing+
time_spend_company.position_product_mng+time_spend_company.position_sales+
time_spend_company.position_support+time_spend_company.salary_low+
time_spend_company.salary_medium+Work_accident.promotion_last_5years+
Work_accident.position_IT+Work_accident.position_RandD+
Work_accident.position_accounting+Work_accident.position_hr+
Work_accident.position_management+Work_accident.position_marketing+
Work_accident.position_product_mng+Work_accident.position_sales+
Work_accident.position_support+Work_accident.salary_low+
Work_accident.salary_medium+promotion_last_5years.position_IT+
promotion_last_5years.position_RandD+promotion_last_5years.position_accounting+
promotion_last_5years.position_hr+promotion_last_5years.position_management+
promotion_last_5years.position_marketing+promotion_last_5years.position_sales+
promotion_last_5years.salary_low+promotion_last_5years.salary_medium+
position_IT.salary_low+position_IT.salary_medium+position_RandD.salary_low+
position_accounting.salary_low+position_hr.salary_low+position_hr.salary_medium+
position_management.salary_low+position_management.salary_medium+
position_marketing.salary_low+position_marketing.salary_medium+
position_product_mng.salary_low+position_product_mng.salary_medium+
position_sales.salary_low+position_sales.salary_medium+
position_support.salary_low+position_support.salary_medium,data = hr,family = 'binomial')


summary(filogit)
aa=tidy(filogit)
bb=aa[c(1,2,5)]
tt=aa %>% filter(p.value<0.01)
tt$term