def test_settings_fixture__where_settings_are_not_configured(pytester):
    pytester.makepyfile(
        """
        def test_sample(settings):
            assert settings.FOO == "bar"
    """
    )

    result = pytester.runpytest()

    result.stdout.fnmatch_lines(
        [
            "*::test_sample FAILED*",
        ]
    )

    assert result.ret == 1
