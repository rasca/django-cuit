django-cuit
===========

This app verificates a CUIT (Código Único de Identificación Tributaria) against
a `released database`_ by the AFIP (Administración General de Ingresos
Públicos) with all the current CUITs. It also gives you some more information
related to the CUIT:

- Denominacion
- Imp. Ganancias
- Imp IVA
- Monotributo
- Integrante Soc
- Empleador
- Actividad Monotributo

How it works
------------

For this app, you need to upload the latest AFIP `released database`_. It's a
simple text zipped text file that get's parsed and loaded into the database.
You can achieve this by using the admin UI or running a management command.

You can interact with this app by listening to the signal `cuit_updated` or by
using the ARCUITField.

ARCUITField
-----------

This field works exactly like `django.contrib.` but instead of checking the
CUIT against a regex, it also checks it againt the AFIP data.

`cuit_updated` signal
---------------------

To be written

Updating the database
---------------------


To be written

TODO
----

- Automatically unzzip the downloaded database in memory
- Allow updating the database with the *no denomination* database
- Complete the *monotributo* activities

.. _released database: http://www.afip.gob.ar/genericos/cInscripcion/archivoCompleto.asp
