#coding=UTF-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

REFS = {
    'NI': _(u'No Inscripto'),
    'N': _(u'No Inscripto'),
    'AC': _(u'Activo'),
    'S': _(u'Activo'),
    'EX': _(u'Exento'),
    'NA': _(u'No alcanzado'),
    'XN': _(u'Exento no alcanzado'),
    'AN': _(u'Activo no alcanzado'),
    'NC': _(u'No corresponde'),

}
class Inscription(models.Model):
    """
    Stores the "Constancia de Inscripción" from the AFIP
    
    It also stores related data
    """
    IMP_GANANCIAS_CHOICES = (
        ('NI', REFS['NI']),
        ('AC', REFS['AC']),
        ('EX', REFS['EX']),
        ('NC', REFS['NC']),
    )

    IMP_IVA_CHOICES = (
        ('NI', REFS['NI']),
        ('AC', REFS['AC']),
        ('EX', REFS['EX']),
        ('NA', REFS['NA']),
        ('XN', REFS['XN']),
        ('AN', REFS['AN']),
    )

    ACTIVO_CHOICES = (
        ('S', REFS['S']),
        ('N', REFS['N']),
    )

    cuit = models.CharField(_(u'CUIT'), max_length=13, unique=True)
    denominacion = models.CharField(_(u'Denominación'), max_length=30)
    imp_ganancias = models.CharField(_(u'Impuesto Ganancias'), max_length='2',
                                   choices=IMP_GANANCIAS_CHOICES)
    imp_iva = models.CharField(_(u'Impuesto IVA'), max_length=2,
                               choices=IMP_IVA_CHOICES)
    monotributo = models.CharField(_(u'Monotributo'), max_length=2, help_text=
                       u'Código de categoría tributaria o NI (No inscripto)')
    integrante_soc = models.CharField(_(u'Integrante de una sociedad'),
                                      max_length=1, choices=ACTIVO_CHOICES)
    empleador = models.CharField(_(u'Empelador'), max_length=1,
                                 choices=ACTIVO_CHOICES)
    actividad_monotributo = models.DecimalField(_(u'Actividad monotributo'),
                                                max_digits=2, decimal_places=0)

    class Meta:
        verbose_name = _(u'Inscription')
        verbose_name_plural = _(u'Inscriptions')

    def __unicode__(self):
        return '%s %s' % (self.cuit, self.denominacion)
