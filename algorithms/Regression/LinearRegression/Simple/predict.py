import pandas as pd
import joblib
from config import LINEAR_REGRESSION_DIR

MODEL_PATH = LINEAR_REGRESSION_DIR / "model.pkl"

model = joblib.load(MODEL_PATH)

experience = float(
    input("Enter Years of Experience: ")
)

sample = pd.DataFrame(
    {
        "YearsExperience": [experience]
    }
)

prediction = model.predict(sample)

salary = float(prediction[0][0])

print(
    f"Predicted Salary: ₹{salary:,.2f}"
)