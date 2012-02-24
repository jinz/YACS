from optparse import make_option

from django.core.management.base import BaseCommand
from django.db import transaction

from courses.models import Semester
from scheduler import models


class Command(BaseCommand):
    help = "Caches all the section conflicts into the database."
    option_list = BaseCommand.option_list + (
        make_option('--all', '-a', dest='all', action='store_true',
            help='Force update of all semesters instead of just the latest one.'),
        make_option('--sql', '-s', dest='sql', action='store_true',
            help='Use manual SQL Insertion instead of Django objects to insert conflicts.'),
    )

    def handle(self, *args, **options):
        with transaction.commit_on_success():
            semesters = Semester.objects.all()
            if not options.get('all'):
                semesters = semesters[:1]
            s = options.get('sql')
            for semester in semesters:
                print "Computing conflicts for %d-%d..." % (semester.year, semester.month)
                models.cache_conflicts(semester=semester, sql=s)


