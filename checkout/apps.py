from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    """
    Override ready method to import signals and
    Call update total model each time  line item is deleted or saved
    """

    def ready(self):
        import checkout.signals
