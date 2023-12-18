from sqlite3 import connect

from django.core.management.base import BaseCommand
from pandas import DataFrame, read_csv

from nasa_exoplanet_query.settings import DATABASES
from planets.models import Facility, Hostname, Method, Planet


class Command(BaseCommand):
	help = "Imports exoplanets data from CSV file"

	def add_arguments(self, parser):
		parser.add_argument("filepath", help="File path")
		parser.add_argument("skiprows", type=int, help="Line numbers to skip (0-indexed) or number of lines to skip at the start of the file.")
		parser.add_argument("usecols", nargs="+", help="Subset of columns to select")

	def handle(self, *args, **options):
		planets_df = read_csv(options["filepath"], usecols=options["usecols"], skiprows=options["skiprows"])
		planets_df = planets_df.rename(columns={'disc_year': 'year_of_discovery', 'discoverymethod': 'discovery_method_id', 'disc_facility': 'discovery_facility_id', 'hostname': 'hostname_id'})

		with connect(DATABASES["default"]["NAME"]) as conn:
			DataFrame(planets_df.rename(columns={"discovery_method_id": "name"}).name.drop_duplicates().reset_index(drop=True)).to_sql(Method._meta.db_table, conn, if_exists='replace', index_label='id')
			DataFrame(planets_df.rename(columns={"hostname_id": "name"}).name.drop_duplicates().reset_index(drop=True)).to_sql(Hostname._meta.db_table, conn, if_exists='replace', index_label='id')
			DataFrame(planets_df.rename(columns={"discovery_facility_id": "name"}).name.drop_duplicates().reset_index(drop=True)).to_sql(Facility._meta.db_table, conn, if_exists='replace', index_label='id')

			planets_df = planets_df.replace({**{facility.name: facility.name for facility in Facility.objects.all()}, **{hostname.name: hostname.name for hostname in Hostname.objects.all()}, **{method.name: method.name for method in Method.objects.all()}})
			planets_df.to_sql(Planet._meta.db_table, conn, if_exists='replace', index_label='id')
			conn.commit()