from pathlib import Path

serve_path = str(Path(__file__).with_name("serve").resolve())
serve = {"__trame_formkit": serve_path}
scripts = ["__trame_formkit/formkit.js"]
vue_use = [
    (
        "FormKitVue.plugin",
        dict(js_eval="FormKitVue.defaultConfig({ theme: 'genesis' })"),
    )
]
