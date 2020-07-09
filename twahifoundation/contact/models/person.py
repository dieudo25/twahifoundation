from django.db import models


class Company(models.Model):
    """
    Company model definition
    """

    name = models.CharField(
        max_length=60, verbose_name="Nom", default=None)
    adresse = models.CharField(
        max_length=60, verbose_name="Adresse", default=None)
    email = models.EmailField(max_length=254, default=None)
    phone_number = models.CharField(
        max_length=60, verbose_name="Téléphone", null=None)
    site_web = models.URLField(max_length=200, blank=True)
    is_partner = models.BooleanField(
        default=False, verbose_name="Est un partenaire")

    class Meta:
        """
        Meta definition for Company.
        """

        verbose_name = 'Entreprise'
        verbose_name_plural = 'Entreprises'

    def __str__(self):
        """
        Unicode representation of Entreprise.
        """

        return f"{self.name}"


class Person(models.Model):
    """
    Person model definition
    """
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(
        max_length=60, verbose_name="Prénom", default=None)
    last_name = models.CharField(
        max_length=60, verbose_name="Nom", default=None)
    email = models.EmailField(max_length=254, default=None)
    phone_number = models.CharField(
        max_length=60, verbose_name="Téléphone", null=None)
    is_supplier = models.BooleanField(
        default=False, verbose_name="Est un fournisseur")
    is_donor = models.BooleanField(
        default=False, verbose_name="Est un donateur")
    is_follower = models.BooleanField(
        default=False, verbose_name="Est inscrit à la newsletter")

    class Meta:
        """
        Meta definition for Person.
        """

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """
        Unicode representation of Donor.
        """

        return f"{self.last_name} {self.first_name}"
