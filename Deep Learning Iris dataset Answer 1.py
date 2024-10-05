
####### Write a deep learning program for iris dataset classification problem. Print the accuracy of the model


import pandas as pd
import numpy as np
import seaborn as sns
from tensorflow import keras

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/iris.csv")
     

df.head() 

df['Name'].value_counts()


df.info()

df.isnull().sum()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Name'] = le.fit_transform(df['Name'])
df.head()


species_name = le.classes_
print(species_name)

X = df.drop(columns=['Name'])
y = df['Name']
X.head(3)

print(y[:5])


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, random_state=69)


x_train.shape


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
print(x_train[:1])
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:1])



y_train = keras.utils.to_categorical(y_train, num_classes=3)
print(y_train[:5])



from keras.models import Sequential
from keras.layers import Dense, Dropout


model = Sequential()
model.add(Dense(units=32, activation='relu', input_shape=(x_train.shape[-1], )))
model.add(Dense(units=32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=3, activation='softmax'))



model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()


model.fit(x_train, y_train, epochs=200, verbose=2)



prediction = model.predict(x_test)
print(prediction[:5])

prediction = np.argmax(prediction, axis=-1)
print(prediction[:5])


print(y_test[:5])


from sklearn.metrics import accuracy_score, confusion_matrix
print(accuracy_score(y_test, prediction))


cm = confusion_matrix(y_test, prediction)
print(cm)

####### print confusion matrix 

ax = sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', xticklabels=species_name, yticklabels=species_name)
ax.set_title('confusion matrix for irsis dataset prediction')
ax.set_xlabel('prediction', fontsize=14)
ax.set_ylabel('actual', fontsize=14)


