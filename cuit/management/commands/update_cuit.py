#coding=UTF-8
from django.core.management.base import BaseCommand, CommandError

from cuit.utils import update_cuit

class Command(BaseCommand):
    args = '<file>'
    help = u'Updates the AFIP Inscriptions database.'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('You must supply one file')

        try:
            f = open(args[0])
        except IOError:
            raise CommandError('There was a problem opening the file')

        self.stdout.write('Updating AFIP Inscriptions from %s ...\n' % args[0])

        update_cuit(f)

        self.stdout.write(u'The inscriptions where successfully updated\n')

