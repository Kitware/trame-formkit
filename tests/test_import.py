def test_import():
    from trame_formkit.widgets.formkit import FormKit, FormKitSchema  # noqa: F401

    # For components only, the FormKit is also importable via trame
    from trame.widgets.formkit import FormKit, FormKitSchema  # noqa: F401,F811
