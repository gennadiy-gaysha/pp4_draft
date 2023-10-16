from django.db import models

class Country(models.Model):
    iso = models.CharField(max_length=5, default='')
    iso3 = models.CharField(max_length=5, default='')
    iso_numeric = models.CharField(max_length=5, default='')
    fips = models.CharField(max_length=5, default='')
    country_name = models.CharField(max_length=100, default='')
    capital = models.CharField(max_length=100, default='')
    area_sq_km = models.FloatField(default=0.0)
    population = models.IntegerField(default=0)
    continent = models.CharField(max_length=5, default='')
    tld = models.CharField(max_length=5, blank=True, default='')
    currency_code = models.CharField(max_length=5, default='')
    currency_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=10, default='')
    postal_code_format = models.CharField(max_length=100, default='')
    postal_code_regex = models.CharField(max_length=100, default='')
    languages = models.CharField(max_length=100, default='')
    geonameid = models.IntegerField(default=0)
    neighbours = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.country_name

    # the very first suggestion:
    import os
    from django.core.management.base import BaseCommand
    from myapp.models import Country  # Replace 'myapp' with the name of your app

    class Command(BaseCommand):
        help = 'Populate the list of countries from a text file'

        def handle(self, *args, **kwargs):
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'countries.txt')

            with open(file_path, 'r') as file:
                for line in file:
                    columns = line.split('\t')
                    if len(columns) >= 5:
                        iso, _, _, _, country, *_ = columns
                        Country.objects.get_or_create(country_name=country.strip())

            self.stdout.write(self.style.SUCCESS('Successfully populated countries data'))

    # ===============================================================
    import os
    from django.core.management.base import BaseCommand
    from myapp.models import Country  # Replace 'myapp' with the name of your app

    class Command(BaseCommand):
        help = 'Populate the list of countries from a text file'

        def handle(self, *args, **kwargs):
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'countries.txt')

            with open(file_path, 'r') as file:
                for line in file:
                    columns = line.split('\t')
                    if len(columns) >= 12:  # Update this to the correct number of fields in your text file
                        (
                            iso, iso3, iso_numeric, fips, country, capital, area_sq_km, population,
                            continent, tld, currency_code, currency_name, *_
                        ) = columns
                        country_obj, created = Country.objects.get_or_create(
                            iso=iso.strip(),
                            iso3=iso3.strip(),
                            iso_numeric=iso_numeric.strip(),
                            fips=fips.strip(),
                            country_name=country.strip(),
                            capital=capital.strip(),
                            area_sq_km=float(area_sq_km.strip()) if area_sq_km.strip() else 0.0,
                            population=int(population.strip()) if population.strip() else 0,
                            continent=continent.strip(),
                            tld=tld.strip() if tld.strip() else '',
                            currency_code=currency_code.strip(),
                            currency_name=currency_name.strip(),
                        )

                self.stdout.write(self.style.SUCCESS('Successfully populated countries data'))

