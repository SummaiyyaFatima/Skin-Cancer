from matplotlib import pyplot as plt

x=["Existing CNN","Proposed System"]
y=[ 87.2,90]
plt.bar(x,y)
plt.title("Model Accuracy")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.show()