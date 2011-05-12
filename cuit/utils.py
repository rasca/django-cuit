from cuit.models import Inscription
def update_cuit(file):

    # Deactivate ALL Inscriptions
    Inscription.objects.update(active=False)

    for line in file:
        cuit = u'%s-%s-%s' % (line[:2], line[2:10], line[10])
        try:
            inscription = Inscription.objects.get(cuit=cuit)
        except Inscription.DoesNotExist:
            inscription = Inscription(cuit=cuit)

        inscription.denominacion = line[11:40]
        inscription.imp_ganancias = line[41:43]
        inscription.imp_iva = line[43:45]
        inscription.monotributo = line[45:47]
        inscription.integrante_soc = line[47]
        inscription.empleador = line[48]
        inscription.actividad_monotributo = line[49:52]
        inscription.active = True
        inscription.save()
