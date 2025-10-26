import pyconify
from markupsafe import Markup


def render_icon(icon_key, **kwargs):
    try:
        svg_bytes = pyconify.svg(icon_key, **kwargs)

        if not svg_bytes:
            raise ValueError(f"Icon '{icon_key}' not found or returned empty.")

        svg_string = svg_bytes.decode('utf-8')

        return Markup(svg_string)

    except Exception as e:
        print(f"Error rendering icon '{icon_key}': {e}")
        return Markup(f"<!-- Icon '{icon_key}' failed to load -->")
