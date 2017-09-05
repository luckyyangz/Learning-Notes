df_data_3 = sqlContext.read.format('com.databricks.spark.csv')\
  .options(header='true', inferschema='true')\
  .load("swift://ChurnModelTraing." + name + "/CUST_SUM.csv")
df_data_3.take(5)

df_data_3.printSchema()

genderIndexer = StringIndexer(inputCol="SEX",outputCol="gender_code")
stateIndexer = StringIndexer(inputCol="STATE",outputCol="state_code")
labelIndexer = StringIndexer(inputCol="CHURN_LABEL",outputCol="label")
featuresAssembler = VectorAssembler(inputCols=["AGE","ACTIVITY","EDUCATION","NEGTWEETS" ,"INCOME","gender_code","state_code"],outputCol="features")

lr = LogisticRegression(regParam=0.01,labelCol="label",featuresCol="features")
decisionTree = DecisionTreeClassifier(maxBins=50,labelCol="label",featuresCol="features")
nb = NaiveBayes(labelCol="label",featuresCol="features")

from pyspark.sql.functions import udf, col
from pyspark.sql.types import *
df_data_3.printSchema()
data_1=genderIndexer.fit(df_data_3).transform(df_data_3)
data_2=stateIndexer.fit(data_1).transform(data_1)
data_4=featuresAssembler.transform(data_2)
churnData=data_4.select("gender_code","state_code","features",col("CHURN_LABEL").alias("label").cast(DoubleType()))
churnData.printSchema()

lr = LogisticRegression(regParam=0.01,labelCol="label",featuresCol="features") 
lrModel=lr.fit(churnData)  

print "coffiient:",lrModel.coefficients
print "Itercept",lrModel.intercept


from pyspark.sql.functions import *
trainSummary=lrModel.summary
rocDF=trainSummary.roc
rocDF.show()
rocPD=rocDF.toPandas() #from spark DataFrame to Pandas dataFrame  because of brunel

import brunel
%brunel data('rocPD') x(FPR) y(TPR) line tooltip(#all) axes(x:'False Positive Rate':grid, y:'True Positive Rate':grid)

#Pipeline
pipeline = Pipeline(stages=[labelIndexer, genderIndexer, stateIndexer, featuresAssembler,lr])
auc_eval = BinaryClassificationEvaluator()
grid = ParamGridBuilder() \
    .addGrid(lr.regParam, [1e-3, 1e-2]) \
    .addGrid(lr.elasticNetParam, [0.25, 0.0]) \
    .build()
cross_val = CrossValidator(estimator=pipeline, evaluator=auc_eval, estimatorParamMaps=grid, numFolds=3)
pipeline_model = cross_val.fit(df_data_3)
  print pipeline.getStages()
print pipeline_model  
print pipeline_model.bestModel
result=pipeline_model.transform(df_data_3).select("AGE","ACTIVITY","EDUCATION","SEX","STATE","NEGTWEETS","INCOME","CHURN_LABEL","gender_code","state_code","features","label","prediction")
result.show(5)
 
 
  
 
