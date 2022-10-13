from django.db import models
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.fields import StreamField

class HomePage(Page):
    subtitle_text = models.CharField(
        max_length = 50,
        blank = True,
        help_text = "Homepage subtitle"
    )

    background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name="+",
        help_text="Background image",
        on_delete = models.SET_NULL
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle_text"),
        FieldPanel("background_image"),
    ]
