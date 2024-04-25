
from taipy.gui import Page, Row, Col, Input, TextArea, Button

class PatientInfo(Page):
  def build(self):
    return Row(
      children=[
        Col(
          children=[
            "Patient Name:",
            Input(id="name", placeholder="Enter patient name"),
            "Patient ID:",
            Input(id="patient_id", placeholder="Enter patient ID"),
            "Age:",
            Input(id="age", placeholder="Enter patient age", type="number"),
            "Clinical Status:",
            TextArea(id="clinical_status", placeholder="Describe patient's condition"),
          ]
        ),
        Col(
          children=[
            "Treatment:",
            TextArea(id="treatment", placeholder="Describe planned treatment"),
            Button(text="Save Information", click_handler=self.save_data),
          ]
        ),
      ]
    )

  def save_data(self):
    # Simulate data saving (replace with logic to connect to a database)
    name = self.get_value("name")
    patient_id = self.get_value("patient_id")
    age = self.get_value("age")
    clinical_status = self.get_value("clinical_status")
    treatment = self.get_value("treatment")
    print(f"Patient Information Saved!")
    print(f"Name: {name}")
    print(f"ID: {patient_id}")
    print(f"Age: {age}")
    print(f"Clinical Status: {clinical_status}")
    print(f"Treatment: {treatment}")

# Run the application
app = PatientInfo()
app.run()
