import numpy as np
class LinearRegression:
    def __init__(self):
        self.coef_=None
        self.intercept_=None

    def fit(self,X,y):
        self.X=X
        self.y=y
        arrx=np.array(self.X)
        arry=np.array(self.y)
        self.x_mean=np.mean(arrx)
        self.y_mean=np.mean(arry)
        minxmean=(arrx-self.x_mean).flatten()
        minymean=arry-self.y_mean
        product=minxmean*minymean
        square=(minxmean)**2
        prosum=np.sum(product)
        squsum=np.sum(square)
        self.coef_=prosum/squsum
        self.intercept_=self.y_mean-self.x_mean*self.coef_

    def Predict(self,a):
        result=self.coef_*a+self.intercept_
        return result
obj=LinearRegression()
X=[[1],[2],[3],[4],[5]]
y=[10,20,30,40,50]
obj.fit(X,y)



