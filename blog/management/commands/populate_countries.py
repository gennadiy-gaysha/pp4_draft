import os
from django.core.management.base import BaseCommand
from blog.models import Country  # Replace 'myapp' with the name of your app

class Command(BaseCommand):
    help = 'Populate the list of countries from a text file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'countries.txt')

        with open(file_path, 'r') as file:
            for line in file:
                columns = line.split('\t')
                if len(columns) >= 18:  # Update this to the correct number of fields in your text file
                    (
                        iso, iso3, iso_numeric, fips, country, capital, area_sq_km, population,
                        continent, tld, currency_code, currency_name, phone, postal_code_format,
                        postal_code_regex, languages, geonameid, neighbours, *_
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
                        phone=phone.strip()[:100],
                        postal_code_format=postal_code_format.strip()[:100],
                        postal_code_regex=postal_code_regex.strip()[:100],
                        languages=languages.strip(),
                        geonameid=geonameid.strip() if geonameid.strip() else 0,
                        neighbours=neighbours.strip(),
                    )

            self.stdout.write(self.style.SUCCESS('Successfully populated countries data'))
