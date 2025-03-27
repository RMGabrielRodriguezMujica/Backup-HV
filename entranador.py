import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open('./dataABLEIOU1000.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# model = RandomForestClassifier()

model = RandomForestClassifier(
    n_estimators=10000,  # Aumenta el número de árboles
    max_depth=20,  # Restringidor  de la profundidad para evitar sobreajuste
    min_samples_split=5,  # Evita ramas pequeñas con pocos datos
    min_samples_leaf=2,  # Evita hojas con pocos datos
    bootstrap=True,  # Usa muestreo con reemplazo
    n_jobs=-1,  # Usa todos los núcleos del CPU
    random_state=42
)

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('modelABLEIOU1000.p', 'wb')
pickle.dump({'model': model}, f)
f.close()

# model.p = ABL
# modelV2.p = ABCDFGGHIJKLMNOPQRSTUVWXYZ

