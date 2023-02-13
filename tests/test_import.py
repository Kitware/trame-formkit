def test_import():
    from trame_formkit.widgets.trame_formkit import CustomWidget  # noqa: F401

    # For components only, the CustomWidget is also importable via trame
    from trame.widgets.trame_formkit import CustomWidget  # noqa: F401,F811
