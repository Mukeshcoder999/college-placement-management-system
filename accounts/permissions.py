from rest_framework.permissions import BasePermission


#students permission to login or not checks wheather is student or not
class IsStudent(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated and
            request.user.role == 'student'
        )

#company permission to login or not checks wheather is company or not
class IsCompany(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated and
            request.user.role == 'company'
        )

#placementofficer to login or not checks wheather is placement_officer or not
class IsPlacementOfficer(BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated and
            request.user.role == 'placement_officer'
        )
#object level permission
class IsJobOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.company.user == request.user   

class IsApplicationAccessible(BasePermission):

    def has_object_permission(self, request, view, obj):

        user = request.user

        if user.role == "student":
            return obj.student.user == user

        elif user.role == "company":
            return obj.job.company.user == user

        elif user.role == "placement_officer":
            return True

        return False

#students cannot update their appliction after submitting only comapny and placementofficer can update
class CanUpdateApplication(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return request.user.role in [
            "company",
            "placement_officer"
        ]