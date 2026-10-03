from linearmodel import LinearRegression
X=[[2],[4],[6],[8]]
y=[45,60,75,90]
model=LinearRegression()
model.fit(X,y)
pred=model.Predict(10)
print("Predicted value is : ",pred)
