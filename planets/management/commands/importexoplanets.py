from sqlite3 import connect

from django.core.management.base import BaseCommand
from pandas import read_csv

from nasa_exoplanet_query.settings import DATABASES
from planets.models import Planet


class Command(BaseCommand):
	help = "Imports exoplanets data from CSV file"

	def add_arguments(self, parser):
		parser.add_argument("filepath", help="File path")
		parser.add_argument("skiprows", type=int, help="Line numbers to skip (0-indexed) or number of lines to skip at the start of the file.")
		parser.add_argument("usecols", nargs="+", help="Subset of columns to select")

	def handle(self, *args, **options):
		planets_df = read_csv(options["filepath"], usecols=options["usecols"], skiprows=options["skiprows"])
		planets_df = planets_df.rename(columns={'disc_year': 'year_of_discovery', 'discoverymethod': 'discovery_method', 'disc_facility': 'discovery_facility'})

		with connect(DATABASES["default"]["NAME"]) as conn:
			planets_df.to_sql(Planet._meta.db_table, conn, if_exists='replace', index_label='id')
			conn.commit()