from guardrails import Guard
from validator import LowerCase

guard = Guard.from_string(validators=[LowerCase(on_fail='filter')])

def test_pass():
  test_output = "a test value"
  res = guard.parse(test_output)
  assert(res.validated_output == test_output)

def test_fail():
  test_output = "A test value"
  res = guard.parse(test_output)
  assert(res.validated_output == None)