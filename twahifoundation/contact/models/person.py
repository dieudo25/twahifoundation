from django.db import models


class Person(models.Model):
    """
    AbstractPerson model definition
    """

    first_name = models.CharField(
        max_length=60, verbose_name="Prénom", default=None)
    last_name = models.CharField(
        max_length=60, verbose_name="Nom", default=None)
    email = models.EmailField(max_length=254, default=None)
    phone_number = models.CharField(
        max_length=60, verbose_name="Téléphone", null=None)
    company = models.CharField(max_length=60, verbose_name="Entreprise")

    class Meta:
        """
        Meta definition for Supplier.
        """

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """
        Unicode representation of Donor.
        """

        return f"{self.last_name} {self.first_name}"
