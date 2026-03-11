from apps.doctors.models import Doctor


def get_all_doctors():
    return Doctor.objects.all()


def get_doctor_by_id(doctor_id):
    return Doctor.objects.filter(id=doctor_id).first()


def get_available_doctors():
    return Doctor.objects.filter(is_available=True)