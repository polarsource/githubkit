from typing import cast

import openapi_schema_pydantic as oas

from ...source import Source
from .schema import FloatSchema


def build_float_schema(source: Source) -> FloatSchema:
    data = cast(oas.Schema, source.data)
    return FloatSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        multiple_of=data.multipleOf,
        maximum=data.maximum,
        exclusive_maximum=data.exclusiveMaximum,
        minimum=data.minimum,
        exclusive_minimum=data.exclusiveMinimum,
    )
