from enum import Enum, unique

from django.apps import AppConfig
from django.db import models
from django.utils.translation import ugettext_lazy as _


class InitiativesConfig(AppConfig):
    name = 'initiatives'


@unique
class Fields(Enum):
    ENERGY = 1
    MARITIME_FISHERIES = 2
    HEALTH = 3
    DEFENSE = 4
    ENVIRONMENT = 5
    SOCIAL = 6
    EDUCATION = 7
    TECHNOLOGY = 8
    CULTURE_AND_LANGUAGE = 9
    ECONOMY = 10
    AGRICULTURE = 11
    ARCHITECTURE_AND_URBAN_PLANNING = 12


class Initiative(models.Model):
    # Overview
    name = models.CharField(_('Initiative name'), max_length=255)
    description = models.TextField(_('Description'))

    predicted_beneficiary_count = models.IntegerField(_('Predicted beneficiary count'),
                                                      null=True, blank=True)
    location = models.TextField(_('Location'))
    target = models.CharField(_('Target'), max_length=255,
                              help_text='Institution / Organization / Government / Specific society group')
    start = models.DateField(_('Start date'))
    end = models.DateField(_('End date'))

    contact_person_name = models.CharField(_('Contact person name'), max_length=255)
    contact_person_number = models.CharField(_('Contact person mobile number'), max_length=255)

    field = models.SmallIntegerField(
        _("Initiative type"),
        choices=(
            (Fields.ENERGY.value, _('Energy')),
            (Fields.MARITIME_FISHERIES.value, _('Maritime and Fisheries')),
            (Fields.HEALTH.value, _('Health')),
            (Fields.DEFENSE.value, _('Defense')),
            (Fields.ENVIRONMENT.value, _('Environment')),
            (Fields.SOCIAL.value, _('Social')),
            (Fields.EDUCATION.value, _('Education')),
            (Fields.TECHNOLOGY.value, _('Technology')),
            (Fields.CULTURE_AND_LANGUAGE.value, _('Culture and language')),
            (Fields.ECONOMY.value, _('Economy')),
            (Fields.AGRICULTURE.value, _('Agriculture')),
            (Fields.ARCHITECTURE_AND_URBAN_PLANNING.value, _('Architecture and urban planning')),
        )
    )

    # Initiative details

    # Meta
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
