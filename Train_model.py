import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("Food_Adulteration.csv")

# Drop rows with missing 'action_taken'
df = df.dropna(subset=['action_taken'])

# Drop rows with any missing inputs
df = df.dropna()

# Select features and target
features = ['product_name', 'brand', 'category', 'adulterant', 'detection_method', 'severity', 'health_risk']
X = df[features]
y = df['action_taken']

# Encode features
encoders = {}
for col in features:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

# Encode target
target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

# Save encoders
joblib.dump(encoders, "encoders.pkl")
joblib.dump(target_encoder, "target_encoder.pkl")

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model training completed.")
