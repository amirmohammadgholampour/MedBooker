from django.db import models 
from config.settings import AUTH_USER_MODEL 

class DoctorExpertise(models.TextChoices):
    CARDIOLOGIST = 'cardiologist', 'Cardiologist'
    NEUROLOGIST = 'neurologist', 'Neurologist'
    DERMATOLOGIST = 'dermatologist', 'Dermatologist'
    ONCOLOGIST = 'oncologist', 'Oncologist'
    PEDIATRICIAN = 'pediatrician', 'Pediatrician'
    PSYCHIATRIST = 'psychiatrist', 'Psychiatrist'
    ORTHOPEDIC_SURGEON = 'orthopedic_surgeon', 'Orthopedic Surgeon'
    GYNECOLOGIST = 'gynecologist', 'Gynecologist'
    ENDOCRINOLOGIST = 'endocrinologist', 'Endocrinologist'
    OPHTHALMOLOGIST = 'ophthalmologist', 'Ophthalmologist'


class CityChoices(models.TextChoices):
    TEHRAN = 'tehran', 'Tehran'
    MASHHAD = 'mashhad', 'Mashhad'
    ISFAHAN = 'isfahan', 'Isfahan'
    SHIRAZ = 'shiraz', 'Shiraz'
    TABRIZ = 'tabriz', 'Tabriz'
    AHVAZ = 'ahvaz', 'Ahvaz'
    KARAJ = 'karaj', 'Karaj'
    QOM = 'qom', 'Qom'
    KERMANSHAH = 'kermanshah', 'Kermanshah'
    RASHT = 'rasht', 'Rasht'
    URMIA = 'urmia', 'Urmia'
    ZAHEDAN = 'zahedan', 'Zahedan'
    ARAK = 'arak', 'Arak'
    YAZD = 'yazd', 'Yazd'
    ZANJAN = 'zanjan', 'Zanjan'
    SARI = 'sari', 'Sari'
    HAMEDAN = 'hamedan', 'Hamedan'
    SANANDAJ = 'sanandaj', 'Sanandaj'
    BANDAR_ABBAS = 'bandar_abbas', 'Bandar Abbas'
    GORGAN = 'gorgan', 'Gorgan'


class Doctor(models.Model):
    doctor_user = models.OneToOneField(AUTH_USER_MODEL, related_name="doctor_profile", limit_choices_to={"user_type":"doctor"}, on_delete=models.CASCADE) 
    expertise = models.CharField(max_length=255, choices=DoctorExpertise.choices, verbose_name="Doctor expertise") 
    city = models.CharField(max_length=255, choices=CityChoices.choices, verbose_name="City", default=CityChoices.TEHRAN) 
    office_address = models.TextField(verbose_name="Office address")
    bio = models.TextField(verbose_name="Biography", blank=True, null=True)
    medical_code = models.CharField(max_length=20, unique=True, verbose_name="Medical System Code")
    office_phone = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_media = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f"Dr. {self.doctor_user.first_name} {self.doctor_user.last_name} ({self.expertise})"