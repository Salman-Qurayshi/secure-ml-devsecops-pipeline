import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from utils import get_data_path
import joblib
from utils import get_data_path

# 1. Load preprocessed data
df = pd.read_csv(get_data_path("iris_processed.csv"))

# 2. Split features and target
X = df.drop(columns=["target"])
y = df["target"]

# 3. Split into train/test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Initialize the model
model = LogisticRegression(max_iter=200)

# 5. Train the model
model.fit(X_train, y_train)

# 6. Make predictions on the test set
y_pred = model.predict(X_test)

# 7. Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")


# Save the trained model
model_path = get_data_path("iris_model.pkl")
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
