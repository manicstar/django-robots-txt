from django.views.generic import TemplateView


class TextView(TemplateView):
    """
    Mimetype text/plain
    """
    def render_to_response(self, context, **kwargs):
        return super(TextView, self).render_to_response(
            context,
            content_type='text/plain',
            **kwargs
        )

