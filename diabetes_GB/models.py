from django.db import models

class DiabetesInput(models.Model):
    glucose=models.FloatField()
    blood_pressure=models.FloatField()
    bmi=models.FloatField()
    insulin=models.FloatField()
    skinthickness=models.FloatField()
    pregnancies=models.FloatField()
    Age=models.FloatField()
    DiabetesPedigree=models.FloatField()
    Prediction=models.CharField(max_length=20)



    def __str__(self):
        return str(self.glucose)+","+str(self.blood_pressure)+","+str(self.bmi)+","+str(self.insulin)+","+str(self.skinthickness)+","+str(self.pregnancies)+","+str(self.Age)+","+str(self.DiabetesPedigree)+","+str(self.Prediction)
