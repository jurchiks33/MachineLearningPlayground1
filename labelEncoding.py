#Label Encoding
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
input_classes = ['audi', 'ford', 'audi', 'toyota', 'ford', 'bmw']

label_encoder.fit(input_classes)
print("\nClass mapping:")
for i, item in enumerate(label_encoder.classes_):
    print(f"{item} --> {i}")