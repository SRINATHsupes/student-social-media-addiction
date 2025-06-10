{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0b55fbbb-c13b-482b-8926-ebdfb45e7b63",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f051bac1-d79d-4771-a197-ee268825443d",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = joblib.load(\"addiction_model.pkl\")\n",
    "encoders = joblib.load(\"label_encoders.pkl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b86a279a-a558-45b9-a135-c2e0e32ee180",
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict_addiction(input_data):\n",
    "    \n",
    "\n",
    "    try:\n",
    "        \n",
    "        encoded_features = []\n",
    "        for field in ['Gender', 'Academic_Level', 'Country', 'Most_Used_Platform', \n",
    "                      'Affects_Academic_Performance', 'Relationship_Status']:\n",
    "            val = input_data[field]\n",
    "            le = encoders[field]\n",
    "            encoded_val = le.transform([val])[0]\n",
    "            encoded_features.append(encoded_val)\n",
    "\n",
    "    \n",
    "        encoded_features.extend([\n",
    "            input_data[\"Age\"],\n",
    "            input_data[\"Avg_Daily_Usage_Hours\"],\n",
    "            input_data[\"Sleep_Hours_Per_Night\"],\n",
    "            input_data[\"Mental_Health_Score\"],\n",
    "            input_data[\"Conflicts_Over_Social_Media\"]\n",
    "        ])\n",
    "        input_array = np.array(encoded_features).reshape(1, -1)\n",
    "        prediction = model.predict(input_array)[0]\n",
    "\n",
    "        return \"Addicted\" if prediction == 1 else \"Not Addicted\"\n",
    "    \n",
    "    except Exception as e:\n",
    "        return f\"Error in prediction: {e}\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "29dd7c06-5124-4929-9f0c-f2fa20ee3471",
   "metadata": {},
   "outputs": [],
   "source": [
    "student_input = {\n",
    "    \"Gender\": \"Female\",\n",
    "    \"Academic_Level\": \"Undergraduate\",\n",
    "    \"Country\": \"USA\",\n",
    "    \"Most_Used_Platform\": \"Instagram\",\n",
    "    \"Affects_Academic_Performance\": \"Yes\",\n",
    "    \"Relationship_Status\": \"Single\",\n",
    "    \"Age\": 20,\n",
    "    \"Avg_Daily_Usage_Hours\": 6.0,\n",
    "    \"Sleep_Hours_Per_Night\": 5.0,\n",
    "    \"Mental_Health_Score\": 6,\n",
    "    \"Conflicts_Over_Social_Media\": 4\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "abde4c8b-91b7-4eb3-9756-6cc679f722c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addicted\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "F:\\anaconda\\Lib\\site-packages\\sklearn\\base.py:493: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "print(predict_addiction(student_input))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be739ed4-8b71-43da-9fb0-07c740a1abdc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
