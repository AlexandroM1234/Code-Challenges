from re import search
# You need to write regex that will validate a password to make sure it meets the following criteria:

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.
regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"

# tests cases that i couldnt figure out how to use
# Test.describe("Basic tests")
# Test.assert_equals(bool(search(regex, 'fjd3IR9')), True)
# Test.assert_equals(bool(search(regex, 'ghdfj32')), False)
# Test.assert_equals(bool(search(regex, 'DSJKHD23')), False)
# Test.assert_equals(bool(search(regex, 'dsF43')), False)
# Test.assert_equals(bool(search(regex, '4fdg5Fj3')), True)
# Test.assert_equals(bool(search(regex, 'DHSJdhjsU')), False)
# Test.assert_equals(bool(search(regex, 'fjd3IR9.;')), False)
# Test.assert_equals(bool(search(regex, 'fjd3  IR9')), False)
# Test.assert_equals(bool(search(regex, 'djI38D55')), True)
# Test.assert_equals(bool(search(regex, 'a2.d412')), False)
# Test.assert_equals(bool(search(regex, 'JHD5FJ53')), False)
# Test.assert_equals(bool(search(regex, '!fdjn345')), False)
# Test.assert_equals(bool(search(regex, 'jfkdfj3j')), False)
# Test.assert_equals(bool(search(regex, '123')), False)
# Test.assert_equals(bool(search(regex, 'abc')), False)
# Test.assert_equals(bool(search(regex, '123abcABC')), True)
# Test.assert_equals(bool(search(regex, 'ABC123abc')), True)
# Test.assert_equals(bool(search(regex, 'Password123')), True)