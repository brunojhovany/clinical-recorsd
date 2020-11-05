from .entities import Clinic

class ClinicData(object):
    @classmethod
    def find_by_id(cls, id: int) -> Clinic:
        return Clinic.find_by_id(clinic_id=id)
