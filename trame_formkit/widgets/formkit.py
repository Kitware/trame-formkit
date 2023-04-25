"""Formkit Widgets only support vue3.
"""
from trame_client.widgets.core import AbstractElement, Template
from .. import module

__all__ = [
    "FormKit",
    "FormKitSchema",
]

# FormKit section keys
slot_names = [
    "outer",  # The outermost wrapping element.
    "wrapper",  # A wrapper around the label and input.
    "label",  # The label of the input.
    "prefix",  # Has no output by default, but allows content directly before an input element.
    "prefixIcon",  # An element for outputting an icon before the prefix section.
    "inner",  # A wrapper around the actual input element.
    "suffix",  # Has no output by default, but allows content directly after an input element.
    "suffixIcon",  # An element for outputting an icon after the suffix section.
    "input",  # The input element itself.
    "help",  # The element containing help text.
    "messages",  # A wrapper around all the messages.
    "message",  # The element (or many elements) containing a message — most often validation and error messages.
]
Template.slot_names.update(slot_names)


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


class FormKit(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__(
            "FormKit",
            **kwargs,
        )
        self._attr_names += [
            "config",
            "delay",
            "errors",
            "help",
            "id",
            "ignore",
            "index",
            "label",
            "name",
            "parent",
            ("prefix_icon", "prefix-icon"),
            "preserve",
            ("preserve_errors", "preserve-errors"),
            ("sections_schema", "sections-schema"),
            ("suffix_icon", "suffix-icon"),
            "type",
            "validation",
            ("validation_visibility", "validation-visibility"),
            ("validation_label", "validation-label"),
            ("validation_rules", "validation-rules"),
            "value",
            #
            "placeholder",
            "options",
        ]
        self._event_names += [
            "input",
            ("input_raw", "input-raw"),
            "node",
            #
            "submit",
        ]


class FormKitSchema(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__(
            "FormKitSchema",
            **kwargs,
        )
        self._attr_names += [
            "schema",
            "library",
            "data",
        ]
