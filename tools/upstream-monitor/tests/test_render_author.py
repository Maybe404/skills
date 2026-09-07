from upstream_monitor.render import extract_copyright_author

MIT_LOWERCASE = """MIT License

Copyright (c) 2026 aizixun

Permission is hereby granted, free of charge, to any person obtaining a copy
"""


def test_lowercase_author_does_not_swallow_license_body():
    assert extract_copyright_author(MIT_LOWERCASE) == "aizixun"


def test_author_with_year_range_and_uppercase_present():
    text = "Copyright (c) 2025-PRESENT Hairyf <https://github.com/hairyf>\n"
    assert extract_copyright_author(text) == "Hairyf <https://github.com/hairyf>"


def test_year_only_line_yields_none():
    assert extract_copyright_author("Copyright (c) 2026\n\nPermission is hereby granted\n") is None
