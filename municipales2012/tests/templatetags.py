# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core import mail
from django.core.urlresolvers import reverse
from municipales2012.models import Comuna, Area, Indice, Dato, Candidato, Pregunta, Respuesta, Contacto, Colectivo, preguntas_por_partido
from municipales2012.management.commands.comunas_importer import *
from municipales2012.management.commands.contactos_importer import *
from municipales2012.management.commands.candidatos_importer import *
from mailer.models import Message
from django.test.client import Client
from django.utils.unittest import skip
from django.template import Template, Context
from urllib2 import quote


class TemplateTagsTesting(TestCase):
	def setUp(self):
		area = Area.objects.create(nombre=u"Caracterización", clase_en_carrusel=u"fondoCeleste")
		pobreza = Dato.objects.create(nombre=u"Pobreza", imagen="chanchito.png")
		comuna = Comuna.objects.create(nombre=u"La comuna", 
										slug=u"la-comuna",
										main_embedded=u"http://www.candideit.org/lfalvarez/rayo-x-politico/embeded",
										)
		self.indice = Indice.objects.create(
			comuna =comuna,
			area = area,
			dato = pobreza,
			encabezado = u"encabezado",
			numero_1 = u"7%",
			texto_1 = u"de los habitantes de la comuna son pobres",
			numero_2 = u"n2",
			texto_2 = u"t2",
			texto_pie_pagina_1 = u"En el Ranking nacional de pobreza, la comuna está en el lugar",
			numero_pie_pagina_1 = u"1",
			texto_pie_pagina_2 = u"tpp2",
			numero_pie_pagina_2 = u"2",
			texto_pie_pagina_3 = u"tpp3",
			numero_pie_pagina_3 = u"3",
			en_carrusel = True
			)


	# def test_create_link_for_updating_election_data(self):
 #        template = Template('{% load twitter_tags %}{% twitt_indice indice %}')
        
        
 #        context = Context({"indice": self.indice })
 #        election_update_url = reverse('election_update',kwargs={'slug':self.election.slug})
 #        expected_twitt = u''
        
 #        self.assertEqual(template.render(context), expected_html) 