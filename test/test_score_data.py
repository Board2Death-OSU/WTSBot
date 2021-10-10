import context
import pytest

from utl.prkeeper import _get_country_acronyms, _get_country_names, _check_score_data

SAMPLE_DATA = [
    {"country_name": "Russia", "country_acronym": "RU"},
    {"country_name": "United Kingdom", "country_acronym": "UK"},
    {"country_name": "United States", "country_acronym": "US"}
]

#####################################################################
# Test _get_country_names
#####################################################################


def test_get_country_names_normal():
    """Test get_country_names for the normal use case
    """
    expected = ["Russia", "United Kingdom", "United States"]

    result = _get_country_names(SAMPLE_DATA)

    assert result == expected


def test_get_country_names_missing_field():
    """Test get_country_names when the name field is missing for an element
    """
    expected = ["United Kingdom", "United States"]
    data = [
        {"country_acronym": "RU"},
        {"country_name": "United Kingdom", "country_acronym": "UK"},
        {"country_name": "United States", "country_acronym": "US"}
    ]

    result = _get_country_names(data)

    assert result == expected


def test_get_country_names_only_names():
    """Test get_country_names with only the name field
    """
    expected = ["Russia", "United Kingdom", "United States"]
    data = [
        {"country_name": "Russia"},
        {"country_name": "United Kingdom"},
        {"country_name": "United States"}
    ]

    result = _get_country_names(data)

    assert result == expected


def test_get_country_names_none():
    """Test get_country_names with no valid entry
    """
    expected = []
    data = [
        {"country_acronym": "RU"},
        {"country_acronym": "UK"},
        {"country_acronym": "US"}
    ]

    result = _get_country_names(data)

    assert result == expected

#####################################################################
# Test _get_country_acronyms
#####################################################################


def test_get_country_acronyms_normal():
    """Test get_country_acroymys for the normal use case
    """
    expected = ["RU", "UK", "US"]

    result = _get_country_acronyms(SAMPLE_DATA)

    assert result == expected


def test_get_country_acronyms_missing_field():
    """Test get_country_acronyms when the name field is missing for an element
    """
    expected = ["UK", "US"]
    data = [
        {"country_name": "Russia"},
        {"country_name": "United Kingdom", "country_acronym": "UK"},
        {"country_name": "United States", "country_acronym": "US"}
    ]

    result = _get_country_acronyms(data)

    assert result == expected


def test_get_country_acronyms_only_acronyms():
    """Test get_country_acronyms with only the name field
    """
    expected = ["RU", "UK", "US"]
    data = [
        {"country_acronym": "RU"},
        {"country_acronym": "UK"},
        {"country_acronym": "US"}
    ]

    result = _get_country_acronyms(data)

    assert result == expected


def test_get_country_acronyms_none():
    """Test get_country_acronyms with no valid entry
    """
    expected = []
    data = [
        {"country_name": "Russia"},
        {"country_name": "United Kingdom"},
        {"country_name": "United States"}
    ]

    result = _get_country_acronyms(data)

    assert result == expected

#####################################################################
# Test _get_score_data
#####################################################################


def test_check_score_data_normal():
    """test check_score_data under normal conditions
    """
    names = ["Russia", "United Kingdom", "United States"]
    acronyms = ["RU", "UK", "US"]

    result = _check_score_data(names, acronyms)

    assert result


def test_check_score_data_length_mismatch():
    """test check_score_data with non matching lengths
    """
    names = ["Russia", "United Kingdom", "United States"]
    acronyms = ["UK", "US"]

    with pytest.raises(ValueError):
        result = _check_score_data(names, acronyms)
        assert not result


def test_check_score_data_letter_mismatch():
    """test check_score_data with a non matching letter
    """
    names = ["Russia", "United Kingdom", "United States"]
    acronyms = ["EU", "UK", "US"]

    with pytest.raises(ValueError):
        result = _check_score_data(names, acronyms)
        assert not result


def test_check_score_data_out_of_order():
    """test check_score_data with an acronym out of order
    """
    names = ["Russia", "United Kingdom", "United States"]
    acronyms = ["UK", "RU", "US"]

    with pytest.raises(ValueError):
        result = _check_score_data(names, acronyms)
        assert not result
