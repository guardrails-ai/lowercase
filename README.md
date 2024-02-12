# Overview

| Developed by | Guardrails AI |
| --- | --- |
| Date of development | Feb 15, 2024 |
| Validator type | Format |
| Blog |  |
| License | Apache 2 |
| Input/Output | Output |

# Description

This validator ensures that a generated output is in lower case.

# Installation

```bash
$ guardrails hub install hub://guardrails/lowercase
```

# Usage Examples

## Validating string output via Python

In this example, we’ll test that a generated sentence is lower case.

```python
# Import Guard and Validator
from guardrails.hub import LowerCase
from guardrails import Guard

# Initialize Validator
val = LowerCase(on_fail="fix")

# Setup Guard
guard = Guard.from_string(
    validators=[val, ...],
)

guard.parse("pip install guardrails-ai")  # Validator passes
guard.parse("Pip Install Guardrails-AI")  # Validator fails
```

## Validating JSON output via Python

In this example, we verify that a user’s email is specified in lower case.

```python
# Import Guard and Validator
from pydantic import BaseModel
from guardrails.hub import LowerCase
from guardrails import Guard

val = LowerCase(on_fail="fix")

# Create Pydantic BaseModel
class UserInfo(BaseModel):
		user_name: str
		user_name: str = Field(validators=[val])

# Create a Guard to check for valid Pydantic output
guard = Guard.from_pydantic(output_class=UserInfo)

# Run LLM output generating JSON through guard
guard.parse("""
{
		"user_name": "User Name",
		"user_name": "user@guardrailsai.com"
}
""")
```

# API Reference

`__init__`
- `on_fail`: The policy to enact when a validator fails.
