# You are given a test_input_text function that takes two values: expected_result is the expected result,
# and actual_result is the actual result. Note that you don't need to use input!
#
# The function must check for a match using an assert statement and, if not, provide a comprehensive error message.
#
# Important! The format of the error must exactly match the one given in the example in order for it to be counted
# by the checking system!


def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, f"expected {expected_result}, got {actual_result}"


